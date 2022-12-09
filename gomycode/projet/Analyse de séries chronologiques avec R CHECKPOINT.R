AirPassengers <- read.csv("C:/Users/ZIGUI OUMARO/Downloads/AirPassengers.csv")
data(AirPassengers)
AP <- AirPassengers
class(AP)
AP
sum(is.na(AP))# rechercher les valeurs manquantes
frequency(AP)  #le cycle de la serie sur 12 mois
summary(AP) 
plot(AP,xlab="Date", ylab = "Passenger numbers (1000's)",main="Air Passenger numbers from 1949 to 1961") 
cycle(AP)
boxplot(AP~cycle(AP),xlab="Date", ylab = "Passenger Numbers (1000's)" ,main ="Monthly Air Passengers Boxplot from 1949 to 1961")
decomposeAP <- decompose(AP,"multiplicative")
autoplot(decomposeAP)
