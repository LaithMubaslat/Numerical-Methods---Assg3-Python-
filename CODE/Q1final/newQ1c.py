def Fj(j,j1,j2,xr,x):
    F=1
    for r in range (j1,j2+1):
        if (r!=j):
            F=F*(x-xr[r])
            
        
    
    return F
            
def Lj(j,j1,j2,xr,x): 
    xj=xr[j]
    L=Fj(j,j1,j2,xr,x)/Fj(j,j1,j2,xr,xj)
    return L
        




def derLj(j,j1,j2,xr,x):
    xj=xr[j]
    derL=1/Fj(j,j1,j2,xr,xj)
    return derL
    





##############################################################################
##############################################################################

#main starts here 



#6degrees of freedom 
b=[0]*(n+1)

#for i in range (1,7):
    #a[i]=y[i]
    








start=0
end=22650
reductionfactor=10
numberofvaluestobemeasure=int((end-start)/reductionfactor)

V1int=[0]*(numberofvaluestobemeasure+1)
V2int=[0]*(numberofvaluestobemeasure+1)
V3int=[0]*(numberofvaluestobemeasure+1)
V4int=[0]*(numberofvaluestobemeasure+1)
V5int=[0]*(numberofvaluestobemeasure+1)
V6int=[0]*(numberofvaluestobemeasure+1)


U1int=[0]*(numberofvaluestobemeasure+1)
U2int=[0]*(numberofvaluestobemeasure+1)
U3int=[0]*(numberofvaluestobemeasure+1)
U4int=[0]*(numberofvaluestobemeasure+1)
U5int=[0]*(numberofvaluestobemeasure+1)
U6int=[0]*(numberofvaluestobemeasure+1)


totalcurve=[0]*(numberofvaluestobemeasure+1)


end=int(end/reductionfactor)




x1=0
x2=540.6
x3=1062.8
x4=8687.4
x5=13924.3
x6= 22650.2


y1=0
y2=1.3
y3=1.4
y4=1.7
y5=1.8
y6= 1.9




n=6

y=[0,y1,y2,y3,y4,y5,y6]




xr=[0,x1,x2,x3,x4,x5,x6] #in order to start from x1 at r=1




a=[0]*(n+1)

for i in range (1,7):
    a[i]=y[i]
    
    
    
#start should be zero 
for i in range (start,end):
    
    x= int(i*reductionfactor)
    
    
    
    
    if (x>=x1 and x<=x2):
        
        j1=1 
        
        j2=2 
        
    if (x>=x2 and x<=x3):
        
        j1=2
        j2=3
        
    if (x>=x3 and x<=x4):
        
        j1=3
        j2=4
        
    if (x>=x4 and x<=x5):
        
        j1=4
        j2=5
        
    if (x>=x5 and x<=x6):
        
        j1=5
        j2=6 
        
        
    L=Lj(j1,j1,j2,xr,x)
    derL=derLj(j1,j2,j2,xr,x)
    xj=xr[j1]
    U1 = (1 - 2 * derL * (x-xj) )* L * L 
    
    V1 = (x-xj) * L * L 
    
    
    L=Lj(j2,j1,j2,xr,x)
    derL=derLj(j2,j1,j2,xr,x)
    xj=xr[j2]
    U2 = (1 - 2 * derL * (x-xj) )* L * L 
    
    V2 = (x-xj) * L * L 

    

    
       
    
    
    
    
    
    
    b=slope
    #try only Lag and see what happens 
    
    #ouput au +bv 
    
    totalcurve[i+1]=a[j1]*U1+a[j2]* U2
    totalcurve[i+1]=totalcurve[i+1]+ b[j1]*V1+b[j2]* V2
    
























