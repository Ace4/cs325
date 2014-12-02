#include <iostream>
#include <stdio.h>
#include <string.h>
#include "vec2.h"
using namespace std;

class Point {

		int city;
		Vec2 pts;
	public:
		Point(); 
		Point 	(int city_in, int x_in , int y_in); 
		void 	Print(char * = "", FILE * = stderr); 
		Vec2 	point(){return pts;};
		int 	x(){return pts.x();}; 
		int 	y(){return pts.y();}; 
		int 	city_num() {return city;};
		bool 	operator==(Point B);
		float	Dot( Vec2 ); 
};

