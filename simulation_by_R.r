# Execute this by source("simulation_by_R.r")
rpwishart<-function(lambda=3,sigma=diag(c(1/2,1/4,1/6)),
                    n=5,try=10000)
{ count<-0;r<-rWishart(try,df=n,Sigma=sigma);
  for (k in seq(1,try)) {
    ell1 <- max(eigen(r[,,k])$values);
    if (ell1 < lambda) count<-count+1; }
  return(count/try) }  
print(rpwishart())
