#include <opencv2/opencv.hpp>
#include <iostream>
#include <fstream>

using namespace cv;
using namespace std;

// 相机内参矩阵和畸变系数
double fx = (1.0e+03) * 0.4496;
double fy = (1.0e+03) * 0.4506;
double cx = (1.0e+03) * 0.7359;
double cy = (1.0e+03) * 1.1123;
double k1 = (1.0e-03) * 0.1352;
double k2 = (1.0e-03) * 0.0103;
double k3 = 0;
double p1 = 0;
double p2 = 0;

int main()
{
    // 读取输入棋盘格图像
    Mat img = imread("checkerboard.bmp");

    // 将图像转换为灰度图像
    Mat gray;
    cvtColor(img, gray, COLOR_BGR2GRAY);

    // 定义棋盘格的内角点尺寸
    Size pattern_size(7, 7);

    // 使用findChessboardCorners函数查找棋盘格角点
    bool found;
    vector<Point2f> corners;
    found = findChessboardCorners(gray, pattern_size, corners);

    if (found)
    {
        // 使用cornerSubPix函数进行亚像素级角点查找
        TermCriteria criteria(TermCriteria::EPS + TermCriteria::MAX_ITER, 30, 0.001);
        cornerSubPix(gray, corners, Size(11, 11), Size(-1, -1), criteria);

        // 定义棋盘格的三维坐标
        vector<Point3f> objp;
        for (int i = 0; i < pattern_size.height; i++)
        {
            for (int j = 0; j < pattern_size.width; j++)
            {
                objp.push_back(Point3f(j, i, 0));
            }
        }
        // 定义相机内参矩阵和畸变系数
        Mat camera_matrix = (Mat_<double>(3, 3) << fx, 0, cx,
            0, fy, cy,
            0, 0, 1);
        Mat dist_coeffs = (Mat_<double>(1, 5) << k1, k2, p1, p2, k3);

        // 使用solvePNP函数计算相机位姿的旋转向量和平移向量
        Mat rvecs, tvecs;
        solvePnP(objp, corners, camera_matrix, dist_coeffs, rvecs, tvecs);

        // 使用Rodrigues函数将旋转向量转换为旋转矩阵
        Mat rotation_matrix;
        Rodrigues(rvecs, rotation_matrix);

        // 将旋转矩阵和平移向量合并为变换矩阵
        Mat extrinsic_matrix(3, 4, CV_64F);
        hconcat(rotation_matrix, tvecs, extrinsic_matrix);

        cout << "相机外参矩阵：" << endl;
        cout << extrinsic_matrix << endl;

        // 通过三组对应点取得变换矩阵（图像坐标系——工具坐标系）
        double x1 = 172.0828, y1 = 88;
        double x2 = 160, y2 = 36;
        double x3 = 226, y3 = 82;
        double u1 = 0, v1 = 0;
        double u2 = 0, v2 = 74;
        double u3 = 74, v3 = 0;

        cv::Point2f srcPoints[3] = {
            cv::Point2f(x1, y1),
            cv::Point2f(x2, y2),
            cv::Point2f(x3, y3)
            };
        cv::Point2f dstPoints[3] = {
            cv::Point2f(u1, v1),
            cv::Point2f(u2, v2),
            cv::Point2f(u3, v3)
            };
        cv::Mat affineMatrix = cv::getAffineTransform(srcPoints, dstPoints);
        cout << "Affine Transformation Matrix:\n";
        cout << affineMatrix << std::endl;
        imshow("chessboard", img);
        waitKey(0);

        //相机内参矩阵
        Mat camera_matrix_1 = (Mat_<double>(3, 4) << fx, 0, cx,0,   
            0, fy, cy, 0,
            0, 0, 1,0);
        
        //相机外参矩阵   
        Mat extrinsic_matrix_1 = (Mat_<double>(4, 4) << 0.999948, -0.01000, -0.0017943,-0.0222998,     
            0.01000, 0.9999486, 0.001608,-4.442938,
            0.0017781, -0.001626, 0.999999,2.230281,
            0,0,0,1);
        double rate = 0.4;

        // 工具坐标系和世界坐标系的变换矩阵
        Mat affineMatrix_1 = (Mat_<double>(4, 3) << 0.1336 * rate, -0.0308 * rate, -20.2677 * rate,      
            -0.0154 * rate, -0.1387 * rate, 14.8616 * rate,
            0, 0, 0,
            0, 0, 1);

        // 计算像素坐标系和机械臂坐标系之间的变换矩阵
        Mat transformed_matrix;
        transformed_matrix = camera_matrix_1 * extrinsic_matrix_1 * affineMatrix_1;

        // 读取字样图像
        Mat image = imread("word.bmp", 0);
        if (image.empty()) {
            cerr << "Failed to read image." << endl;
            return -1;
        }

        // 对图像旋转180度
        Mat FlippedImage_1;
        flip(image, FlippedImage_1, 0);         //竖直翻转
        Mat FlippedImage_2;
        flip(FlippedImage_1, FlippedImage_2, 1);//水平翻转

        // 二值化处理
        Mat binary;
        threshold(FlippedImage_2, binary, 30, 255, THRESH_BINARY_INV);
        dilate(binary, image1, Mat(), Point(-1, -1), 3);
        erode(binary, image1, Mat(), Point(-1, -1), 11);
        imshow("2", binary);

        // 轮廓检测
        vector<vector<Point>> contours;
        findContours(binary, contours, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE, Point(0, 0));

        // 绘制轮廓
        Mat result;
        cvtColor(binary, result, COLOR_GRAY2BGR);
        drawContours(result, contours, -1, Scalar(0, 0, 255), 2);

        // 将轮廓中的点坐标进行变换
        vector<Point2f> transformedPoints;
        for (size_t i = 0; i < contours.size(); i++)
        {
            for (size_t j = 0; j < contours[i].size(); j++)
            {
                Point2f p = contours[i][j];
                Mat pointMat = (Mat_<double>(3, 1) << p.x, p.y, 1);
                Mat transformedPointMat = transformed_matrix.inv() * pointMat;
                Point2f transformedPoint(transformedPointMat.at<double>(0, 0), transformedPointMat.at<double>(1, 0));
                transformedPoints.push_back(transformedPoint);
            }
        }

        // 打开文件
        ofstream outputFile("contour_points.txt");
        if (!outputFile.is_open()) {
            cerr << "Failed to open output file." << endl;
            return -1;
        }

        // 将变换后的点坐标写入txt文件
        for (size_t i = 0; i < transformedPoints.size(); i++)
        {
            outputFile << transformedPoints[i].x << " " << transformedPoints[i].y << endl;
        }

        // 关闭文件
        outputFile.close();

        // 显示图像
        imshow("Image", result);
        waitKey(0);
    }
    else
    {
        cout << "未找到棋盘格角点" << endl;
    }
}
