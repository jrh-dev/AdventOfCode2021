input <- sort(scan("day_7.txt", sep = ","))

# Part 1 answer
print(min(unlist(lapply(0:max(input), function(x) sum(abs(input - x))))))

# Part 2 answer
print(min(unlist(lapply(0:max(input), function(i) sum(sapply(input, function (x) sum(seq_along(i:x) - 1)))))))

