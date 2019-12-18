#main 
from math import sin 
from math import log 
from math import cos




def integrate(x0,xN,N,function):
    
    h=(xN-x0)/N
    # since it's the one point scheme 
    wi=2 
    zetai=0
    
    
    
    
    
        
    
        
  
    sum=0
    
    for i in range (N):
        sum = sum + wi*function(zetai+h*(i+1/2) ) *h/2
        
    
    
    return sum




x0=0 
xN=1
exactvaluesSINintegral = -cos(xN)- (-cos(x0))
exactvaluesLnintegral = -1 



function=sin
N=10




        
        
        
#the following programs serve to evaluate the effect of decreasing h at different parts of the integration interval
#the integration is divided into 10 intervals 
#the smallest interval is chosen to be each of them seperatly (with numerous orders of magnitude difference determined by the ratio of the variables normal and less where less+9*normal = (xN-x0))
#the values of the absolute error for each is then compared against the interval which provides the largest abserror 
# a pattern can be clearly seen for both integral where the closer the smallest interval is to the right side of curve the lower the error is 
# due to the consistancy of the results for different normal/less ratios and the obvious and persistant pattern where the error decreases as we move the the right hand side 
# it can be concluded that the higher accuracy is consistent with choosing smaller h values close the right side of the curve  
        
        
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### ####      
#unequal spacing SIN


function=sin
 



N=10
hequalspacing=(xN-x0)/N
normal=2
less=0.5

normalizingfactor= normal*9+less 
    
h=[0]*N 
a=[normal]*N
abserrorsin=[0]*N

for j in range (N):
    a[j]=less
    for i in range(N):
        
        
        h[i]=(hequalspacing*a[i]/normalizingfactor)*10
        
    a[j]=normal
    wi=2 
    zetai=0
    sum=0
    
    sumh=0
    for i in range (N):
        sumh=sumh+h[i]/2
        sum = sum + wi*function(zetai+sumh) *h[i]/2
        sumh=sumh+h[i]/2
    
    
    abserrorsin[j]=sum-exactvaluesSINintegral
    
    
    
largest=0
for i in range (N):
    if (abserrorsin[i]<0):
        abserrorsin[i]=-abserrorsin[j]
        
    if (abserrorsin[i]>largest):
        largest=abserrorsin[i]
        
    
for i in range (N):
    abserrorsin[i]=(largest-abserrorsin[i])*100000000
    

#largest error is when the smallest interval is near zero which means that the smaller the intervals are near 1 the 
#better the integration accuracy is 
    
        

   
    
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 

    
#unequal spacing ln   
    
    
function=log
 



N=10
hequalspacing=(xN-x0)/N
normal=2
less=0.001

normalizingfactor= normal*9+less 
    
h=[0]*N 
a=[normal]*N
abserrorln=[0]*N

for j in range (N):
    a[j]=less
    for i in range(N):
        
        
        h[i]=(hequalspacing*a[i]/normalizingfactor)*10
        
    a[j]=normal
    wi=2 
    zetai=0
    sum=0
    sumh=0
    
    for i in range (N):
        sumh=sumh+h[i]/2
        sum = sum + wi*function(zetai+(i+1)*h[i]/2) *h[i]/2
        sumh=sumh+h[i]/2
    
    
    abserrorln[j]=sum-exactvaluesLnintegral
    

for i in range (N):
    if (abserrorln[j]<0):
        abserrorln[j]=-abserrorsin[j]
      
  
largest=0
for i in range (N):
    if (abserrorln[i]<0):
        abserrorln[i]=-abserrorln[j]
        
    if (abserrorln[i]>largest):
        largest=abserrorln[i]
        
    
for i in range (N):
    abserrorln[i]=(largest-abserrorln[i])*100000000

    
#largest error is when the smallest interval is near zero which means that the smaller the intervals are near 1 the 
#better the integration accuracy is 
    
    
    
        