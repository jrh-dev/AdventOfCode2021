library(ggplot2)

nput <- readLines("day_13.txt",  warn = FALSE)

split_at <- sum((1:length(input))[match(input, "") == 1], na.rm = TRUE)

dots <- input[1:(split_at - 1)]

folds <- strsplit(gsub("fold along ", "", input[(split_at + 1):length(input)]), "=")

coords <- data.frame(matrix(as.double(unlist(strsplit(dots,","))), length(dots), 2, T), stringsAsFactors = F)

names(coords) <- c("x", "y")

Folder <- function (axis, fold_pos, data) {
  coords$tmp <- coords[[axis]]
  coords$tmp <- (fold_pos * 2) - coords$tmp
  coords$tmp[coords$tmp > fold_pos] <- coords[[axis]][coords$tmp > fold_pos]
  coords[[axis]] <- coords$tmp
  coords$tmp <- NULL
  return(coords)
}

# Part 1 answer
nrow(unique(Folder(folds[[1]][1], as.numeric(folds[[1]][2]), coords)))

for (ii in seq_along(folds)){
  coords <- Folder(folds[[ii]][1], as.numeric(folds[[ii]][2]), coords)
}

# Part 2 answer
ggplot(coords, aes(x, -y)) + 
  geom_tile() + theme_minimal()