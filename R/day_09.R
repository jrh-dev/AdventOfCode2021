main <- as.matrix(read.fwf("day_9.txt",rep(1,100)), 100, 100)

xlen <- ncol(main)
ylen <- nrow(main)

right <- main[,2:xlen]
right <- cbind(right, rep(NA,ylen))

left <- main[1:ylen,1:(xlen - 1)]
left <- cbind(rep(NA,ylen), left)

up <- main[2:ylen,1:xlen]
up <- rbind(up, rep(NA,xlen))

down <- main[1:(ylen - 1),1:xlen]
down <- rbind(rep(NA) ,down)

result <-  matrix(FALSE, nrow = ylen, ncol = xlen, byrow = TRUE)

for (ii in 1:(ylen * xlen)) {
  result[ii] <- all(
    main[ii] < right[ii],
    main[ii] < left[ii],
    main[ii] < up[ii],
    main[ii] < down[ii],
    na.rm = TRUE
  )
}

# Part 1 answer
sum(main[result] + 1)

map <- matrix(0, nrow = ylen, ncol = xlen, byrow = TRUE)

group_inc <- 1

for (ii in 1:(ylen * xlen)) {
  if (result[ii]) {
    map[ii] <- group_inc
    group_inc <- group_inc + 1
  }
}

change_detect <- TRUE

while(change_detect){
  map_tmp <- map
  for (jj in 1:xlen) {
    for (ii in 1:ylen) {
      try(if (map[ii,(jj + 1)] > 0 & main[ii,(jj + 1)] < main[ii,jj] & main[ii,jj] != 9)
        map[ii,jj] <- map[ii,(jj + 1)], silent = TRUE)
      try(if (map[ii,(jj - 1)] > 0 & main[ii,(jj - 1)] < main[ii,jj] & main[ii,jj] != 9)
        map[ii,jj] <- map[ii,(jj - 1)], silent = TRUE)
      try(if (map[(ii + 1),jj] > 0 & main[(ii + 1),jj] < main[ii,jj] & main[ii,jj] != 9)
        map[ii,jj] <- map[(ii + 1),jj], silent = TRUE)
      try(if (map[(ii - 1),jj] > 0 & main[(ii - 1),jj] < main[ii,jj] & main[ii,jj] != 9)
        map[ii,jj] <- map[(ii - 1),jj], silent = TRUE)
    }
  }
  change_detect <- !(identical(map_tmp, map))
}

# Part 2 answer
prod(sort(table(map[map != 0]), decreasing = TRUE)[1:3])