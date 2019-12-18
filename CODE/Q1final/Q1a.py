#####Q1A


xstartingpoint=0
xendpoint=200 #i.e 199 




x1=0
x2=14.7
x3=36.5
x4=71.7
x5=121.4
x6= 197.4


y1=0
y2=0.2
y3=0.4
y4=0.6
y5=0.8
y6= 1




n=6

y=[0,y1,y2,y3,y4,y5,y6]




xr=[0,x1,x2,x3,x4,x5,x6] #in order to start from x1 at r=1


numberofvaluestobemeasure=xendpoint-xstartingpoint
#used to hold the values we compute for L at an x=value
L1int=[0]*(numberofvaluestobemeasure+1)
L2int=[0]*(numberofvaluestobemeasure+1)
L3int=[0]*(numberofvaluestobemeasure+1)
L4int=[0]*(numberofvaluestobemeasure+1)
L5int=[0]*(numberofvaluestobemeasure+1)
L6int=[0]*(numberofvaluestobemeasure+1)


def Fj(j,xr,x):
    F=1
    for r in range (1,7):
        if (r!=j):
            F=F*(x-xr[r])
    
    return F
            
def Lj(j,xr,x): 
    xj=xr[j]
    L=Fj(j,xr,x)/Fj(j,xr,xj)
    return L
        
            


#n=6 > order 5 lag poly 


#j=1
#L1=Lj(j,xr,x)
#j=2
#L2=Lj(j,xr,x)
#j=3
#L3=Lj(j,xr,x)
#j=4
#L4=Lj(j,xr,x)
#j=5
#L5=Lj(j,xr,x)
#j=6
#L6=Lj(j,xr,x)





#main starts here 

totalcurve=[0]*(numberofvaluestobemeasure+1) 



a=[0]*(n+1)

for i in range (1,7):
    a[i]=y[i]


for i in range (xstartingpoint,xendpoint): 
    valuestobecomputedat=i
    x=valuestobecomputedat
    
    j=1
    L1int[i+1]=Lj(j,xr,x)
    
    
    j=2
    L2int[i+1]=Lj(j,xr,x)
    
    
    j=3
    L3int[i+1]=Lj(j,xr,x)
    
    
    j=4
    L4int[i+1]=Lj(j,xr,x)
    
    j=5
    L5int[i+1]=Lj(j,xr,x)
    
    
    j=6
    L6int[i+1]=Lj(j,xr,x)
    
    
    totalcurve[i+1]=a[1]*L1int[i+1]+a[2]* L2int[i+1]+a[3]*L3int[i+1]+a[4]*L4int[i+1]+a[5]*L5int[i+1]+a[6]*L6int[i+1]
    
    
    

#first output value starts at 1>total curve 


#

    
    









