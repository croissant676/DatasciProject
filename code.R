# read from formatted.csv

data <-  read.csv("formatted.csv", header = TRUE, sep = ",")
# best subsets to find the best model predicting the owner_count
# all the other variables except steam_id

library(leaps)
# convert is_multiplayer from T or F to 1 or 0
data$is_multiplayer <- as.numeric(data$is_multiplayer)
data$is_mac <- as.numeric(data$is_mac)

#make sure to run install.packages("leaps") before using this library
#we need the library for the regsubsets() function,
#this function produces an exhaustive search for the best subsets of the full model,
#you can make it go forwards or backwards
library(leaps)
out <- summary(regsubsets(log(owner_count) ~ . + log(steam_rating) + log(metacritic_rating) + log(igdb_rating) + log(metacritic_score) + log(full_price) + log(achievements) + log(tag_count) + I(metacritic_rating * steam_rating * igdb_rating), data = data[,c(3,4,5,6,7,8,9,10,11,12,13)], nbest = 2, really.big = T))
Subsets<-out$which #tells us which subsets are used (T/F)
R2<-round(100*out$rsq,1) #storing a list of all R2 percentages
R2adj<-round(100*out$adjr2,1) #storing a list of all R2adj percentages
Cp<-round(out$cp,1) #storing a list of all Mallows' Cp values
cbind(Subsets,R2,R2adj,Cp) #output a dataframe showing all the info we just collected