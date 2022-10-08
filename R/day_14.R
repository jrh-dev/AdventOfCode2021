# Day 14 - total run time <2.5s
# Set option to prevent scientific notation of long numbers
options(scipen = 999)

# Get starter string
string <- readLines("day_14.txt", 1)

string <- unlist(strsplit(string, ""))

# Identify final letter to add after iterations
final_letter <- string[(length(string))]

# Create a lookup table for how pairs split and create new pairs
lookup <- read.table("day_14.txt", skip = 2, sep = " ")

lookup$V4 <- paste0(substr(lookup$V1, 1, 1), lookup$V3) 

lookup$V5 <- paste0(lookup$V3, substr(lookup$V1, 2, 2))

lookup <- lookup[order(lookup$V1),]

# Process for parts 1 & 2 is identical, just addition itterations
#  loop quicker to write out than function in this case.
for (parts in c(10, 40)) {
  
  # Initialise a df for capturing
  pair_track <- merge(
    data.frame(Var1 = lookup$V1), 
    as.data.frame(
      table(
        paste0(string[1:(length(string) - 1)], string[2:length(string)])
      )
    ),
    on = "V1",
    all.x = TRUE
  )
  
  pair_track$Freq[is.na(pair_track$Freq)] <- 0
  
  # Loop through pair additions, counting new ones and dropping split pairs
  for (iterations in 1:parts) {
    tmp <- pair_track
    
    for (ii in 1:nrow(tmp)) {
      add <- tmp$Freq[tmp$Var1 == tmp$Var1[ii]]
      pair_track$Freq[pair_track$Var1 == lookup$V4[ii]] <- pair_track$Freq[pair_track$Var1 == lookup$V4[ii]] + add
      pair_track$Freq[pair_track$Var1 == lookup$V5[ii]] <- pair_track$Freq[pair_track$Var1 == lookup$V5[ii]] + add
      pair_track$Freq[pair_track$Var1 == tmp$Var1[ii]] <- pair_track$Freq[pair_track$Var1 == tmp$Var1[ii]] - add
    }
  }
  
  pair_track$Var1 <- substr(pair_track$Var1,1,1)
  
  pair_track <- aggregate(pair_track$Freq, by = list(pair_track$Var1), FUN = sum)
  
  pair_track$x[pair_track$Group.1 == final_letter] <- pair_track$x[pair_track$Group.1 == final_letter]  + 1
  
  ans <- max(pair_track$x) - min(pair_track$x)
  
  # Print answers
  if (parts == 10) {
    print(paste0("Part 1 answer ", ans))
  } else {
    print(paste0("Part 2 answer ", ans))
  }
}
