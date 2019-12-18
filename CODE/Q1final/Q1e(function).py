#Q1E


# we are curve fitting the permiability 


#function 
X=[0]*17
Y=[0]*17
perm=[0]*17
X[1]=0
X[2]=14.7
X[3]=36.5
X[4]=71.7
X[5]=121.4
X[6]= 197.4
X[7]= 256.2
X[8]= 348.7
X[9]= 540.6
X[10]=1062.8
X[11]= 2318.0
X[12]= 4781.9
X[13]=8687.4
X[14]=13924.3
X[15]=22650.2




Y[1]=0
Y[2]=0.2
Y[3]=0.4
Y[4]=0.6
Y[5]=0.8
Y[6]= 1
Y[7]=1.1
Y[8]=1.2
Y[9]=1.3
Y[10]=1.4
Y[11]=1.5
Y[12]=1.6
Y[13]=1.7
Y[14]=1.8
Y[15]=1.9


X[16]=30000 # value to be found  from part c 
Y[16]=2






for i in range (2,17):
    perm[i]=Y[i]/X[i]   
X=Y
Y=perm



# X axis is B
# Y axis is perm 

#first order lagrange
#j1 and j2 are x1 and x2 for each interval
#j is which lag poly it is 

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


def function(Y,X,x):
    
    # we have 14 intervals > each interval has it's own linear function 
    interval=0
    
    for i in range (1,15):  #because the last interval is between i=14 and i+1=15
        if (x>=X[i] and x<=X[i+1]):
            interval = i
            break
        
    
    
    #FIRST L IS THAT OF i 
    
    #SECOND L IS THAT OF i+1
    xr=X
    
    j1=i
    j2=i+1
    
    
    j=j1
    L1=Lj(j,j1,j2,xr,x)
    
    
    j=j2
    L2=Lj(j,j1,j2,xr,x)
    
    
    
    
    
    f= Y[j1]*L1 + Y[j2]* L2
    
    return f
        
        
    

    
    

    
    
def derfunction(Y,X,x):
     # we have 14 intervals > each interval has it's own linear function 
    interval=0
    
    for i in range (1,15):  #because the last interval is between i=14 and i+1=15
        if (x>=X[i] and x<=X[i+1]):
            interval = i
            break
        
    
    
    #FIRST L IS THAT OF i 
    
    #SECOND L IS THAT OF i+1
    xr=X
    
    j1=i
    j2=i+1
    
    
    j=i
    xj=xr[j]
    Fj1=Fj(j,j1,j2,xr,xj)
    
    
    j=i+1
    xj=xr[j]
    Fj2=Fj(j,j1,j2,xr,xj)
    
    
    
    derf= Y[j1]/Fj1 + Y[j2]/Fj2
    
    return derf
        


output=[0]*200
deto=[0]*200
for i in range (200):
    x=i/100
    output[i]=function (Y,X,x)
    deto[i]=derfunction(Y,X,x)
    





function (Y,X,1)

 