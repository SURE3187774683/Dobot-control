# Dobot桌面机械臂
## Frame
#### python
#### MATLAB
#### Dobot机器人本体、绘图笔夹持器、吸盘工具
## Main work
#### 1.平面绘图及码垛
##### 编写如下函数：
①绘制直线函数
功能：从当前位置开始绘制指定长度的直线，直线方向与机器人x轴正方向夹角为指定角度（逆时针旋转为正）
输入参数：直线长度、直线与x轴正方向夹角
②绘制圆弧函数
功能：以当前点为起点，绘制以指定点为圆心、圆弧角度为指定值（逆时针为正）的圆弧
输入参数：圆心的x坐标和y坐标、圆弧角度
③绘制圆形函数
功能：以当前点为起点，绘制以指定点为圆心的圆形
输入参数：圆心的x坐标和y坐标
##### 末端执行器使用吸盘，将叠在一起的小方块从桌面上的位置A越过中间的障碍物搬运到位置B。
（1）硬币最初摆放时方向一致，“1元”文字正立，要求搬运完成后文字变为倒立。
（2）使用Python脚本完成控制，不允许使用示教功能
（3）使用默认的最大速度和最大加速度设定值，记录完成搬运所用的时间、AB两点之间的平面距离、障碍物的高度。


#### 2.正逆解计算验证及单关节控制
##### 推导出Dobot Magician机械臂的逆解计算公式，并采用Python编写脚本实现以下功能：
（1）通过dType.GetPose(api)函数读取Dobot Magician的位姿信息，并利用print()函数打印位姿信息；
（2）以第（1）步中读取到的笛卡尔坐标为输入，计算各关节变量的值，并利用print()函数打印输出，比较计算出的关节变量和GetPose函数读取到的关节变量；
（3）改变Dobot Magician的末端位姿，使末端分别位于笛卡尔坐标系的8个象限中，重复上述过程，验证推导的逆解计算公式的正确性。
##### 编写Python脚本，通过单关节控制实现物品搬运，具体功能如下：
（1）以当前位置为起点，通过GetPose函数获取当前位置；
（2）自己设定一个终点位置和若干个中间点，以这些点的笛卡尔坐标为逆解计算的输入，计算出其对应的关节变量；
（3）利用dType.SetCPCmd(api, cpMode, x, y, z, velocity, isQueued=0)函数或者dType.SetPTPCmd(api, ptpMode, x, y, z, rHead, isQueued=0)函数，在关节空间中，每次修改一个关节变量，以三次单关节运动的方式完成到下一个目标点的移动。
（4）重复（3）完成把物品从起点搬移到终点。

#### 3.流水线码垛
##### 通过红外线识别货物是否等待处理，通过颜色传感器分辨货物类别，通过机械臂吸盘将对应颜色的货物放到对应的仓库
#### 4.视觉拍照写字
##### 使用相机拍摄Dobot机器人工作空间内白纸上书写的汉字，编写机器视觉程序提取汉字轮廓，编写机器人程序控制机器人沿着汉字轮廓描边书写空心汉字。
重点：拍照图片的调用、程序的编写
难点：相机坐标系到机器人坐标系的转换和图片特征提取方法

