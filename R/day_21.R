
.end_on <- function(x) x - (x - (x %% 10))

get_ans = function(p1_start, p2_start){
  rolls = rep(1:100, 9000)
  
  p1 = cumsum(rolls[c(T,T,T,F,F,F)])
  p2 = cumsum(rolls[c(F,F,F,T,T,T)])
  
  p1 <- .end_on(p1[seq(3, length(p1), 3)] + p1_start)
  p2 <- .end_on(p2[seq(3, length(p2), 3)] + p2_start)
  
  p1[p1 == 0] <- 10
  p2[p2 == 0] <- 10
  
  p1_win_n = sum(cumsum(p1) < 1000) + 1
  
  p2_win_n = sum(cumsum(p2) < 1000) + 1
  
  if (min(p1_win_n, p2_win_n) == p1_win_n) {
    # if p1 wins
    rolls = (p1_win_n * 3) + ((p1_win_n - 1) * 3)
    lose_score = sum(p2[1:(p1_win_n - 1)])
  } else {
    # if p2 wins
    rolls = (p2_win_n * 3) + ((p2_win_n - 1) * 3)
    lose_score = sum(p1[1:(p2_win_n - 1)])
  }
  return(lose_score * rolls)
}


# Part 1 answer
get_ans(7,9)

