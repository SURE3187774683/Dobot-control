import math
dType.SetPTPCommonParams(api, 100, 100,0)

pose = dType.GetPose(api)
file = open('C:\\Users\\User\\Desktop\\拍照写字\\P1\\P1\\contour_points.txt','r') #获取机械臂x、y坐标文件
rate = 2

def move():
	# 将每行的x、y坐标送给x和y
	line = file.readline()
	data = line.split()
	if len(data) == 2:
		x = float(data[0])
		y = float(data[1])

		#通过旋转矩阵修正坐标系
		x_r = 0.9397*x-0.3420*y
		y_r = 0.3420*x+0.9397*y	

		print ("X:",x,"Y:",y)

		#防止程序速度超过机械臂移动速度
		queueedCmdIndex = dType.SetPTPCmd(api,2,x_r*rate+49.0669,y_r*rate+32.2098,-27.5,pose[3],1)
		executedCmdIndex = [0]
		while(executedCmdIndex[0] < queueedCmdIndex[0]):
			executedCmdIndex = dType.GetQueuedCmdCurrentIndex(api)

for i in range (1,5000,1):
	move()
