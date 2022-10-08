input <- read.csv("day_2/day_2.txt", header = FALSE)

# Part 1
input <- do.call(rbind, rbind(strsplit(input$V1, "\\s+")))

df <- data.frame(
    dir = input[,1],
    n = input[,2]
)

directions <- lapply(
    split(df, df$dir),
    function(x) {
        sum(as.numeric(x$n))
        }
)

# Part 1 Answer
print((directions$down - directions$up) * directions$forward)

# Part 2
df$n <- as.numeric(df$n)

df$n[df$dir == "up"] <- df$n[df$dir == "up"] * -1

aim <- 0
depth <- 0

for (ii in seq_along(df$dir)) {
    if (df$dir[ii] == "forward") {
        depth <- depth + (aim * df$n[ii])
    } else {
        aim <- aim + (df$n[ii])
    }
}

# Part 2 Answer
print(depth * directions$forward)
