#include "quickhull.h"
#include <limits.h>

Point * quickHull(Point * in){
	Point * convexHull;
	Point temp[100]; 
	if(sizeof(in) < 3)	//if our set is 3 point our hull is this set
		return in; 
	int minPoint = -1;
	int maxPoint = -1; 
	int minX = INT_MAX; 
	int maxX = INT_MIN; 


	convexHull = new Point[sizeof(temp)]; 	
	return convexHull;
}

int main(){
	Point  data_set[100];
	Point a (1, 51,21); 
	Point b (2,24,52);
	Point c (3,33,73); 
	data_set[0] = a;
	data_set[1] = b;
	data_set[2] = c; 
	a.print();	
	b.print();
	c.print(); 
	int dis = a.distance(a,b,c);


	return 0; 
} 
