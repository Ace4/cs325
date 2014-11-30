#include "point.h"
#include <limits.h>
#include <vector> 
#include <algorithm>

int point_location(Point A, Point B, Point P){
        int cp1 = (B.x() - A.x())*(P.y()-A.y()) - (B.y()-A.y())*(P.x()-A.x());
        if(cp1>0)
                return 1;
        return -1;
}


int distance(Point A, Point B, Point C){
        int ABx = B.x() - A.x();
        int ABy = B.y() - A.y();
        int num = ABx * (A.y() - C.y()) - ABy * (A.x() - C.x());
        if (num < 0)
                num = -num;
        return num;
}


void hull_set(Point A, Point B, vector<Point> set, vector<Point>& hull){
	int insert_position =  find(hull.begin(), hull.end(), B) -  hull.begin();
	if (set.size() == 0)
		return;
	if (set.size() == 1){
		Point p = set[0];
		set.erase(set.begin() + 0);
		hull.insert(hull.begin() + insert_position,p); 
		return;
	}
	int dist = INT_MIN;
	int furthestPoint = -1;
	for (int i = 0; i <set.size(); i++){
		Point p = set[i];
		int distance1 = distance(A,B,p);
		if (distance1 > dist){
			dist = distance1;
			furthestPoint = i;
		}
	}
	Point P = set[furthestPoint];
	set.erase(set.begin() + furthestPoint); 
	hull.insert(hull.begin()+insert_position,P);

	vector<Point> leftSetAP(0); 
	for (int i = 0; i< set.size(); i++){
		Point M = set[i];
		if(point_location(A,P,M)==1){
			leftSetAP.push_back(M);
		}
	}

	vector<Point> leftSetPB(0);
	for (int i = 0; i< set.size(); i++){
		Point M = set[i];	
		if(point_location(P,B,M)==1){
			leftSetPB.push_back(M);
		}
	}
	
	hull_set(A,P,leftSetAP,hull);
	hull_set(P,B,leftSetPB,hull);

}

vector<Point>  quickHull(vector<Point> points_in){
	vector<Point> convexHull(0);
	if(points_in.size() < 3)	//if our set is 3 point our hull is this set
		return points_in; 
	int minPoint = -1;
	int maxPoint = -1; 
	int minX = INT_MAX; 
	int maxX = INT_MIN; 
	for (int i = 0; i < points_in.size(); i++){
		if(points_in[i].x() < minX){
			minX = points_in[i].x();
			minPoint = i;
		}
	
		if(points_in[i].x() > maxX){
			maxX = points_in[i].x();
			maxPoint = i;
		}
	}

	Point A = points_in[minPoint];
	Point B = points_in[maxPoint]; 
	convexHull.push_back(A);
	convexHull.push_back(B); 
	int x =	convexHull.size();
	points_in.erase( points_in.begin() + minPoint);
	points_in.erase(points_in.begin() + maxPoint); 
	
	vector<Point> left_set(0);
	vector<Point> right_set(0);

	for (int i = 0; i < points_in.size(); i++) {
		Point p = points_in[i]; 
		if (point_location(A,B,p) == -1)
			left_set.push_back(p); 
		else 
			right_set.push_back(p); 
	}
	hull_set(A,B,right_set,convexHull);
	hull_set(B,A,left_set,convexHull); 

	return convexHull;
}

int main(){
	Point  data_set[100];
	Point a (1,0,0); 
	Point b (2,0,200);
	Point c (3,-4,-30); 
	Point d (4,55,100);
	Point e (5,32,71);	
	Point f (6,54,100);
	data_set[0] = a;
	data_set[1] = b;
	data_set[2] = c; 
	vector<Point> tsp; 
	tsp.push_back(a);
	tsp.push_back(b);
	tsp.push_back(c); 
	tsp.push_back(d);
	tsp.push_back(e);
	tsp.push_back(f);
	vector<Point> the_hull = quickHull(tsp); 
	
	for(int i = 0; i< the_hull.size(); i++)
		the_hull[i].print();
	return 0; 

} 
