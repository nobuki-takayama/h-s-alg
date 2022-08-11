# Install the package hgm by 
#    install.packages("hgm")
# 
# Execute this program by source("hgm_on_R.r");
library("hgm")
print(hgm.pwishart(m=3,n=5,beta=c(1,2,3),q=3))
plot(hgm.pwishart(m=3,n=5,beta=c(1,2,3),q=10,autoplot=1))
