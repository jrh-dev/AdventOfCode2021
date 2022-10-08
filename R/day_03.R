input <- readLines("day_3/day_3.txt", warn = FALSE)

# Part 1
catch_gamma <- catch_epsilon <- vector(mode = 'list', length = nchar(input[1]))

for (ii in seq_len(nchar(input[1]))) {
  tmp <- sum(as.numeric(substr(input,ii,ii))) > length(input) / 2
  catch_gamma[ii] <- tmp
  catch_epsilon[ii] <- (!tmp)
}

bin2dec <- function(x) {
  strtoi(paste(as.numeric(unlist(x)), collapse=''), base = 2)
}

# Part 1 answer
print(bin2dec(catch_gamma) * bin2dec(catch_epsilon))

# Part 2
i.x <- i.y <- input


for (ii in seq_len(nchar(i.x[1]))) {
  oxy_tmp <- sum(as.numeric(substr(i.x, ii, ii))) >= length(i.x) / 2
  i.x <- i.x[substr(i.x, ii, ii) == as.numeric(oxy_tmp)]
  if(length(i.x) == 1) {break}
}

for (ii in seq_len(nchar(i.y[1]))) {
  co2_tmp <- sum(as.numeric(substr(i.y, ii, ii))) < length(i.y) / 2
  i.y <- i.y[substr(i.y, ii, ii) == as.numeric(co2_tmp)]
  if(length(i.y) == 1) {break}
}

# Part 2 answer
print(bin2dec(i.x) * bin2dec(i.y))
