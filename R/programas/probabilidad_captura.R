# 
remove(list = ls())

# Valores tomados de la tabla 2 del artículo de gatos en San Nicolás (Ramsey,2011)
media <- c(-2.42, 1.57)
desviacionEstandar <- c(0.195, 0.495)

# Esfuerzo arbitrario
esfuerzo <- seq(1,11,1)

# Parámetros de la ecuación 2 del artículo de gatos en San Nicolás (Ramsey,2011)
# Se obtienen los valores de los parámetros de manera aleatoria
alfa <- rnorm(n = length(esfuerzo), mean = media[1], sd = desviacionEstandar[1])
beta <- rnorm(n = length(esfuerzo), mean = media[2], sd = desviacionEstandar[2])
# Ecuación 2: log(p/1-p) = alfa + beta* esfuerzo
logDeProbabilidad <- alfa + beta*esfuerzo

# Se calculan alfa y beta teóricos
(modelo <- lm(logDeProbabilidad ~ esfuerzo))

# Se despeja la probabilidad de la ecuación 2
(probabilidadCaptura <- exp(logDeProbabilidad)/(1+exp(logDeProbabilidad)))

# Los valores de la probabilidad aún no se obtienen. El exponente del logaritmo 
# de la probabilidad es muy grande, lo cual da resultados infinitos.
