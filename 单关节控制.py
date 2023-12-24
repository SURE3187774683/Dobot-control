# 单关节控制到指定点
import math 
from numpy import*
pi=math.pi

pos=dType.GetPose(api)
x_0 = pos[0]
y_0 = pos[1]
z_0 = pos[2]
r_0 = pos[3]

time = 10

def action(x,y,z):
   pos=dType.GetPose(api)
   theta_1=pos[4]
   theta_2=pos[5] 
   theta_3=pos[6]
   k = math.sqrt(x**2+y**2)
   e = math.asin(y/k)
   if x >= 0:
      j1 = e
   elif x < 0:
      j1 = pi-e
   p=(math.sqrt(x*x+y*y)-l3)**2+z**2+l1**2-l2**2
   q=2*l1*math.sqrt((math.sqrt(x**2+y**2)-l3)**2+z**2)
   j2=90-math.degrees(math.atan(z/(math.sqrt(x**2+y**2)-l3)))-math.degrees(math.acos(p/q))
   j3=math.asin((l1*math.cos(math.radians(j2))-z)/l2)

   dType.SetPTPCmd(api, 4, math.degrees(j1),theta_2,theta_3, r, 1)
   dType.SetPTPCmd(api, 4,theta_1, j2, theta_3, r, 1)
   dType.SetPTPCmd(api, 4, theta_1, theta_2,math.degrees(j3), r, 1)
   dType.SetWAITCmd(api,500, 1)

for i in range(time):
   dType.SetEndEffectorGripper(api,1 , 1, 1) 
   action(10,20,30)  
   action(10,30,50)
   dType.SetEndEffectorGripper(api,0,  0, 1)
   action(10,20,30) 
   action(x_0,y_0,z_0)
