#码垛函数
import math
moveX=0;moveY=0;moveZ=0
pos = dType.GetPose(api)
x = pos[0]
y = pos[1]
z = pos[2]
rHead = pos[3]

cnt = 0

while(1):
	cnt = cnt+1
	if (cnt%2==1):
		dType.SetEndEffectorSuctionCup(api, 1 , 1 , 1)
		dType.SetPTPCmd(api,0, 195,-55,-66+23*math.floor((cnt+1)/2), rHead, 1)
		dType.SetEndEffectorSuctionCup (api, 1 , 0 ,1)
		dType.SetWAITCmd(api,500,1)
	else:
	dType.SetEndEffectorSuctionCup(api, 1 , 0 ,1)
	dType.SetPTPCmd(api,0,x, y z-24*math.floor ((cnt+1)/2), rHead,1)
	dType. SetWAITCmd(api, 500,1)
	if (cnt > 4):
	break

