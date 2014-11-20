#include <iostream>
using namespace std;

class Point {

		int city_num, x, y;
	public:
		Point(); 
		Point (int a, int b , int c); 
		void print(); 
		int distance(Point A, Point B, Point C);
		int point_location(Point A, Point B, Point C); 

};

Point::Point (){
	city_num = 0;
	x = 0;
	y = 0;
}

Point::Point (int city_in, int x_in, int y_in){
        city_num = city_in;
        x = x_in;
        y = y_in;
}

void Point::print(){
	cout << "City Number: " << city_num <<endl
	     << "X: " << x <<endl
	     << "Y: " << y <<endl; 

}

int Point::distance(Point A, Point B, Point C){
	int ABx = B.x - A.x;
	int ABy = B.y - A.y;
	int num = ABx * (A.y - C.y) - ABy * (A.x - C.x);
	if (num < 0)	
		num = -num;
	return num; 
}

int Point::point_location(Point A, Point B, Point P){
	int cp1 = (B.x - A.x)*(P.y-A.y) - (B.y-A.y)*(P.x-A.x);
	if(cp1>0)
		return 1;
	return -1;
}
