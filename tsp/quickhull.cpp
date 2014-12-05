#include <limits.h>
#include <vector> 
#include <algorithm>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include "parser.h"
//part of the quick hull algorithm based on http://www.ahristov.com/tutorial/geometry-games/convex-hull.html
int point_location(City A, City B, City P){
        int cp1 = (B.x() - A.x())*(P.y()-A.y()) - (B.y()-A.y())*(P.x()-A.x());
        if(cp1 > 0)
                return 1;
       	else
		 return -1;
}

//part of the quick hull algorithm based on http://www.ahristov.com/tutorial/geometry-games/convex-hull.html
int distance(City A, City B, City C){
        int ABx = B.x() - A.x();
        int ABy = B.y() - A.y();
        int num = ABx * (A.y() - C.y()) - ABy * (A.x() - C.x());
        if (num < 0)
                num = -num;
        return num;
}

//part of the quick hull algorithm based on http://www.ahristov.com/tutorial/geometry-games/convex-hull.html
void hull_set(City A, City B, vector<City> &set, vector<City> &hull){
	int insert_position =  find(hull.begin(), hull.end(), B) -  hull.begin();
	if (set.size() == 0)
		return;
	if (set.size() == 0){
		City p = set[0];
		//set.erase(set.begin()); 
		hull.insert(hull.begin() + insert_position, p); 
		return;
	}
	int dist = INT_MIN;
	int furthestCity = 0;
	for (int i = 0; i < set.size(); ++i){
		City p = set[i];
		int distance1 = distance(A,B,p);
		if (distance1 > dist){
			dist = distance1;
			furthestCity = i;
//			cout << "furthest index" <<furthestCity <<endl;
		}
	}

	City P = set[furthestCity];
//	set[furthestCity].Print("set");
//	for(int i = 0; i <set.size(); i++)
//		set[i].Print("set");
//	cout <<"furthest " <<furthestCity <<endl;
	hull.insert(hull.begin()+insert_position,P);
	set.erase(set.begin() + furthestCity);
//	 for(int i = 0; i <set.size(); i++)
//              set[i].Print("set");


	vector<City> leftSetAP(0); 
	for (int i = 0; i< set.size(); i++){
		City M = set[i];
		if(point_location(A,P,M)==1){
			//set.erase(set.begin() + i);
			leftSetAP.push_back(M);
		}
	}

	vector<City> leftSetPB(0);
	for (int i = 0; i< set.size(); i++){
		City M = set[i];	
		if(point_location(P,B,M)==1){
			//set.erase(set.begin() + i); 
			leftSetPB.push_back(M);
		}
	}
	
           
	hull_set(A,P,leftSetAP,hull);
	hull_set(P,B,leftSetPB,hull);

//	for(int i =0; i < leftSetPB.size(); i++){
  //              leftSetPB[i].Print("right set");
    //            set.push_back(leftSetPB[i]);
      //  }
        //for(int i =0; i < leftSetAP.size(); i++){
       //         leftSetAP[i].Print("left set");
         //       set.push_back(leftSetAP[i]);
       // }

}

//qucikHull algorithm based on algorithm based on http://www.ahristov.com/tutorial/geometry-games/convex-hull.html java implimentation
vector<City> quickHull(vector<City> points_in){
	vector<City> convexHull(0);
	if(points_in.size() < 3){			//if our set is 3 point our hull is this set
							//		City A = points_in[0];	//Add the first point to the end so that we connect
							//		points_in.push_back(A);
		return points_in; 
	}
	int minCity = -1;
	int maxCity = -1; 
	int minX = INT_MAX; 
	int maxX = INT_MIN; 
	for (int i = 0; i < points_in.size(); i++){
		if(points_in[i].x() < minX){
			minX = points_in[i].x();
			minCity = i;
		}
	
		if(points_in[i].x() > maxX){
			maxX = points_in[i].x();
			maxCity = i;
		}
	}

	City A = points_in[minCity];
	City B = points_in[maxCity]; 
	convexHull.push_back(A);
	convexHull.push_back(B); 
	points_in.erase(points_in.begin() + minCity);
	points_in.erase(points_in.begin() + maxCity); 
	
	vector<City> left_set;
	vector<City> right_set;

	for (int i = 0; i < points_in.size(); i++) {
		City p = points_in[i]; 	
		if (point_location(A,B,p) == -1){
			left_set.push_back(p); 
		}
		else{ 
			right_set.push_back(p); 
		}
	}
	hull_set(A,B,right_set,convexHull);
	hull_set(B,A,left_set,convexHull);

	points_in.clear();
	for(int i =0; i < right_set.size(); i++){
		//right_set[i].Print("right set"); 
     		points_in.push_back(right_set[i]); 
	}
	      for(int i =0; i < left_set.size(); i++){
		//left_set[i].Print("left set"); 
		points_in.push_back(left_set[i]); 
	}

	return convexHull;
}

