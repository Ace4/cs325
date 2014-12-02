#include "point.h"
Point::Point (){
	city = -1;
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

void Point::Print(char *str, FILE *fp){
	fprintf(fp, "%s City Number: %d \n X: %f\n Y: %f\n", str, city, pts.x() , pts.y());

}

float Point::Dot(Vec2 that){
	float result; 
	result =  this->point().Dot(that); 
	return result; 
}
