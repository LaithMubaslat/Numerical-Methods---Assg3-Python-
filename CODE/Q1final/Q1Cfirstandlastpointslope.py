#Q1C first and last point slope 
def Fj(j,xr,x):
    F=1
    for r in range (1,3):
        if (r!=j):
            F=F*(x-xr[r])
            
        
    
    return F
            
def Lj(j,xr,x): 
    xj=xr[j]
    L=Fj(j,xr,x)/Fj(j,xr,xj)
    return L
        


#point 1 

x1=0
y1=0

x2=14.7
y2=0.2






#define the function (1st order lagrange poly.)
x=-14.7
xr=[0,x1,x2]
L1=Lj(1,xr,x)
L2=Lj(2,xr,x)

y=y1*L1+y2*L2


xextrapolated1=x
yextrapolated1=y



slope1=(y2-yextrapolated1)/(x2-xextrapolated1)



#point 6 

x1=13924.3
y1=1.8

x2=22650.2
y2=1.9




x=23000
xr=[0,x1,x2]
L1=Lj(1,xr,x)
L2=Lj(2,xr,x)

y=y1*L1+y2*L2



xextrapolated2=x
yextrapolated2=y

slope6=(y1-yextrapolated2)/(x1-xextrapolated2)




####slope1 fixed 
#x2 y2 fixed 


x1=0
y1=0

x2=540.6
y2=1.3





#define the function (1st order lagrange poly.)
x=-14.7
xr=[0,x1,x2]
L1=Lj(1,xr,x)
L2=Lj(2,xr,x)

y=y1*L1+y2*L2


xextrapolated1=x
yextrapolated1=y



slope1=(y2-yextrapolated1)/(x2-xextrapolated1)









