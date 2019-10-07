#' Corrige fecha provenientes del archivo \code{POSICION_TRAMPAS.XLSX}
#'
#' Recibe un vector con las fechas y las corrige, dejando las fechas en el formato \code{YYYY-MM-DDThh:mm:ss}. 
#'
#' @author \tabular{l}{
#' David Martínez <david.martinez@@islas.org.mx>
#' }
#'
#' @usage addDateTimeFormat(tabla)
#'  # Agrega tres columnas a los datos: "Date.and.Time"
#'  # con formato as.POSIXct, "Date" con formato
#'  # as.IDate y "Time" con formato as.ITime. TambiÃ©n
#'  # se agregan los metadatos correspondientes.
#'
#' @param tabla(list) Un vector con las fechas a corregir
#'
#' @return  \tabular{ll}{
#'  tabla(list) \tab  El mismo vector pero ahora con las fechas corregidas y con el formato que solicita la convención GECI: \code{YYYY-MM-DDThh:mm:ss}
#' }
#'
#' @references
#'
#' @examples
#'  fixDateFormat(datos)
#'
#'
#'  @seealso \code{funcion 1}, \code{funcion 2}
#'
#' @import gdata, data.table, stringi, stringr
#' @export
fixDateFormat <- function(Datos) {
  fechaACorregir <- Datos$Fecha
  fechaACorregir <- substr(fechaACorregir,2,20)
  fechaSeparada <- str_split_fixed(fechaACorregir,'T',2)
  fecha <- fechaSeparada[,1]
  hora <- fechaSeparada[,2]
  
  fecha <- stri_replace_all_fixed(fecha,'.','-')
  hora <- stri_replace_all_fixed(hora,'.',':')
  
  fechaConcatenada <- stri_join(fecha, hora, sep = 'T')
  
  Datos$Fecha <- fechaConcatenada
  Salida <- Datos
  
  return(Datos)
}

#'
meltTable <- function(nombreArchivo) {
  Lista <- list(Datos = data.table(read.xls(nombreArchivo, sheet = 1)), Meta = data.table(read.xls(nombreArchivo, sheet = 2)))
  Datos <- Lista$Datos
  Meta <- data.table(Lista$Meta)
  
  nombreColumnas <- c(Meta[,1])
  nombreColumnas <- nombreColumnas[nombreColumnas != 'Global']
  
  Datos <- melt(Datos, id = 1:4, variable.name = 'Fecha', value.name = 'condicion de la trampa')
  
  Salida <- Datos
  
  return(Datos)
}