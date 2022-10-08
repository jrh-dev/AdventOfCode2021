UsefulR::set_dir()

dat <- readLines("day_20.txt", warn = F)

split = match(0, nchar(dat))

algo = paste0(dat[1:(split - 1)], collapse = "")

algo = unlist(strsplit(algo, ""))

raw_img = dat[(split + 1):length(dat)]

raw_img = matrix(unlist(strsplit(paste0(raw_img, collapse = ""), split = "")), ncol = nchar(raw_img[1]), byrow = TRUE)


# function to expand into the void
ex_vo <- function(input, pad) return(rbind(pad, cbind(pad, input, pad), pad))


# function to apply enhancement
enhance_img <- function(input, enhance = 0, default, flip = FALSE) {
  
  tmp_img <- enh_img <- input
  iter = 0
  
  while (iter < enhance) {
    
    if (flip) if (iter %% 2 == 0) default = "." else default = "#"
    
    tmp_img <- enh_img <- ex_vo(enh_img, pad = default)
    
    len = length(tmp_img)
    x = nrow(tmp_img)
    
    for (ii in seq_len(len)) {
      
      a = ii - x - 1 ; a = ifelse(a < 1 | a > len, default, tmp_img[a])
      b = ii - 1     ; b = ifelse(b < 1 | b > len, default, tmp_img[b])
      c = ii + x - 1 ; c = ifelse(c < 1 | c > len, default, tmp_img[c])
      d = ii - x     ; d = ifelse(d < 1 | d > len, default, tmp_img[d])
      e = ii         ; e = ifelse(e < 1 | e > len, default, tmp_img[e])
      f = ii + x     ; f = ifelse(f < 1 | f > len, default, tmp_img[f])
      g = ii - x + 1 ; g = ifelse(g < 1 | g > len, default, tmp_img[g])
      h = ii + 1     ; h = ifelse(h < 1 | h > len, default, tmp_img[h])
      i = ii + x + 1 ; i = ifelse(i < 1 | i > len, default, tmp_img[i])
      
      parsed <- strtoi(gsub("#", "1", gsub("\\.", "0", gsub("NA", default, paste0(a,b,c,d,e,f,g,h,i)))), base = 2) + 1  
      
      enh_img[ii] = algo[parsed]
      
    }
    
    iter = iter + 1
  }
  return(enh_img)
}


# Part 1 answer
table(enhance_img(input = raw_img, enhance = 2, default = "#", flip = TRUE))

# Part 2 answer
table(enhance_img(input = raw_img, enhance = 50, default = "#", flip = TRUE))
