library(tibble)

get_tibble <- function() {
  tibble(x = 1:5, y = 1, z = x ^ 2 + y)
}
