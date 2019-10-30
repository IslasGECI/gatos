#' @param Datos Un data frame en formato tidy donde una de las columnas contiene las fechas a corregir
#' @return El mismo data frame con el formato de las fechas modificado
#' @examples 
#' @examples
#' 
#' @import rlang
#'  
fixDateFormat <- function(Datos) {
fechaACorregir <- Datos$Fecha
fechaACorregir <- substr(fechaACorregir,2,12)

fechaSeparada <- str_split_fixed(fechaACorregir,'[.]', n = 3)
dia <- fechaSeparada[,1]
mes <- fechaSeparada[,2]
ano <- fechaSeparada[,3]
  
meses <- c("Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic")
reemplazoMeses <- c("01","02","03","04","05","06","07","08","09","10","11","12")

mesCorregido <- NULL
for(i in 1:length(meses)){
  indiceMeses <- grep(meses[i], mes)
  if(!rlang::is_empty(indiceMeses)){
    mes[indiceMeses] <- reemplazoMeses[i]
  }
}
 
fechaConcatenada <- stri_join(ano, mes, dia, sep = '-')
Datos$Fecha <- fechaConcatenada
Salida <- Datos
 
return(Salida)
}
