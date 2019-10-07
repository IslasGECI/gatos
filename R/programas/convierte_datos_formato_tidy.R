# Importa paquetes y funciones
library(data.table)
library(gdata)
library(stringr)
library(stringi)
library(rlang)
source('//pelicano/gatos/R/funciones/fixDateFormat.R')
source('//pelicano/gatos/R/funciones/cats2tidy.R')

# Carga el archivo de interés
nombreComputadora <- paste0("//",Sys.getenv("COMPUTERNAME"))
nombreArchivo <- file.path(nombreComputadora,"datos","POSICION_TRAMPAS.xlsx")
Lista <- list(Datos = data.table(read.xls(nombreArchivo, sheet = 1)), Meta = data.table(read.xls(nombreArchivo, sheet = 2)))
Datos <- Lista$Datos

# Convierte la tabla a formato tidy, corrige el formato de las fechas y guarda el dataframe
Datos <- cats2tidy(Datos)
write.csv(Datos, file = "../../resultados/POSICION_TRAMPAS_TIDY.csv", row.names = FALSE)

# Obtiene la cantidad de datos para cada tipo de fecha y condición de trampa. Suma los renglones tales que tengan condición 'A' o 'X' ya que esta condición nos habla del esfuerzo de trampeo
Datos.suma <- Datos[, .N, by = .(`condicion de la trampa`,Fecha)]
Tabla.esfuerzo <- Datos.suma[`condicion de la trampa` == 'A' | `condicion de la trampa` == 'X', sum(N), by = Fecha]

# Crea la columna de capturas la cual se va a llenar para cada fecha de la tabla "Tabla.esfuerzo". Esto creará un dataframe que contendrá la fecha, el esfuerzo y las capturas
tamanoTablaEsfuerzo = dim(Tabla.esfuerzo)[1]
capturas <- NULL
for (iRenglon in 1:tamanoTablaEsfuerzo){
  Tabla.auxiliar <- Datos.suma[Fecha == Tabla.esfuerzo$Fecha[iRenglon] & `condicion de la trampa` == 'X']
  if (is_empty(Tabla.auxiliar$N)) {
    capturas[iRenglon] = 0
  }else {
    capturas[iRenglon] = Tabla.auxiliar$N
  }
}

Tabla.capturas <- data.table(capturas)
Tabla.esfuerzo.capturas <- data.frame(fecha=Tabla.esfuerzo$Fecha,esfuerzo=Tabla.esfuerzo$V1,capturas=Tabla.capturas$capturas)
write.csv(Tabla.esfuerzo.capturas, file = "../../resultados/captura_gatos_guadalupe.csv", row.names = FALSE)