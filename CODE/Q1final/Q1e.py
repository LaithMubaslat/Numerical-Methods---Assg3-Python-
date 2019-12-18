#constants
Lc= 30 * 10**(-2)
Lg= 0.5 * 10**(-2)
N= 800 
I= 10 
A= 1 * 10**(-4)
perm0=1.256637 * 10**(-6)
M= I * N 


Rg=Lg/(A*perm0) 

#reference for error
refflux=0
refB = refflux/A
refcoreperm=function(Y,X,refB)
#refRc=Lc/(A*refcoreperm)

#fref=(Rg + refRc) * refflux - M 
fref=-M




fluxold =0

countersteps=0


flux=[0]*100000

for i in range (100000): 
    
    countersteps=countersteps+1
    
    B=fluxold/A
    coreperm=function(Y,X,B)
    if (coreperm==0):
        coreperm=7
    Rc=Lc/(A*coreperm)
    
    if (fluxold==0):
        Rc=0
    
    derterm= Rg - fluxold*(Lc/ (A*A * coreperm*coreperm)) * derfunction(Y,X,B)
    #if we remove Rg it will converge in 7 steps 

    
    f= (Rg + Rc) * fluxold - M 
    
    
    derf= Rg + Rc + derterm    
    
    
    fluxnew = - (f/derf) + fluxold
    
    #compute f (fluxnew)
    
    B=fluxnew/A
    coreperm=function(Y,X,B)
    Rc=Lc/(A*coreperm)
    
    f= (Rg + Rc) * fluxnew - M 
    
    ref= f/fref
    
    if (ref < 0 ):
        ref=-ref
        
    
    if (ref < 10**(-6)):
        break 
    
    fluxold=fluxnew
    flux[i]=fluxnew
    
    
    
    
    
    
    
    
    