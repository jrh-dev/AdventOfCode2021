# Read and prep data
called <- readLines("day_4/day_4.txt")

boards <- called[-1]

called <- as.numeric(unlist(strsplit(called[[1]], ",")))

# Drop blank elements
boards <- boards[-c(seq(1, length(boards), 6))]

boards <- strsplit(boards, " ")

# Remove spaces introduced by single digit numbers
boards <- lapply(boards, function(x) {
    x <- x[x != ""]
    as.numeric(x)
})

# Put bingo boards into a list of data.frames
boards <- data.frame(do.call(rbind, boards))

boards <- split(boards, rep(1:(nrow(boards) / 5), each = 5))

# Functions to find first and last boards to win and return the sum
#  of uncalled numbers multiplied by the last number called
FirstWinner <- function(input_boards, input_called) {
    catch_break <- FALSE
    for (ii in seq_along(input_called)) {
        if (catch_break) {
            break
        }
        input_boards <- lapply(input_boards, function(x) {
            x[x == input_called[ii]] <- NA

            for (jj in 1:5) {
                if (all(is.na(x[, jj])) | all(is.na(x[jj, ]))) {
                    print(sum(x, na.rm = TRUE) * input_called[ii])
                    catch_break <<- TRUE
                    break
                }
            }
            return(x)
        })
    }
}

LastWinner <- function(input_boards, input_called) {
    catch_break <- FALSE
    for (ii in seq_along(input_called)) {
        if (catch_break) {
            break
        }

        input_boards <- input_boards[lengths(input_boards) != 0]

        input_boards <- lapply(input_boards, function(x) {
            x[x == input_called[ii]] <- NA

            for (jj in 1:5) {
                if (
                    (all(is.na(x[, jj])) | all(is.na(x[jj, ]))) &
                        length(input_boards) == 1
                ) {
                    print(sum(x, na.rm = TRUE) * input_called[ii])
                    catch_break <<- TRUE
                    break
                }
                if (
                    (all(is.na(x[, jj])) | all(is.na(x[jj, ]))) &
                        length(input_boards) != 1
                ) {
                    x <- NULL
                }
            }
            return(x)
        })
    }
}

FirstWinner(boards, called)
LastWinner(boards, called)
