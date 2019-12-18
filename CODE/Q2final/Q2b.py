#Q2B

from math import exp

def Jacobian (v1,v2):
    KTq=25 / 1000 
    qKT= 1/KTq
    
    E=200/1000
    R= 512
    Isa= 0.8 * ( (10) ** (-6)    ) 
    Isb=1.1 * ( (10) ** (-6)    ) 
    
    
    
    df1v1=1 + R * Isa * qKT * exp (    (v1-v2) * qKT )
    df1v2= - R * Isa * qKT * exp (    (v1-v2) * qKT )
    df2v1=1
    df2v2= R * Isb * qKT * exp (    (v2) * qKT )
    
    
    Jvec=[df1v1, df1v2,df2v1,df2v2]
    
    J=Matrix(Jvec,2,2)
    
    
    return J 



def EuclidianNorm(V):
    for i in range (2):
        norm=V[0]*V[0]+V[1]*V[1]
        norm=sqrt(norm)


    return norm
    


#main newton raphson 
numberofmeasuments=1000
initialv1=0
initialv2=0





counter=0
v=[0]*numberofmeasuments





KTq=25 / 1000 
qKT= 1/KTq   
E=200/1000
R= 512
Isa= 0.8 * ( (10) ** (-6)    ) 
Isb=1.1 * ( (10) ** (-6)    ) 
    




v1=initialv1
v2=initialv2


#saved voltage values 
Vector=[0]* (2* numberofmeasuments)




IterationsVoltageOutput=Matrix(Vector,numberofmeasuments,2)
IterationsFOutput=Matrix(Vector,numberofmeasuments,2)

for i in range (numberofmeasuments):
    
    
    
    
    
    counter=counter+ 1
    
    J= Jacobian(v1,v2)
    
    A= J[0][0]
    B= J[0][1]
    C= J[1][0]
    D= J[1][1]
    
    
    
    
    f1old= v1-E+R*Isa* ( exp ( (v1-v2) * qKT        )    - 1             )
    f2old= v1-E+R*Isb* ( exp ( (v2) * qKT        )    - 1             )
    
    
    foldvector= [f1old,f2old]
    fold= Matrix(foldvector, 2, 1)
    
    vvectorold=[v1,v2]
    vold= Matrix(vvectorold,2,1)
    
    
    
    R1=Multiplication (J,vold)
    Rightside=[0]*2
    Rightside=Matrix(Rightside,2,1)
    
    for j in range (2):
        Rightside[j][0]= - fold[j][0]+R1[j][0]
   
    
    X=Rightside[0][0]
    Y=Rightside[1][0]
    
    
    v2new= (Y- C*X/A) / (D-C*B/A)
    
    
    v1new= (X-B*v2new)/A 
    
    
    
    
    
    
    IterationsVoltageOutput[i][0]=v1
    IterationsVoltageOutput[i][1]=v2
    
    
    IterationsFOutput[i][0]=f1old
    IterationsFOutput[i][1]=f2old
    
    
    Vitekminus1=IterationsVoltageOutput[i-1]
    Vitek=[v1new,v2new]
    
    if (EuclidianNorm(Vitekminus1 )==EuclidianNorm(Vitek ) ):
        break
    
    
    
    
    
    # add stop check here 
    
    
    
    v1=v1new
    v2=v2new 
    
    
    
    xfinal=IterationsVoltageOutput[8]
    
    
    
    
    
    
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 


    

xxfinalminus1=[0]*2
xxfinalminus2=[0]*2
xxfinalminus3=[0]*2
xxfinalminus4=[0]*2
xxfinalminus5=[0]*2


for i in range (2):
    xxfinalminus1[i]=xfinal[i]-IterationsVoltageOutput[1][i]
    xxfinalminus2[i]=xfinal[i]-IterationsVoltageOutput[2][i]
    xxfinalminus3[i]=xfinal[i]-IterationsVoltageOutput[3][i]
    xxfinalminus4[i]=xfinal[i]-IterationsVoltageOutput[4][i]
    xxfinalminus5[i]=xfinal[i]-IterationsVoltageOutput[5][i]
    



finalminus1norm=EuclidianNorm(xxfinalminus1)
finalminus2norm=EuclidianNorm(xxfinalminus2)
finalminus3norm=EuclidianNorm(xxfinalminus3)
finalminus4norm=EuclidianNorm(xxfinalminus4)
finalminus5norm=EuclidianNorm(xxfinalminus5)


term1=finalminus2norm/(finalminus1norm*finalminus1norm)
term2=finalminus3norm/(finalminus2norm*finalminus2norm)
term3=finalminus4norm/(finalminus3norm*finalminus3norm)
term4=finalminus5norm/(finalminus4norm*finalminus4norm)


#term2 term3 term4 

#as can be clearly seen as x is close enough to x norm[1]/norm[2]^2 = C 





