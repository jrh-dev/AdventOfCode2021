input <- strsplit(readLines("day_8.txt", warn = FALSE), " ")

# Part 1 answer
sum(unlist(lapply(input, function(x) nchar(x[12:15]))) %in% c(2, 3, 4, 7))

<<<<<<< HEAD


=======
>>>>>>> b21afab6e5e48268f6a16283c0f958c91575e411
.WhatNumber <- function(t_1, test, ip_1) {
 
  c1 <- ip_1[nchar(ip_1) == 2]
  c4 <- ip_1[nchar(ip_1) == 4]
  fourdif <- c(substr(c4,1,1),substr(c4,2,2),substr(c4,3,3),substr(c4,4,4))
  fourdif <- fourdif[!(fourdif %in% c(substr(c1,1,1),substr(c1,2,2)))]
  
  if (nchar(test) == 2) {is <- 1}
  if (nchar(test) == 4) {is <- 4}
  if (nchar(test) == 3) {is <- 7}
  if (nchar(test) == 7) {is <- 8}
  
  if (nchar(test) == 5) {
    if (
      all(unlist(strsplit(c1,"")) %in% unlist(strsplit(test,"")))
        ) {
      is <- 3
    } else {
      if (
        all(unlist(strsplit(fourdif,"")) %in% unlist(strsplit(test,"")))
        ) {
        is <- 5
      } else {
        is <- 2
      }
    }
  }
  
  if (nchar(test) == 6) {
    if (
      all(unlist(strsplit(c4,"")) %in% unlist(strsplit(test,"")))
    ) {
      is <- 9
    } else {
      if (
        all(unlist(strsplit(fourdif,"")) %in% unlist(strsplit(test,"")))
      ) {
        is <- 6
      } else {
        is <- 0
      }
    }
  }
  return(is)
}

<<<<<<< HEAD

Decoder <- function(ip_1, ip_2) {
  
=======
Decoder <- function(ip_1, ip_2) {
 
>>>>>>> b21afab6e5e48268f6a16283c0f958c91575e411
  catch <- rep(NA, 4)
  
  for (ii in 1:4) {
    catch[ii] <- .WhatNumber(
      t_1 = unlist(strsplit(ip_1, "")),
      test = ip_2[ii],
      ip_1 = ip_1
    )
  }
<<<<<<< HEAD
  
=======
>>>>>>> b21afab6e5e48268f6a16283c0f958c91575e411
  return(as.numeric(paste0(catch, collapse = "")))
}

out <- rep(NA, 200)

for(jj in 1:200){
  out[jj] <- Decoder(
  ip_1=lapply(input, function(x) x[1:10])[[jj]],
  ip_2=lapply(input, function(x) x[12:15])[[jj]]
)
}

# Part 2 answer
sum(out)
