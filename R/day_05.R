coord <- strsplit(readLines("day_5.txt", warn = FALSE), " -> ")

Intersections <- function (input, diag = FALSE) {
  out <- lapply(input, function(z) {
    
    x = as.numeric(gsub(".*,", "", z))
    y = as.numeric(gsub(",.*", "", z))
    
    if (diff(x) != 0 & diff(y) != 0) {
      if (diag) {
        paste0(y[1]:y[2], ",", x[1]:x[2])
      } else {
        NA
      }
    } else {
      if (diff(x) == 0) {
        paste0(y[1]:y[2], ",", unique(x))
      } else {
        paste0(unique(y), ",", x[1]:x[2])
      }
    }
  }
  )
  return(sum(table(unlist(out)) >= 2))
}

# Part 1 answer
Intersections(coord, diag = FALSE)

# Part 2 answer
Intersections(coord, diag = TRUE)
