input <- strsplit(readLines("day_12.txt", warn = FALSE), "-")

# Capture all possible moves between nodes
moves <- data.frame(
  x = c(unlist(lapply(input, function(x) x[1])), unlist(lapply(input, function(x) x[2]))),
  y = c(unlist(lapply(input, function(x) x[2])), unlist(lapply(input, function(x) x[1])))
)

# Prevent starting with 'end' or ending with 'start'
moves <- moves[moves$x != "end" & moves$y != "start",]

all_caves <- unique(c(moves$x, moves$y))

# Determine small caves, except 'start' and 'end'
small_caves <- all_caves[sapply(all_caves, function (x) all(strsplit(x,"")[[1]] %in% letters[1:26]))]

small_caves <- small_caves[!(small_caves %in% c("start", "end"))]

# Initialise helper objects
map <- moves
mapping <- TRUE
paths <- 0

# Part 1 loop - find all paths visiting small caves a maximum of 1 time
while (mapping) {
  names(map) <- c(paste0("pos",1:(ncol(map) - 1)), "x")
  
  map <- dplyr::left_join(map, moves, by = "x")
  
  map <- map[map$pos1 == "start",]
  
  # Check single use caves not visited twice
  for (ii in seq_along(small_caves)) {
    map <- map[rowSums(map == small_caves[ii], na.rm = T) < 2,]
  }
  
  # Count paths successfully completing
  paths <- paths + sum("end" == map$y, na.rm = TRUE)
  
  map <- map[map$y != "end",]
  
  # Stop when all paths resolve
  if (nrow(map) == 0) {
    mapping <- FALSE
  } 
}

# Part 1 answer
print(paths)

# Part 2 loop - find all paths visiting 1 small cave a maximum of 2 times
#  and all other small caves a maximum of 1 time
for (jj in seq_along(small_caves)) {
  
  map <- moves
  
  mapping <- TRUE
  
  dup_small_caves <- small_caves[!(small_caves %in% small_caves[jj])]
  
  while (mapping) {
  names(map) <- c(paste0("pos",1:(ncol(map) - 1)), "x")
  
  map <- dplyr::left_join(map, moves, by = "x")
  
  map <- map[map$pos1 == "start",]
  
  # check single use caves
  map <- map[rowSums(map == small_caves[jj], na.rm = T) < 3,]
  
  for (ii in seq_along(dup_small_caves)) {
    map <- map[rowSums(map == dup_small_caves[ii], na.rm = T) < 2,]
  }
  
  paths <- paths + sum("end" == map[rowSums(map == small_caves[jj], na.rm = T) == 2,]$y, na.rm = TRUE)
  
  map <- map[map$y != "end",]
  
  if (nrow(map) == 0) {
    mapping <- FALSE
  } 
}
}

# Part 2 answer
print(paths)
