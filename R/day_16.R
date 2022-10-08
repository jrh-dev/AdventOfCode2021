options(scipen = 999)

hex_dict <- c(
  "0" = "0000",
  "1" = "0001",
  "2" = "0010",
  "3" = "0011",
  "4" = "0100",
  "5" = "0101",
  "6" = "0110",
  "7" = "0111",
  "8" = "1000",
  "9" = "1001",
  "A" = "1010",
  "B" = "1011",
  "C" = "1100",
  "D" = "1101",
  "E" = "1110",
  "F" = "1111"
)

input <- "9C0141080250320F1802104A08"

input <- readLines("day_16/day_16.txt", warn = FALSE)

ParseInput <- function(str, dict) {
  str <- strsplit(str, "")
  str <- dict[str[[1]]]
  str <- paste0(str, collapse = "")
  return(str)
}

parsed <- ParseInput(input, hex_dict)

# get pac ver and typ
Pack <- function(input, start) {
  
  pac_ver <- strtoi(substr(input, start, start + 2), base = 2)
  
  pac_typ <- strtoi(substr(input, start + 3, start + 5), base = 2)
  
  return(list(ver = pac_ver, typ = pac_typ))
  
}

# strtoi replacement to circumvent overflow
strtod <- function(input){
  x <- as.numeric(strsplit(input, "")[[1]])
  sum(x * 2^rev((seq_along(x)-1)))
}

# get bit type
BitType <- function (input, start) {
  
  typ <- substr(input, start + 6, start + 6)
  
  return(typ)
  
}

# get end for literals
LiteralClose <- function(input, start) {
  
  ii <- start + 6
  
  input_chars <- as.integer(unlist(strsplit(input, "")))
  
  while (input_chars[ii] != 0) {
    ii <- ii + 5
  }
  
  end_actual <- (ii + 4)
  
  return(list(end_actual = end_actual, end_parse = ii))
  
}

# initiate vectors

catch_pack_versions <- NULL

catch_pack_type <- NULL

catch_start_point <- NULL

catch_bit_type <- NULL

catch_pack_len <- NULL

catch_lit <- NULL

start <- 1

# loop
while (start < nchar(parsed)) {
  
  current_pack <- Pack(parsed, start)
  
  catch_pack_versions <- c(catch_pack_versions, current_pack$ver)
  
  catch_pack_type <- c(catch_pack_type, current_pack$typ)
  
  catch_start_point <- c(catch_start_point, start)
  
  if (current_pack$typ == 4) {
    
    catch_bit_type <- c(catch_bit_type, NA)
    
    catch_pack_len <- c(catch_pack_len, NA)
    
    catch_lit <- c(catch_lit, strtod(substr(parsed, start + 6, LiteralClose(parsed, start)$end_parse)))
    
    start <- LiteralClose(parsed, start)$end_actual + 1
    
  } else if (BitType(parsed, start) == "1") {
    
    catch_bit_type <- c(catch_bit_type, 1)
    
    catch_pack_len <- c(catch_pack_len, strtod(substr(parsed, start + 7, start + 17)))
    
    catch_lit <- c(catch_lit, NA)
    
    start <- start + 18
    
  } else {
    
    start <- start + 22
    
    catch_bit_type <- c(catch_bit_type, 0)
    
    catch_pack_len <- c(catch_pack_len, 2)
    
    catch_lit <- c(catch_lit, NA)
    
  }
  print(catch_lit[length(catch_lit)])
}

# Part 1 answer
sum(catch_pack_versions)
