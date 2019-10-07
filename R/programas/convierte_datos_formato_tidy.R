# Importa paquetes y funciones
library(data.table)
library(gdata)
library(rgdal)
library(rlang)
library(stringr)
library(stringi)
source('//pelicano/gatos/R/funciones/fixDateFormat.R')
source('//pelicano/gatos/R/funciones/cats2tidy.R')

# Carga el archivo de interés
rutaInstextdata <- "../../inst/extdata/"
nombre.archivos <- list.files(path = rutaInstextdata, pattern = "POSICION")

# Convierte la tabla a formato tidy, corrige el formato de las fechas y guarda el dataframe
Tabla.concatenada <- data.table(ID = factor(), Coor.X = integer(), Coor.Y = integer(), Nombre.del.responsable = factor(), Fecha = character(), "condicion de la trampa" = character())
for(iArchivo in nombre.archivos){
  Datos.auxiliar <- data.table(read.xls(paste0(rutaInstextdata,iArchivo), sheet = 1))
  Datos.auxiliar <- cats2tidy(Datos.auxiliar)
  Tabla.concatenada <- rbind(Tabla.concatenada,Datos.auxiliar)
}
colnames(Tabla.concatenada)[6] <- 'condicion'
colnames(Tabla.concatenada)[4] <- 'responsable'
colnames(Tabla.concatenada)[5] <- 'fecha'

# Convierte datos a lon lat
coordenadas.utm <- data.frame(x=Tabla.concatenada$Coor.X, y=Tabla.concatenada$Coor.Y)
coordinates(coordenadas.utm) <- ~x+y
proj4string(coordenadas.utm) <- CRS("+proj=utm +zone=11 +datum=WGS84 +units=m +ellps=WGS84")
lonLat <- spTransform(coordenadas.utm,CRS("+proj=longlat +datum=WGS84"))

Tabla.concatenada$longitud <- lonLat$x
Tabla.concatenada$latitud <- lonLat$y

#
Datos <- Tabla.concatenada
nombre.archivo.salida.monitoreo.trampas <- "../../resultados/trampas_monitoreo_gatos_islaGuadalupe.csv"
write.csv(Datos, file = nombre.archivo.salida.monitoreo.trampas, row.names = FALSE, quote = FALSE, fileEncoding = "UTF-8")

