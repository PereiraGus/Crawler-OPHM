arquivo <- read.csv2("C:/Users/gusta/OneDrive - SPTech School/Área de Trabalho/Crawler-OPHM/ETL/raw.csv")
df <- data.frame(arquivo) 
df

#Computadores e modelo da CPU
insight_pc_cpu <- function(){
  pc <- df$nome_pc[1]
  cpu <- df$cpu_modelo[1]
  print(paste("Computador examinado:",pc))
  print(paste("Modelo de CPU:",cpu))
}

#Uso CPU e RAM x tempo
insight_cpu_ram <- function(){
  plot(df$cpu_uso,type="l",
     main="CPU e RAM de acordo com o tempo",
     xlab="Instante de tempo",
     ylab="% de uso",col="blue")
  lines(df$ram_uso, col="red")
  legend("topright",legend=c("CPU","RAM"),fill=c("red","blue"),cex=0.9)
}

#Temperaturas máxima, média e mínima
insight_temperatura <- function(){
  valores <- c(max(df$cpu_temp),mean(df$cpu_temp),min(df$cpu_temp))
  cores <- c("red","lightgreen","lightblue")
  barplot(
    valores,
    names = paste(valores,"ºC"),
    col = cores,ylim=c(0,140)
  )
  legend("topright",
         legend=c("Temperatura mais alta","Temperatura média","Temperatura mais baixa"),
         fill=cores,cex=0.7)
}

#Consumo energético total
insight_energia <- function(){
  kW <- round(sum(df$cpu_energia)/1000,1)
  print(paste("Consumo energético total:",kW,"KW"))
  print(paste("Gasto com eletricidade: R$",round(kW*0.649,2)))
}

insight_pc_cpu()
insight_cpu_ram()
insight_temperatura()
insight_energia()
