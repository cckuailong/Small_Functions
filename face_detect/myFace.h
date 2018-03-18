#pragma once
#include "head.h"

using namespace cv;
using namespace std;

Mat relight(Mat img, double alpha = 1, int bias = 0);
int random(int a, int b);
double random(double a, double b);
string int2str(const int &int_temp);
void getMyFace();
void getOtherFace();