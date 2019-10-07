#' Convierte la tabla `POSICION_TRAMPAS.xlsx` a formato tidy
#'
#' Recibe una tabla en donde algunas columnas son los días donde se colectaron los datos y la convierte en formato tidy
#'
#' @author \tabular{l}{
#' David Martínez <david.martinez@@islas.org.mx>
#' }
#'
#' @usage 
#'
#' @param Datos Un data frame que no es formato tidy. Las primeras 4 columnas son: ID de la trampa, coordenada-X, coordenada-Y y nombre del responsable; las siguientes columnas son las fechas diarias del monitoreo.
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
#' @seealso 
#'
#' @import gdata, data.table, stringi, stringr
#' @export

#'
cats2tidy <- function(Datos){
  Datos <- melt(Datos, id = 1:4, variable.name = 'Fecha', value.name = 'condicion de la trampa')
  Datos <- fixDateFormat(Datos)
  Salida <- Datos
  return(Salida)
}