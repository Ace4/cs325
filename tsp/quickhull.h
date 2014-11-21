#include <iostream>
using namespace std;

class Point {

		int city_num, x, y;
	public:
		Point(); 
		~Point();
		Point (int a, int b , int c); 
		void print(); 
		int distance(Point A, Point B, Point C);
		int get_x(){return x;}; 
		int get_y(){return y;}; 
		int get_city_num() {return city_num;};
		bool operator==(Point B);
};

Point::Point (){
	city_num = 0;
	x = 0;
	y = 0;
}

Point::~Point (){
	city_num = 0;	
	x = 0;
	y = 0; 
}

Point::Point (int city_in, int x_in, int y_in){
        city_num = city_in;
        x = x_in;
        y = y_in;
}

bool Point::operator==(Point B){
	if(city_num == B.get_city_num() && x == B.get_x() && y == B.get_y())
		return true;
	return false; 

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
