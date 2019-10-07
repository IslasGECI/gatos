import bokeh.io as bi
import bokeh.models as bm
import bokeh.plotting as bp
from bokeh.embed import components
from bokeh.models import ColumnDataSource, Circle, HoverTool, CustomJS
import matplotlib.pyplot as plt
from collections import OrderedDict
import numpy as np
from bokeh.models import NumeralTickFormatter

AZUL_GECI = "#2957A4"
VERDE_GECI = "#00A859"
HERRAMIENTAS = "box_zoom,box_select,save,reset"
ANCHO_GRAFICA = int(800 * .8)
ALTO_GRAFICA = int(500 * .8)
ANCHO_LINEA = 3
RUTA_RESULTADOS = "resultados/"

def set_plot_format(plot_handle):
    plot_handle.xaxis.formatter = NumeralTickFormatter(format="0,0")

    plot_handle.xaxis.axis_label_text_font = "verdana"
    plot_handle.xaxis.axis_label_text_font_style = "normal"
    plot_handle.xaxis.axis_label_text_font_size = "16pt"
    plot_handle.xaxis.major_label_text_font_size = "16pt"
    plot_handle.yaxis.axis_label_text_font = "verdana"
    plot_handle.yaxis.axis_label_text_font_style = "normal"
    plot_handle.yaxis.axis_label_text_font_size = "16pt"
    plot_handle.yaxis.major_label_text_font_size = "16pt"
    plot_handle.plot_width = ANCHO_GRAFICA
    plot_handle.plot_height = ALTO_GRAFICA
    plot_handle.toolbar_location = None
    plot_handle.grid.visible = False

    plot_handle.min_border_right = 50
    plot_handle.min_border_top = 60
    plot_handle.min_border_bottom = 50
    plot_handle.min_border_left = 50

class RemanentCatPlotter:
    
    ''' Objeto encargado de generar las gráficas
    de gatos remanentes.

    El constructor acepta que se le pase la distribucion del tamaño de la población inicial, las capturas,
    el valor_mas_probable y el intervalo de confianza. Si no se le pasan aquí se puede utilizar el
    método `set_values()`    
    '''

    def __init__(self, distribucion_posterior_No=None, capturas=None, valor_mas_probable=None, intervalo_confianza=None):        
        self.set_values(distribucion_posterior_No, capturas, valor_mas_probable, intervalo_confianza)        

    def set_values(self, distribucion_posterior_No: np.array, total_capturas: int, valor_mas_probable, intervalo_confianza):
        ''' Método encargado de inicializar los valores necesarios para crear las gráficas
        '''
        self._distribucion_posterior_No = distribucion_posterior_No
        self._total_capturas = total_capturas
        self._valor_mas_probable = valor_mas_probable
        self._intervalo_confianza = intervalo_confianza
        self._init_plots_values()

    def _init_plots_values(self):
        ''' Función encargada de iniciar los valores necesarios para generar las gráficas
        solo debe ser llamado por el método `set_values`
        '''
        self._bins_necesarios: int = max(self._distribucion_posterior_No) - min(self._distribucion_posterior_No)    
        self._histograma_completo, self.lados, _ = plt.hist(self._distribucion_posterior_No, bins=self._bins_necesarios, normed=1)
        self._bins_trasladados = self.lados - self._total_capturas
        self._bins_centrados = (self._bins_trasladados[:-1] + self._bins_trasladados[1:])/2
        self._indice_valor_mas_probable = np.argmin(abs(self._bins_centrados - self._valor_mas_probable))
        self._es_inferior = (self._bins_centrados < self._intervalo_confianza.min())
        self._es_superior = (self._bins_centrados > self._intervalo_confianza.max())   
        self._integral = self._histograma_completo.cumsum() 
        self._fuente = bp.ColumnDataSource({'x': self._bins_centrados, 'p': self._histograma_completo, 'c': self._integral})
        self._indice_ultimo_inferior = np.argmax(~self._es_inferior);
        self._indice_primer_superior = np.argmax(self._es_superior);

    def get_cat_status_plots(self):
        ''' Método que regresa las gráficas (PDF y CDF) de los gatos remanentes
        '''   
        pdf = self.get_pdf_status_plot()
        cdf = self.get_cdf_status_plot()
        p = bp.gridplot([[pdf, cdf]], toolbar_options={'logo': None})
        return p

    def get_pdf_status_plot(self):
        ''' Método que regresa las gráficas PDF de los gatos remanentes
        ''' 
        encima_pdf = bm.HoverTool(tooltips=[("Number of cats remaining", "@x"),("Probability", "@p")], mode='vline')
        pdf = bp.figure(x_axis_label='Number of cats remaining', y_axis_label='Probability',
            y_range=(0,0.035), tools=[encima_pdf, HERRAMIENTAS])
        pdf.vbar(x = self._bins_centrados, top=self._histograma_completo, bottom=0, width = 1, fill_color=AZUL_GECI)
        pdf.line([self._valor_mas_probable, self._valor_mas_probable], [0, self._histograma_completo.max()], line_width=5, line_color="DarkOrange")
        pdf.vbar(x = self._bins_centrados[self._es_inferior], top=self._histograma_completo[self._es_inferior], bottom=0, width = 1, fill_color=VERDE_GECI, line_color=VERDE_GECI)
        pdf.vbar(x = self._bins_centrados[self._es_superior], top=self._histograma_completo[self._es_superior], bottom=0, width = 1, fill_color=VERDE_GECI, line_color=VERDE_GECI)
        pdf.line('x','p', source=self._fuente, line_alpha=0)
        pdf.grid.visible = False        
        pdf.text(x = [self._intervalo_confianza[0]], y=[self._histograma_completo[self._indice_ultimo_inferior]], text=[self._intervalo_confianza[0]], text_align='right')
        pdf.text(x = [self._intervalo_confianza[1]], y=[self._histograma_completo[self._indice_primer_superior]], text=[self._intervalo_confianza[1]], text_align='left')
        pdf.text(x = [self._valor_mas_probable], y=[self._histograma_completo[self._indice_valor_mas_probable]+0.001], text=[self._valor_mas_probable], text_align='center', text_baseline = 'bottom')
        set_plot_format(pdf)
        bi.export_png(pdf, filename=RUTA_RESULTADOS +
                      "pdf_cantidad_gatos_remanentes.png")
        return pdf

    def get_cdf_status_plot(self):
        ''' Método que regresa las gráficas CDF de los gatos remanentes
        ''' 
        encima_cdf = bm.HoverTool(tooltips=[("Number of cats remaining", "@x"), ("Probability", "@c")], mode='vline')
        
        cdf = bp.figure(x_axis_label="Number of cats remaining",\
                        y_axis_label='Probability', y_range=(0, 1), x_range=(0, 150), tools=[encima_cdf, HERRAMIENTAS])
        cdf.grid.visible = False
        cdf.line('x', 'c', line_width=ANCHO_LINEA, line_color=AZUL_GECI, source=self._fuente)
        cdf.line([self._bins_centrados[self._indice_primer_superior], self._bins_centrados[self._indice_primer_superior]],[0, self._integral[self._indice_primer_superior]], line_width=3, line_color=VERDE_GECI)
        cdf.line([self._bins_centrados[self._indice_ultimo_inferior], self._bins_centrados[self._indice_ultimo_inferior]],[0, self._integral[self._indice_ultimo_inferior]], line_width=3, line_color=VERDE_GECI)
        fuenteVMP = bp.ColumnDataSource({'x': [self._valor_mas_probable], 'p': [self._histograma_completo.max()], 'c': [self._integral[self._indice_valor_mas_probable]]})        
        cdf.line([self._valor_mas_probable, self._valor_mas_probable], [0, self._integral[self._indice_valor_mas_probable]], line_width=3, color="DarkOrange")
        set_plot_format(cdf)
        bi.export_png(cdf, filename=RUTA_RESULTADOS +
                      "cdf_cantidad_gatos_remanentes.png")

        return cdf

