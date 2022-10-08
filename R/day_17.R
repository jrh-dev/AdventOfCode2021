# target area: x=29..73, y=-248..-194#

GetTar <- function(x_start, x_end, y_start, y_end) {
  
  tar <- expand.grid(
    x = seq(x_start, x_end, 1),
    y = seq(y_start, y_end, 1)
  )
  
  return (paste0(tar$x, ",", tar$y))
  
}

targets <- GetTar(29, 73, -248, -194)

CheckXSols <- function(x, y, x_end, y_end, valid_hits) {
  
  cur_x <- 0
  cur_y <- 0
  
  vel_x <- x
  vel_y <- y
  
  firing_solution <- FALSE
  
  while (cur_x <= x_end & cur_y >= y_end) {
    
    if (vel_x != 0) {
      cur_x <- cur_x + vel_x
      vel_x <- vel_x - 1
    }
    
    cur_y <- cur_y + vel_y
    vel_y <- vel_y - 1
    
    if (paste0(cur_x, ",", cur_y) %in% valid_hits) {
      firing_solution <- TRUE
    }
  }
  
  return(firing_solution)
}

x_sols <- NULL
y_sols <- NULL

for (ii in abs(-248):-248) {
  for (jj in abs(73):1) {
    if (CheckXSols(jj,ii,73,-248,targets)) {
      x_sols <- c(x_sols, jj)
      y_sols <- c(y_sols, ii)
    }
  } 
}

cur_y <- 0
vel_y <- y_sols[1]
while (vel_y > 0) {
  cur_y <- cur_y + vel_y
  vel_y <- vel_y - 1 
}

# Part 1 answer
cur_y

# Part 2 answer
length(x_sols)


