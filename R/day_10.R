input <- readLines("day_10.txt", warn = FALSE)

.ParseString <- function(input) unlist(strsplit(input, ""))
.SwitchParen <- function (x) return(switch(x, ")" = "(", "]" = "[", ">" = "<", "}" = "{"))

Validate <- function(input) {
  stack <- NULL

  illegal <- NA
  
  for(ii in .ParseString(input)){
    if (
      ii == "(" | ii == "[" | ii == "<" | ii == "{"
    ) {
      stack <- c(stack, ii)
    } else if (stack[length(stack)] == .SwitchParen(ii)) {
      stack <- stack[1:(length(stack) - 1)]
    } else {
      illegal <- ii
      break
    }
  }
  return(illegal)
}

Complete <- function(input) {
  stack <- NULL
  
  for(ii in .ParseString(input)){
    if (
      ii == "(" | ii == "[" | ii == "<" | ii == "{"
    ) {
      stack <- c(stack, ii)
    } else if (stack[length(stack)] == .SwitchParen(ii)) {
      stack <- stack <- if (length(stack) == 1) {NULL} else {stack[1:(length(stack) - 1)]}
    }
  }
  return(stack)
}

Score <- function(input) {
  score <- 0
  for (ii in seq_along(input)) {
    score <- (score * 5) + switch(input[ii], "(" = 1, "[" = 2, "<" = 4, "{" = 3)
  }
  return(score)
}

# Part 1
illegals <- NULL

for (ii in seq_along(input)) {
  check <- Validate(input[ii])
  if (!is.na(check)) illegals <- c(illegals, check)
}

# Part 1 answer
(sum(")" == illegals) * 3) + 
  (sum("]" == illegals) * 57) +
  (sum("}" == illegals) * 1197) +
  (sum(">" == illegals) * 25137)
  
# Part 2
incomplete <- rep(FALSE, length(input))

for (ii in seq_along(input)) {
  if (is.na(Validate(input[ii]))) incomplete[ii] <- TRUE
}

input <- input[incomplete]

calc_scores <- rep(0, length(input))

for (ii in seq_along(input)) {
  calc_scores[ii] <- Score(rev(Complete(.ParseString(input[ii]))))
}

# Part 2 answer
median(calc_scores)