class EradicationSuccesPlotter:
    
    ''' Objeto encargado de generar las gráficas del éxito de la erradicación

    El constructor acepta que se le pase un vector de esfuerzo (en noches*trampa) y la 
    probabilidad de captura de remanentes. Si no se le pasan aquí se puede utilizar el 
    método `set_values()`
    '''

    def set_values(self, esfuerzo_noches_trampa, probabilidad_captura_remanentes):
        ''' Método encargado de inicializar los valores necesarios para crear las gráficas
        '''
        self._esfuerzo_noches_trampa = esfuerzo_noches_trampa
        self._probabilidad_captura_remanentes = probabilidad_captura_remanentes

    def _init_plot_values(self):
        pass
    
class CatchPerEffortPlotter:

    def __init__(self, esfuerzo_acumulado=None, capturas_acumuladas=None, capturas_por_esfuerzo=None):
        self.set_values(esfuerzo_acumulado, capturas_acumuladas, capturas_por_esfuerzo)

    def set_values(self, esfuerzo_acumulado: np.array, capturas_acumuladas: np.array, capturas_por_esfuerzo: np.array):
        ''' Método encargado de inicializar los valores necesarios para crear las gráficas
        '''
        self._esfuerzo_acumulado = esfuerzo_acumulado
        self._capturas_acumuladas = capturas_acumuladas
        self._capturas_por_esfuerzo = capturas_por_esfuerzo
        self._init_column_data_source()

    def _init_column_data_source(self):
        ''' Función encargada de iniciar los valores necesarios para generar las gráficas
        solo debe ser llamado por el método `set_values`
        '''
        self._column_data_source = bp.ColumnDataSource({'esfuerzo_acumulado': self._esfuerzo_acumulado, 'capturas_acumuladas': 
                                                        self._capturas_acumuladas, 'capturas_por_esfuerzo': self._capturas_por_esfuerzo})

    def show_catch_effort_plots(self):
        ''' Método que regresa las gráficas (PDF y CDF) de los gatos remanentes
        '''
        p1 = self.plot_catch_per_effort_by_cumulative_effort()
        p2 = self.plot_cummulative_catch_by_cumulative_effort()
        p = bp.gridplot([[p1, p2]],
                        toolbar_options={'logo': None})
        return p

    def plot_cummulative_catch_by_cumulative_effort(self):

        fuente = self._column_data_source
        encima_p1 = bm.HoverTool(tooltips=[
        ("Cumulative effort", "@esfuerzo_acumulado"),
        ("Cumulative removals", "@capturas_acumuladas")],
        mode='vline')

        
        ## Grafica de capturas acumuladas vs esfuerzo acumulado    
        limite_y = 700
        opciones_grafica = dict(x_axis_label='Cumulative effort',
                                y_axis_label='Cumulative removals', y_range=(0,limite_y),\
                                tools=[encima_p1, HERRAMIENTAS])

        p1 = bp.figure(**opciones_grafica)    
        set_plot_format(p1)
        p1.circle('esfuerzo_acumulado', 'capturas_acumuladas',
                  size=10, color=AZUL_GECI, source=fuente)
        bi.export_png(p1, filename=RUTA_RESULTADOS +
                      "capturas_acumuladas_vs_esfuerzo_acumulado.png")
        return p1

    def plot_catch_per_effort_by_cumulative_effort(self):
        fuente = self._column_data_source
        
        ## Grafica de Capturas por esfuerzo vs esfuerzo acumulado    
        limite_y = 0.10
        encima_p2 = bm.HoverTool(tooltips=[
                ("Cumulative effort", "@esfuerzo_acumulado"),
                ("Removals per effort", "@capturas_por_esfuerzo")],
                mode='vline')

        opciones_grafica = dict(x_axis_label='Cumulative effort',
                                y_axis_label='Removals per effort', y_range=(0, limite_y),
                                tools=[encima_p2, HERRAMIENTAS])

        p2 = bp.figure(**opciones_grafica)    
        set_plot_format(p2)
        p2.circle(
            'esfuerzo_acumulado', 'capturas_por_esfuerzo', size=10, color=AZUL_GECI, source=fuente)
        bi.export_png(p2, filename=RUTA_RESULTADOS +
                      "capturas_por_esfuerzo_vs_esfuerzo_acumulado.png")
        return p2