//**in**
//City A the starting point of the line
//City B the ending point of the line
//City point the point to find the distance to
//**out**
//the distance from this line to the point
double point_to_line(Vec2 A, Vec2 B, City point)
{
	float diffX = B.x() - A.x();
	float diffY = B.y() - A.y();
	if ((diffX == 0) && (diffY == 0)){
		diffX = point.x() - A.x();
		diffY = point.y() - A.y();
		return sqrt(diffX * diffX + diffY * diffY);
	    }

	float t = ((point.x() - A.x()) * diffX + (point.y() - A.y()) * diffY) / (diffX * diffX + diffY * diffY);

	if (t < 0){
		//point is nearest to the first point i.e x1 and y1
		diffX = point.x() - A.x();
		diffY = point.y() - A.y();
	}
	else if (t > 1){
		//point is nearest to the end point i.e x2 and y2
		diffX = point.x() - B.x();
		diffY = point.y() - B.y();
	}
	else
	{
		//if perpendicular line intersect the line segment.
		diffX = point.x() - (A.x() + t * diffX);
		diffY = point.y() - (A.y() + t * diffY);
	}
    //return shortest distance
    return sqrt(diffX * diffX + diffY * diffY);
}

//returns the line that
vector< pair<Line, vector<City> > > determine_closest_lines(vector<Line> &hull_lines, vector<City> &points){
//	cout << points.size() << endl; 
	vector<float> min_dist(points.size(), INT_MAX);
	vector<int> min_lines(points.size()); 
	vector< pair<Line, vector<City> > > line_city_pair; 
	for(int i = 0; i < hull_lines.size(); i++){
		pair<Line, vector<City> > temp; 
		temp.first = hull_lines[i]; 
		line_city_pair.push_back(temp); 
	} 

	for(int i = 0; i < hull_lines.size(); i++){
		for(int j = 0; j < points.size(); j++){
			double dist = hull_lines[i].ltp(points[j]);
			if(dist < min_dist[j]){
				//line_city_pair[i].second.push_back(points[j]); 		
				min_lines[j] = i; 
				min_dist[i] = dist; 
				//cout << min_dist[j] << endl;
			}
		}
	}

		for(int j = 0; j < min_dist.size();j++){
			line_city_pair[min_lines[j]].second.push_back(points[j]); 
		}

	

return line_city_pair; 
}

vector<Line> draw_lines(vector<City> &hull_points, vector<City> &inside_points){
	vector<Line> hull_lines;
	for(int i = 0; i < hull_points.size(); i++){
		if(i == hull_points.size()-1)
                        hull_lines.push_back(Line(hull_points[i].point(),hull_points[0].point()));
                else
                        hull_lines.push_back(Line(hull_points[i].point(),hull_points[i+1].point()));
               
//                hull_lines[i].Print("hull lines ");
        }
return hull_lines;
}

void redraw_line(Line line_in, City p){
//draw a line from the start of line_in to point p
//and then draw a line from point p to the end of line_in
//	Line start_to_P(line_in.points(), p.point());
//	Line p_to_end(p.point(),line_in.vectors()); 
//	start_to_P.Print();
//	p_to_end.Print();
}

