#Magician
import math 
from numpy import*
pi=math.pi

pos=dType.GetPose(api)
x_0 = pos[0]
y_0 = pos[1]
z_0 = pos[2]
r_0 = pos[3]

Original_P = 	[280.7064,25.3892,	12.00,-16.7]
Colour_test_P = 	[290,111.6600,	23.4300,-1.800]
Red_P = 			[225.8521,-141.6231, -41.6551,-55.3351]
Blue_P = 		[41.231,255.3595,-42.5674,78.83]
Green_P = 		[150.0845,226.0704,-38.7318,53.1380]
Yellow_P = 		[-50,244.3595,-38.5674,99.83]

object_n = [0,0,0,0]

def Get_object():
	return(dType.GetInfraredSensor(api, 2))

def Get_colour():
	return dType.GetColorSensor(api)

def action(P,object_n):
	if object_n<=5:
		dType.SetPTPCmd(api, 0, P[0],P[1], P[2]+24*(object_n-1), P[3], isQueued=1)
	else:
		dType.SetPTPCmd(api, 0, P[0]-50,P[1], P[2]+24*(object_n-6), P[3]-10, isQueued=1)

dType.SetInfraredSensor(api,1,2, 2)
dType.SetColorSensor(api, 1, 1, 1)
red_n = 0
green_n = 0
blue_n = 0
yellow_n = 0 
while 1:
	dType.SetEMotor(api, 0, 1, 5000,  isQueued=1)

	if Get_object()[0]==1:
		dType.SetEMotor(api, 0, 1, 0,  isQueued=1)
		action(Original_P,1)
		
		dType.SetEndEffectorSuctionCup(api, 1,  1, isQueued=1)
		
		dType.SetPTPJumpParams(api,90,90,1)

		queueedCmdIndex = dType.SetPTPCmd(api, 0, Colour_test_P[0],Colour_test_P[1], Colour_test_P[2], Colour_test_P[3], isQueued=1)
		executedCmdIndex=[0]
		while executedCmdIndex[0] < queueedCmdIndex[0]:
			executedCmdIndex = dType.GetQueuedCmdCurrentIndex(api)

		
		colour = Get_colour()
		dType.dSleep(500)

		if colour ==[1,0,0]:
			red_n += 1
			action(Red_P,red_n)
			print("Red_P")
		elif colour == [0,1,0]:
			green_n+=1
			action(Green_P,green_n)
			print("Green_P")
		elif colour == [0,0,1]:
			blue_n+=1
			action(Blue_P,blue_n)
			print("Blue_P")
		elif colour == [0,0,0]:
			yellow_n += 1
			action(Yellow_P,yellow_n)
			print("Yellow_P")
		dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)
		


