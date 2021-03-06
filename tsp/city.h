#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include "vec2.h"
using namespace std;

class City {

		int id;
		Vec2 pts;
	public:
		City();
		City 	(int id_in, int x_in , int y_in); 
		void 	Print(char * = "", FILE * = stderr); 
		Vec2 	point(){return pts;};
		void	set_x(float x){pts.set_x(x);};
		void 	set_y(float y){pts.set_y(y);};
		int 	x(){return pts.x();}; 
		int 	y(){return pts.y();}; 
		int 	city_num() {return id;};
		bool 	operator==(City B);
		float	Dot( Vec2 ); 
};

