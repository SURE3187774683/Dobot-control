import math 
from numpy import*
pi=math.pi
pos=dType.GetPose(api)

theta_1 = math.radians(pos[4])
theta_2 = math.radians(pos[5])
theta_3 = math.radians(pos[6]+90-pos[5])
theta_4 = math.radians(pos[6])
l1=135
l2=147
l3=59.7

T_0_1=mat([[math.cos(theta_1),0,-math.sin(theta_1),0],[math.sin(theta_1),0,math.cos(theta_1),0],[0,-1,0,0],[0,0,0,1]])
T_1_2=mat([[math.sin(theta_2),math.cos(theta_2),0,l1*math.sin(theta_2)],[-math.cos(theta_2),math.sin(theta_2),0,-l1*math.cos(theta_2)],[0,0,1,0],[0,0,0,1]])
T_2_3=mat([[math.cos(theta_3),-math.sin(theta_3),0,l2*math.cos(theta_3)],[math.sin(theta_3),math.cos(theta_3),0,l2*math.sin(theta_3)],[0,0,1,0],[0,0,0,1]])
T_3_4=mat([[math.cos(theta_4),0,math.sin(theta_4),l3*math.cos(theta_4)],[-math.sin(theta_4),0,math.cos(theta_4),-l3*math.sin(theta_4)],[0,-1,0,0],[0,0,0,1]])
B = T_0_1*T_1_2*T_2_3*T_3_4

x = pos[0]
y = pos[1]
z = pos[2] 

e = math.asin(y/math.sqrt(x**2+y**2))
if x >= 0:
   j1 = e
elif x < 0:
   j1 = pi-e
k = math.sqrt(x*x+y*y)-l3
p= k**2+z**2+l1**2-l2**2
q=2*l1*math.sqrt((math.sqrt(x**2+y**2)-l3)**2+z**2)
j2=90-math.degrees(math.atan(z/(math.sqrt(x**2+y**2)-l3)))-math.degrees(math.acos(p/q))
j3=math.asin((l1*math.cos(math.radians(j2))-z)/l2)

a1=mat([math.degrees(j1),j2,math.degrees(j3)])
print(a1)
