options(scipen = 999) # prevent numbers going into scientific notation

input <- as.numeric(unlist(strsplit(readLines("day_11.txt", warn = FALSE), "")))

input <- matrix(input, 10, 10, TRUE)

# Pad the matrix with -Inf to make checking surrounding numbers easy
input <- rbind(
  rep(-Inf, 12),
  cbind(rep(-Inf,10), input, rep(-Inf,10)), 
  rep(-Inf, 12)
)

# Initialise objects to catch results in loop
flashes <- 0
all_flash <- 0
iteration <- 0

while (all_flash == 0) {
  
  iteration <- iteration + 1
  
  input[input != -Inf] <- input[input != -Inf] + 1
  
  # Resolve flashes post step if any occurred
  if (any(input[!is.na(input)]  > 9)) {
    
    result <- input
    result[result != -Inf] <- 99
    
    input_change <- TRUE
    
    while(input_change) {
      
      input_catch <- input
      
      for (ii in (1:length(input))[input != -Inf]) {
        
        if (input[ii] < 10) {
          adj <- ii + c(-13:-11, -1, 1, 11:13)
          adj <- adj[adj %in% (1:length(input))[input != -Inf]]
          result[ii] <- input[ii] + sum(input[adj] > 9 & input[adj] != 99)
        }
      }
      
      input <- result
      result[result > 9] <- 99
      
      input_change <- !(identical(input, input_catch))
    }
    
    # Only capture flashes until specified step i.e 100 for part 1
    if (iteration <= 100) flashes <- sum(input > 9) + flashes
    
    input[input > 9] <- 0
  }
  if (all_flash == 0 & all(input[input != -Inf] == 0)) {
    all_flash <- jj
    break # Break when all flash simultaneously
  } 
}

# Part 1 answer
print(flashes)
# Part 2 answer
print(all_flash)