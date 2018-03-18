#include  "myFace.h"

void getMyFace(){
	string output_dir = "C:/Users/lovebear96/Desktop/";
	int size = 64;
	double alpha = 1;
	int bias = 0;
	int index = 1, key;
	Mat img, gray_img, face;
	int f_x, f_y, f_w, f_h;
	CascadeClassifier haar;
	vector<Rect> faces;
	haar.load("haarcascade_frontalface_alt.xml");

	VideoCapture camera(0);
	if (!camera.isOpened())
		cout << "Failed to open!" << endl;

	while (true){
		if (index <= 2){
			cout << "Being processed pic " << index << endl;
			camera >> img;
			cvtColor(img, gray_img, CV_BGR2GRAY);
			haar.detectMultiScale(gray_img, faces, 1.3, 5);

			for (auto d = faces.begin(); d != faces.end(); d++){
				f_x = (d->x > 0) ? d->x : 0;
				f_y = (d->y > 0) ? d->y : 0;
				f_w = (d->width > 0) ? d->width : 0;
				f_h = (d->height > 0) ? d->height : 0;

				srand((unsigned)time(NULL));
				face = img(Range(f_y, f_y + f_h), Range(f_x, f_x + f_w));
				face = relight(face, random(0.5, 1.5), random(-50, 50));
				resize(face, face, Size(size, size));
				imwrite(output_dir + int2str(index) + ".jpg", face);
				imshow("hjj", face);
				index++;
			}

			key = waitKey(30) & 0xff;
			if (key == 27)
				break;

		}
		else{
			cout << "Finished" << endl;
			break;
		}
	}
}

void getOtherFace(){
	string output_dir = "C:/Users/lovebear96/Desktop/";
	int size = 64;
	double alpha = 1;
	int bias = 0;
	int index = 1, key;
	Mat img, gray_img, face;
	int f_x, f_y, f_w, f_h;
	CascadeClassifier haar;
	vector<Rect> faces;
	haar.load("haarcascade_frontalface_alt.xml");

	while (true){
		if (index <= 2){
			cout << "Being processed pic " << index << endl;
			img = imread("E:\\smallfish\\img\\" + int2str(index) + ".jpg");
			cvtColor(img, gray_img, CV_BGR2GRAY);
			haar.detectMultiScale(gray_img, faces, 1.3, 5);

			for (auto d = faces.begin(); d != faces.end(); d++){
				f_x = (d->x > 0) ? d->x : 0;
				f_y = (d->y > 0) ? d->y : 0;
				f_w = (d->width > 0) ? d->width : 0;
				f_h = (d->height > 0) ? d->height : 0;

				srand((unsigned)time(NULL));
				face = img(Range(f_y, f_y + f_h), Range(f_x, f_x + f_w));
				face = relight(face, random(0.5, 1.5), random(-50, 50));
				resize(face, face, Size(size, size));
				imwrite(output_dir + int2str(index) + ".jpg", face);
				imshow("hjj", face);
				index++;
			}

			key = waitKey(30) & 0xff;
			if (key == 27)
				break;

		}
		else{
			cout << "Finished" << endl;
			break;
		}
	}
}

Mat relight(Mat img, double alpha, int bias){
	int w, h, tmp;
	w = img.cols;
	h = img.rows;

	for (int i = 0; i < w; i++){
		for (int j = 0; j < h; j++){
			for (int c = 0; c < 3; c++){
				tmp = int(img.at<Vec3b>(j, i)[c] * alpha + bias);
				if (tmp > 255)
					tmp = 255;
				else if (tmp < 0)
					tmp = 0;
				img.at<Vec3b>(j, i)[c] = tmp;
			}
		}
	}
	return img;
}

int random(int a, int b){
	return ((std::rand() % (b - a + 1)) + a);
}

double random(double a, double b){
	return ((std::rand() % int(a - b) + (double)(std::rand() % 1000) / 10000.0) + a);
}

string int2str(const int &int_temp)
{
	stringstream stream;
	stream << int_temp;
	string string_temp = stream.str();
	return string_temp;
}