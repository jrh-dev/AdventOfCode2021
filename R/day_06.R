input <- unlist(strsplit(readLines("day_6.txt", warn = FALSE), ","))

group <- as.double(unlist(lapply(0:8 ,function(x) sum(x == input))))

GetFish <- function(x, y){
  for (i in 1:y) {
    new <- x[1]
    x[1:8] <- x[2:9]
    x[7] <- x[7] + new
    x[9] <- new
  }
  return(format(sum(x), scientific = FALSE))
}

GetFish(group, 80)
GetFish(group, 256)