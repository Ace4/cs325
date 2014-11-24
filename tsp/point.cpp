#include "point.h"
Point::Point (){
	city = 0;
	pts = Vec2(0,0);
}


Point::Point (int city_in, int x_in, int y_in){
        city = city_in;
        pts = Vec2 (x_in, y_in);
}

bool Point::operator==(Point B){
	if(city == B.city_num() && pts == B.point())
		return true;
	return false; 

}

void Point::print(){
	cout <<"City Number: " << city <<endl << "X: " << pts.x() <<endl << "Y: " << pts.y() <<endl; 

}

