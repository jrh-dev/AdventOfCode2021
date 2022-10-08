options(scipen = 999)

input <- readLines("day_15.txt", warn = FALSE)

input <- matrix(as.double(unlist(strsplit(as.character(input), ""))), length(input), length(input), TRUE)

# Logical to specify whether processing part 1 or part 2
part_2 <- FALSE

# For part 2 we expand the input, increasing the values (resetting any exceeding 9)
if (part_2) {
  for (jj in 1:4) {
    input <- cbind(input, input[,(ncol(input) - 99):ncol(input)] + 1)
    input[input >= 10] <- input[input >= 10] - 9
  }
  
  for (kk in 1:4) {
    input <- rbind(input, input[(nrow(input) - 99):nrow(input),] + 1)
    input[input >= 10] <- input[input >= 10] - 9
  }
}

# Functions

# Boundaries() returns a list of indices at the 'edge' of the matrix
Boundaries <- function(n_cols, n_rows) {
  tl = 1
  tr = (n_cols * n_rows) - n_cols + 1
  bl = n_rows
  br = n_cols * n_rows
  top = seq(tl + n_rows, tr - n_rows, n_rows)
  bot = seq(bl + n_rows, br - n_rows, n_rows)
  lft = seq(tl, bl, 1)
  rgt = seq(tr, br, 1)
  return(list(tl = tl, tr = tr, bl = bl, br = br, top = top, bot = bot, lft = lft, rgt = rgt))
}

# Moves() returns the indices of adjacent 'nodes', adapted to the matrix 'boundaries'
Moves <- function(bounds, current) {
  if (current == bounds$tl) {
    out = c(current + 1, current + bounds$bl)
  } else if (current == bounds$tr) {
    out = c(current + 1, current - bounds$bl)
  } else if (current == bounds$bl) {
    out = c(current - 1, current + bounds$bl)
  } else if (current == bounds$br) {
    out = c(current - 1, current - bounds$bl)
  } else if (any(current == bounds$top)) {
    out = c(current + 1, current - bounds$bl, current + bounds$bl)
  } else if (any(current == bounds$bot)) {
    out = c(current - 1, current - bounds$bl, current + bounds$bl)
  } else if (any(current == bounds$lft)) {
    out = c(current - 1, current + 1, current + bounds$bl)
  } else if (any(current == bounds$rgt)) {
    out = c(current - 1, current + 1, current - bounds$bl)
  } else {
    out = c(current - 1, current + 1, current - bounds$bl, current + bounds$bl)
  }
  return(out)
}

# GetNext() returns the index of the next 'node' to visit
GetNext <- function (path, visited) {
  path[visited[visited != Inf]] <- Inf
  return(which.min(path))
}

bounds <- Boundaries(ncol(input), nrow(input))

# Initialise a matrix to record the path, values start as Inf except index 1
path <- input

path[1:length(path)] <- Inf

path[1,1] <- 0

# Initialise a vector to capture nodes visited, hopefully quicker than growing the vector
visited <- rep(Inf, ncol(path) * nrow(path))

current <- 1

cycle <- 0

while (current != ncol(path) * nrow(path)) {
  cycle <- cycle + 1
  
  current <- GetNext(path, visited)
  
  to_check <- Moves(bounds, current)
  
  for (ii in to_check) {
    path[ii] <- min(path[ii], input[ii] + path[current])
  }
  
  visited[cycle] <- current
  
}

# Print answer
print(path[ncol(path) * nrow(path)])
