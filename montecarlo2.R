library(RankAggreg)

set.seed(100)


aggr_priorities <- function(modules, weights){
  
  x <- matrix(modules, byrow=TRUE, ncol=4)
  y <- matrix(weights, byrow=TRUE, ncol=4)
  
  result <- RankAggreg(x, weights=y, k=4, method='CE', seed=123, verbose = FALSE)

  return(result)
  
}





