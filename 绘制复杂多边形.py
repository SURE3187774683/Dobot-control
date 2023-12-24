#绘制复杂多边形
import math
dType.SetPTPJointParams(api,200,200,200,200,200,200,200,200,0)
dType.SetPTPCoordinateParams(api,200,200,200,200,0)
dType.SetPTPJumpParams(api, 10, 200,0)
dType.SetPTPCommonParams(api, 100, 100,0)

moveX=0;moveY=0;moveZ=0

pos = dType.GetPose(api)
x = pos[0]
y = pos[1]
z = pos[2]
rHead = pos[3]

radius = 10			#半径（多边形和六边形共用）
num_points = 8		#六边形个数
liu_points = 6		#六边形边数

angle_1_increment = 2*math.pi/num_points
angle_2_increment = 2*math.pi/liu_points

points = []

for i in range(num_points+1):
	for i in range(num_points+1):
		angle_1 = i*angle_1_increment
		moveX = radius*math.cos(angle_1)
		moveY = radius*math.sin(angle_1)
		dType.SetPTPCmd(api, 2, x+moveX, y+moveY, z, rHead, 1)
		
		a = x
		b = y
		x = x+moveX
		y = y+moveY
		for i in range(liu_points+1):
			angle_2 = i*angle_2_increment
			moveX = radius*math.cos(angle_2)
			moveY = radius*math.sin(angle_2)
			dType.SetPTPCmd(api, 2, x+moveX, y+moveY, z, rHead, 1)
		dType.SetPTPCmd(api, 2, a, b, z, rHead, 1)
		x = a
		y = b
		