void hull_sort(vector<City> &hull_points, int i){
	long double min_dist = -1; 
	int min_index = 0; 

	for(int j = i+1; j < hull_points.size(); j++){
		Vec2 temp = hull_points[j].point() - hull_points[i].point();
//		cout << j << min_dist <<endl; 
		if( temp.Length() < min_dist || min_dist < 0){
		 	min_dist = temp.Length(); 
			min_index = j;
		}
	}
	
//	hull_points[min_index].Print("closest points"); 
	City temp = hull_points[i+1]; 	
	hull_points[i+1] = hull_points[min_index]; 
	hull_points[min_index] = temp; 
//swap with the one that is i + 1 

	if(i+1 < hull_points.size()-1)
		hull_sort(hull_points, i+1); 
}
int main(){
	vector<City> tsp; 
	city_parser("input-test1.txt", tsp); 	
	FILE * o_f;
	o_f = fopen("output-test1.txt", "w");



	City  data_set[6] = City();
 	data_set[0] = City(1,15,3); 
	data_set[1] = City(2,9,0);
	data_set[2] = City(3,2,8);
	data_set[3] = City(4,11,6);  
	data_set[4] = City(5,2,2);
	data_set[5] = City(6,8,9);

//	for(int i = 0; i< tsp.size(); ++i)
//		tsp[i].Print("before");

	vector<City> hull_points = quickHull(tsp); 

	int remove_index = 0;  

	for(int i =0; i <hull_points.size();i++){
		remove_index =  find(tsp.begin(), tsp.end(), hull_points[i]) -  tsp.begin();
		tsp.erase(tsp.begin() + remove_index);
	}	
//	for(int i = 0; i< tsp.size(); ++i)
//		tsp[i].Print("after"); 

//	for(int i =0; i <hull_points.size();++i)
//		hull_points[i].Print("tsp"); 

	hull_sort(hull_points, 0);
	vector<Line> hull_lines = draw_lines(hull_points, tsp);	


//	for(int i = 0; i <tsp.size();i++)
//		tsp[i].Print();

/*	for(int i =0; i<hull_points.size();i++)
		hull_points[i].Print();
*/

	vector< pair<Line, vector<City> > > closest_lines = determine_closest_lines(hull_lines, tsp);

//	for(int i = 0; i < tsp.size(); i++)	
//		closest_lines[i].second.push_back(tsp[i]);

	for(int i =0; i < closest_lines.size(); i++){
		int *lengths = new int[closest_lines[i].second.size()];
		 for(int j=0; j<closest_lines[i].second.size();j++){
                        Vec2 temp = closest_lines[i].first.points().Unit(); 
			lengths[j] = closest_lines[i].second[j].point().Dot(temp);
		 }
		quickCitySort(closest_lines[i].second, lengths, 0, closest_lines[i].second.size()-1); 
	}


//	for(int i =0; i<closest_lines.size();i++){
//		hull_points[i].Print(); 
//		for(int j=0; j <closest_lines[i].second.size(); j++){
//			closest_lines[i].second[j].Print(); 
//		}
//	}		
 
// compute our walk. 
	float tot_len = 0; 
	vector<City> walk; 
	for(int i = 0; i < closest_lines.size();++i){
		walk.push_back(hull_points[i]); 
		for(int j = 0; j < closest_lines[i].second.size(); ++j){
			walk.push_back(closest_lines[i].second[j]); 
		}
	}

//compute total length
	Vec2 temp;
	float tempy; 
	for(int i =0; i < walk.size(); i++){
		float a0 = walk[i].point().x();
		float b0 = walk[i-1].point().x();
		float a1 = walk[i].point().y();
		float b1 = walk[i-1].point().y();
		float dx = a0 - b0;
		float dy = a1 - b1;
		tempy = rint(sqrt(dx*dx + dy*dy));
		tot_len += tempy;
	}

//print solutionte total length
//	fprintf(o_f, " %i",tot_len); 
        for(int i =0; i < walk.size(); i++){
                        walk[i].Print("",o_f);
	}
//
	cout << "total path length is: " << tot_len <<" units of space" <<endl; 
 

return 0;
} 
