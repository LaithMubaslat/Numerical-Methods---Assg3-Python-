#new set of slopes 



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




# the slope is needed for each of these points 
slope=[0]*7


slope[2]=(1.4-1.2)/(1062.8-348.7)
slope[3]=(1.5-1.3)/(2318-540.6)
slope[4]=(1.8-1.6)/(13924-4781.9)
slope[5]=(1.9-1.7)/(22650.2-8687.4)


slope[2]=(y3-y1)/(x3-x1)
slope[3]=(y4-y2)/(x4-x2)
slope[4]=(y5-y3)/(x5-x3)
slope[5]=(y6-y4)/(x6-x4)


#computed using Q1 part A program
yinterpolatedbefore=-14.7
xinterpolatedbefore= -0.280482169122

#computed using Q1 part A program for the last 6 points 



slope[1]= (0.2-yinterpolatedbefore)/(14.7-xinterpolatedbefore)
slope[6]= (yinterpolatedafter-1.8)/(xinterpolatedafter-13924)


slope[1]=slope1
slope[6]=slope6