
input_1 <- as.numeric(readLines("day_1/day_1.txt"))

# Part 1 answer
sum(diff(input_1) > 0)

input_roll <- zoo::rollsum(input_1, 3)

# Part 2 answer
sum(diff(input_roll) > 0)
