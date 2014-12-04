#include "city.h"
City::City (){
	id = -1;
	pts = Vec2(0,0);
}


City::City (int city_in, int x_in, int y_in){
        id = city_in;
        pts = Vec2 (x_in, y_in);
}

bool City::operator==(City B){
	if(id == B.city_num() && pts == B.point())
		return true;
	return false; 
}

void City::Print(char *str, FILE *fp){
	fprintf(fp, "%s %d\n", str, id); 

//	fprintf(fp, "%s City Number: %d \n X: %f\n Y: %f\n", str, id, pts.x() , pts.y());

}

float City::Dot(Vec2 that){
	float result; 
	result =  this->point().Dot(that); 
	return result; 
}
