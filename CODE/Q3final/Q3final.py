#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### ####

#QUESTION 3       

def integrate(x0,xN,N,function):
    
    h=(xN-x0)/N
    # since it's the one point scheme 
    wi=2 
    zetai=0
    
    
    
    
    
        
    
        
  
    sum=0
    
    for i in range (N):
        sum = sum + wi*function(zetai+h*(i+1/2) ) *h/2
        
    
    
    return sum


#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### ####      
#PARTA

from math import sin 
from math import log 
from math import cos


#integration limits 
x0=0 
xN=1


function=sin
#Reference value
exactvaluesSINintegral = -cos(xN)- (-cos(x0))

log10N=[0]*21
for i in range (1,21):
    log10N[i]= log(i,10)
    


log10NB=[0]*21
for i in range (1,21):
    x=i*10
    log10NB[i]= log(x,10)

abserrorPARTA = [0]*21 
log10abserrorPARTA = [0]*21 

for i in range (1,21):
    N=i 
    
    abserrorPARTA[i]=exactvaluesSINintegral-integrate(x0,xN,N,function)
    
    if (abserrorPARTA[i]<0):
        abserrorPARTA[i]=-abserrorPARTA[i]
        
    
        
    
    log10abserrorPARTA[i]= log (abserrorPARTA[i],10)
    



#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#PARTB
function=log
#reference
exactvaluesLnintegral = -1 


abserrorPARTB = [0]*21 
log10abserrorPARTB = [0]*21 

for i in range (1,21):
    N=i*10
    
    abserrorPARTB[i]=exactvaluesLnintegral-integrate(x0,xN,N,function)
    
    if (abserrorPARTB[i]<0):
        abserrorPARTB[i]=-abserrorPARTB[i]
        
    
    log10abserrorPARTB[i]= log (abserrorPARTB[i],10)



#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### ####  
#PARTC
def integrateLNABS02SIN(x0,xN,N):
    
    h=(xN-x0)/N
    # since it's the one point scheme 
    wi=2 
    zetai=0
    
    
    
    
    
        
    
        
  
    sum=0
    
    for i in range (N):
        sum = sum + wi*            log(0.2*(abs(sin(zetai+h*(i+1/2)))))        *h/2
        
    
    
    return sum

    
    
exactvaluesLnABSintegral = -2.66616

abserrorPARTC = [0]*21 
log10abserrorPARTC = [0]*21 

for i in range (1,21):
    N=i*10
    
    abserrorPARTC[i]=exactvaluesLnABSintegral-integrateLNABS02SIN(x0,xN,N)
    
    if (abserrorPARTC[i]<0):
        abserrorPARTC[i]=-abserrorPARTC[i]
        
    
    log10abserrorPARTC[i]= log (abserrorPARTC[i],10)


#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### ####  



      
#the following programs serve to evaluate the effect of decreasing h at different parts of the integration interval
#the integration is divided into 10 intervals 
#the smallest interval is chosen to be each of them seperatly (with numerous orders of magnitude difference determined by the ratio of the variables normal and less where less+9*normal = (xN-x0))
#the values of the absolute error for each is then compared against the interval which provides the largest abserror 
# a pattern can be clearly seen for both integral where the closer the smallest interval is to the right side of curve the lower the error is in the case of part a while the higher it is for part b
# due to the consistancy of the results for different normal/less ratios and the obvious and persistant pattern where the error decreases/increases 
# it can be concluded that the higher accuracy is consistent with choosing smaller h values associated with lower abs error values 
        
        
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
        abserrorln[j]=-abserrorln[j]
      
  
largest=0
for i in range (N):
    if (abserrorln[i]<0):
        abserrorln[i]=-abserrorln[j]
        
    if (abserrorln[i]>largest):
        largest=abserrorln[i]
        
    
for i in range (N):
    abserrorln[i]=(largest-abserrorln[i])*100000000

    
#largest error is when the smallest interval is near 1 which means that the smaller the intervals are near 1 the 
#worst the integration accuracy is 


#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#final integration scheme (PARTD-PARTA)


N10abserrorSIN=abserrorPARTA[10]
N10abserrorLN=abserrorPARTB[1]







function=sin
 



N=10
hequalspacing=(xN-x0)/N

normalizingfactor= 0
    
h=[0]*N 
a=[1,1,1,0.9,0.8,0.75,0.7,0.7,0.65,0.64]

for i in range (N):
    normalizingfactor=normalizingfactor+a[i]


for j in range (1):
    
    for i in range(N):
        
        
        h[i]=(hequalspacing*a[i]/normalizingfactor)*10
        
    
    wi=2 
    zetai=0
    sum=0
    
    sumh=0
    for i in range (N):
        sumh=sumh+h[i]/2
        sum = sum + wi*function(zetai+sumh) *h[i]/2
        sumh=sumh+h[i]/2
    
    
    abserrorsinimproved=sum-exactvaluesSINintegral
    
    
    
largest=0
for i in range (1):
    if (abserrorsinimproved<0):
        abserrorsinimproved=-abserrorsinimproved
        
N10abserrorSIN
abserrorsinimproved    
    

#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#final integration scheme (PARTD-PARTB)








function=log
 



N=10
hequalspacing=(xN-x0)/N

normalizingfactor= 0
    
h=[0]*N 
a=[0.3,0.5,0.7,1,2,2,3,3,4,6]

for i in range (N):
    normalizingfactor=normalizingfactor+a[i]


for j in range (1):
    
    for i in range(N):
        
        
        h[i]=(hequalspacing*a[i]/normalizingfactor)*10
        
    
    wi=2 
    zetai=0
    sum=0
    
    sumh=0
    for i in range (N):
        sumh=sumh+h[i]/2
        sum = sum + wi*function(zetai+sumh) *h[i]/2
        sumh=sumh+h[i]/2
    
    
    abserrorlnimproved=sum-exactvaluesLnintegral
    
    
    

for i in range (1):
    if (abserrorlnimproved<0):
        abserrorlnimproved=-abserrorlnimproved
        
N10abserrorSIN
abserrorlnimproved    
    

#ln improves more by the distribution of h which can be attributed to it's integral being harder to evaluate 
#considering the curve going to infinity as x>0 which also agrees with how a better accuracy is obtained by 
#choosing a spacing scheme which focuses more on that portion of the curve. i.e. the nature  of the aformentioned 
#curve characteristic leaves room for improvement which this scheme exploits 
#comparing the abs error 
#sin gives an accuracy half way between 10 and 11 
#ln gives an accuracy better than 30 