class RemanentCatCatchesPlotter:
    
    ''' Objeto encargado de generar las gráficas de las capturas de gatos remanentes.

    El constructor recibe los valores de las variables que se graficarán`    
    '''

    def __init__(self, esfuerzo_trampas: np.array, remanentes_capturados : np.array, derivada: np.array, esfuerzo_para_derivada : np.array):        
        self.fuente = bp.ColumnDataSource(
            data = dict(
                esfuerzo_trampas=esfuerzo_trampas,
                remanentes_capturados=remanentes_capturados,
                derivada = derivada,
                esfuerzo_derivada = esfuerzo_para_derivada
                )
            )

    def show_remanent_catch_effort_plots(self):
        ''' Método que regresa las gráficas (PDF y CDF) de los gatos remanentes
        '''
        p1 = self.plot_derivate_catch_remanent_by_cumulative_effort()
        p2 = self.plot_catch_remanent_by_cumulative_effort()
        p = bp.gridplot([[p1, p2]],
                        toolbar_options={'logo': None})
        return p

    def plot_catch_remanent_by_cumulative_effort(self):
        encima_p2 = bm.HoverTool(tooltips=[
            ("Catch of remaining cats", "@remanentes_capturados"),
            ("Number of trappers", "@esfuerzo_trampas")], 
            mode='vline'
        ) 
        
        opciones_grafica = dict(x_axis_label='Number of trappers', x_range=(0, 60),
                                y_axis_label='Catch of remaining cats',
                                tools=[encima_p2, HERRAMIENTAS])

        p2 = bp.figure(**opciones_grafica)    
        set_plot_format(p2)
        p2.line(x='esfuerzo_trampas', y='remanentes_capturados',
                line_width=ANCHO_LINEA, line_color=AZUL_GECI, source=self.fuente)
        bi.export_png(p2, filename=RUTA_RESULTADOS +
                      "capturas_remanentes_vs_esfuerzo.png")
        return p2

    def plot_derivate_catch_remanent_by_cumulative_effort(self):
        encima_p1 = bm.HoverTool(tooltips=[
            ("Catch per trapper", "@derivada"),
            ("Number of trappers", "@esfuerzo_derivada")], 
            mode='vline'
        )
        
        opciones_grafica = dict(x_axis_label='Number of trappers', x_range=(0, 60), y_range=(0, 2.0),
                                y_axis_label='Catch per trapper', 
                                tools=[encima_p1, HERRAMIENTAS])

        p1 = bp.figure(**opciones_grafica)    
        set_plot_format(p1)
        p1.line(x='esfuerzo_derivada', y='derivada',
                line_width=ANCHO_LINEA, line_color=AZUL_GECI, source=self.fuente)
        p1.yaxis.formatter = NumeralTickFormatter(format="0.0")
        bi.export_png(p1, filename=RUTA_RESULTADOS +
                      "derivada_capturas_remanentes_vs_esfuerzo.png")
        return p1

        
