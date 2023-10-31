# To find the downstream depth of open channel
# Given Data
Q= float(input("Enter the value of Discharge:"))
T= int(input("Enter the value of top width:"))
g= float(input("Enter the value of acceleration due to Gravity:"))
y1= float(input("Enter the value of upstream depth:"))
Z= float(input("Enter the Value of hump:"))
#Dicharge per meter width
q=Q/T
print("The value of discharge per meter width is:", q)
#Area Calculation
A1= T*y1
print("The value of upstream area is:", A1)
# Calculation of Froude Number
Fr1 = ((Q*Q*T)/(g*A1* A1 *A1))**0.5
print("The value of Froude number is:", Fr1)
if Fr1>1:
  print("The flow is Super Critical Flow")
else:
  print("The flow is Sub Critical Flow")
#Upstream Energy
E1=(y1+(Q*Q)/(2 *g*A1 *A1))
print("The value of Energy at initial Section is:", E1)
#Downstream Energy
E2=E1-Z
print("The value of downstream Energy E2 is:", E2)
#Critical Depth
yc=(q*q/g)**0.3333
print("The Value of critical depth is:", yc)
Ec=1.5*yc
print("The value of critical Energy is:", Ec)
if Ec>E2:
 print("Chocking Conditlon")
else:
 print ("SAFE")
#Calculation of Zmax
Zmax=E1-Ec
print("The value of maxinmum hump is:", Zmax)




# To find the downstream depth of open channel
# Given Data
Q= float(input("Enter the value of Discharge:"))
T= int(input("Enter the value of top width:"))
g= float(input("Enter the value of acceleration due to Gravity:"))
y1= float(input("Enter the value of upstream depth:"))
Z= float(input("Enter the Value of hump:"))
#Dicharge per meter width
q=Q/T
print("The value of discharge per meter width is:", q)
#Area Calculation
A1= T*y1
print("The value of upstream area is:", A1)
# Calculation of Froude Number
Fr1 = ((Q*Q*T)/(g*A1* A1 *A1))**0.5
print("The value of Froude number is:", Fr1)
if Fr1>1:
  print("The flow is Super Critical Flow")
else:
  print("The flow is Sub Critical Flow")
#Upstream Energy
E1=(y1+(Q*Q)/(2 *g*A1 *A1))
print("The value of Energy at initial Section is:", E1)
#Downstream Energy
E2=E1-Z
print("The value of downstream Energy E2 is:", E2)
#Critical Depth
yc=(q*q/g)**0.3333
print("The Value of critical depth is:", yc)
Ec=1.5*yc
print("The value of critical Energy is:", Ec)
if Ec>E2:
 print("Chocking Conditlon")
else:
 print ("SAFE")
#Calculation of Zmax
Zmax=E1-Ec
print("The value of maxinmum hump is:", Zmax)





#To find the downstream depth of open channel
#Given Data
Q= int(input("Enter the value of Discharge:"))
B1 = float(input("Enter the value of width at upstream: "))
B2 = float(input("Enter the value of width at downstream: "))
g= float(input("Enter the value of acceleration due to Gravity:"))
yl= int(input("enter the value of upstream depth:"))
#Dicharge per meter width
q1=Q/B1
q2=Q/B2
print("The value of discharge per meter width is:'", q1)
print("The value of discharge per meter width is:", q2)
#Area Calculation
A1=B1*y1
print("The value of upstream area is:", A1)
#Calculation of Froude Number
Fr1=((Q*Q*B1)/(g*A1*A1*A1)) **0.5
print("The value of Froude number is:", Fr1)
if Fr1>1:
 print("The flow is Super Critical Flow")
else:
 print("The flow is Sub Critical Flow")
#Upstream Energy
E1=y1+((Q*Q)/(2*g*A1*A1))
print("The value of Energy at initial Section is:",E1)
#B2min: Any dition
B2min = (27*Q*Q/(8*g*E1*E1*E1))**0.5
print("The value of minimum width to be kept to avoid Chocking is:", B2min)
if B2min > B2:
 print("Chocking Condition")
else:
 print("SAFE")
#Critical Depth
yc=((Q*Q)/(B2*B2*g))**0.3333
print ("The Value of critical depth is: ", yc)
Ec=1.5*yc
print("The value of critical Energy is", Ec)








#Design of Efficient Channel Section
Q= int(input("Enter the value of Discharge:"))
n= float(input("Enter the value of Rugosity coefficient:"))
So= float(input("Enter the value of bed slope:"))
g= float(input("Enter the value of acceleration due to Gravity:"))
#Manning's Formula
#Q=(AR^2/3S^1/2)/n
yn=((Q*n*50*1.591)/(1.732))**(3/8)
print("The Value of yn is", yn)
#To encounter the effect of free board
yn1=1.1*yn
print("The Value of ynl is", yn1)
#Cross Sectional Area
A=1.732*yn*yn1
print("The cross sectional Area is:", A)
#Top Width
T=4*yn/1.732
print("The value of top Width is:", T)
#Bottom Width
B=2*yn/1.732
print("The value of Bottom Width is'", B)
Fr=((Q*Q*T)/(g*A*A*A))*0.5
print("The value of Froude number is:", Fr)
if Fr>1:
 print("The flow is Super Critical Flow")
else:
 print("The flow is Sub Critical Flow")