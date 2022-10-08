# Combine 2 numbers into the pair format
Combine = function (lhs, rhs) {
    return(unlist(strsplit(paste0("[", lhs, ",", rhs,"]"), "")))
}

# Find the position of the 1st number to explode
FindExp <- function(input) {
    
    out = c(NA, NA)

    for (ii in 1:(length(input) - 4)) {

        catch = paste0(input[ii:(ii + 4)], collapse = "")

        check <- grepl("\\[(\\d{1,2},\\d{1,2})\\]", catch)

        if (check) {

            test = input[1:ii]

            lhb = length(test[test == "["])
            rhb = length(test[test == "]"])

            if (lhb - rhb >= 5) {
                out = c(ii, ii + 4)
                break
            }
        }
    }

    return(out)
}

# Perform the explode
Explo = function(input, pos) {

    lhs_num = input[pos[1] + 1]

    rhs_num = input[pos[2] - 1]

    lhs = input[1:(pos[1] - 1)]

    rhs = input[(pos[2] + 1):length(input)]

    lhs_loc = length(lhs) - stringr::str_locate(paste0(rev(lhs), collapse = ""), "\\d{1,2}")[1] + 1

    rhs_loc = stringr::str_locate(paste0(rhs, collapse = ""), "\\d{1,2}")[1]

    if (!is.na(lhs_loc)) {
        lhs[lhs_loc] = as.numeric(lhs[lhs_loc]) + as.numeric(lhs_num)
    }

    if (!is.na(rhs_loc)) {
        rhs[rhs_loc] = as.numeric(rhs[rhs_loc]) + as.numeric(rhs_num)
    }

    out = c(lhs, "0", rhs)

}

# Find position of first number to split
FindSpli = function(input) {

    out = stringr::str_locate(paste0(input, collapse = ""), "\\d{2}")[1]

    return(out)
}

# Perform the split
Splito <- function(input, pos) {
    rep_wi <- as.numeric(input[pos])

    rep_wi <- c("[", floor(rep_wi / 2), ",", ceiling(rep_wi / 2), "]")

    out <- c(input[1:(pos - 1)], rep_wi, input[(pos + 1):length(input)])

    return(out)
}

# Wrapper to perform whole operation of reduction
ReduceNums <- function(input) {
    outer_run <- TRUE

    while (outer_run) {
        inner_run <- TRUE
        exp_pos <- FindExp(input)
        if (is.na(exp_pos[1])) inner_run <- FALSE

        while (inner_run) {
            input <- Explo(input, exp_pos)
            exp_pos <- FindExp(input)
            if (is.na(exp_pos[1])) inner_run <- FALSE
        }

        spli_pos <- FindSpli(input)

        if (!is.na(FindSpli(input)[1])) input <- Splito(input, spli_pos)

        if (is.na(FindExp(input)[1]) & is.na(FindSpli(input)[1])) outer_run <- FALSE
    }

    return(input)
}

# Get the magnitude of a reduced number
Magneto <- function(input) {
    
    input = paste0(input, collapse = "")

    input = gsub("\\[", "(", input)
    input = gsub("\\]", ")", input)
    input = gsub(",", "*3+2*", input)

    return(eval(parse(text = input)))
}

# Read puzzle input
source <- readLines("day_18/day_18.txt", warn = FALSE)

run_sum = source[1]

for (jj in 2:length(source)) {

    run_sum = ReduceNums(Combine(paste0(run_sum, collapse = ""), source[jj]))

}

# Part 1 answer
Magneto(run_sum)

# Get all possible sums as a data/frame
biggest = expand.grid(a = as.character(source), b = as.character(source))

biggest = biggest[biggest$a != biggest$b,]

catch_mag = vector(mode = "numeric", length = nrow(biggest))

for (xx in 1:nrow(biggest)) {
    catch_mag[xx] = Magneto(ReduceNums(Combine(biggest$a[xx], biggest$b[xx])))
    print(xx)
}

# Part 2 answer
max(catch_mag)
