# read from formatted.csv

data <-  read.csv("formatted.csv", header = TRUE, sep = ",")
# best subsets to find the best model predicting the owner_count
# all the other variables except steam_id

library(leaps)
# convert is_multiplayer from T or F to 1 or 0
data$is_multiplayer <- as.numeric(data$is_multiplayer)
best <- regsubsets(owner_count ~ ., data = data, nbest = 1)
summary(best)