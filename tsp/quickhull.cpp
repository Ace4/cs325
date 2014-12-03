#include "line.h"
#include <limits.h>
#include <vector> 
#include <algorithm>
#include <stdio.h>
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
	if (set.size() == 1){
		City p = set[0];
		set.erase(set.begin());
		hull.insert(hull.begin() + insert_position,p); 
		return;
	}
	int dist = INT_MIN;
	int furthestCity = -1;
	for (int i = 0; i <set.size(); i++){
		City p = set[i];
		int distance1 = distance(A,B,p);
		if (distance1 > dist){
			dist = distance1;
			furthestCity = i;
		}
	}
	City P = set[furthestCity];
	set.erase(set.begin() + furthestCity); 
	hull.insert(hull.begin()+insert_position,P);

	vector<City> leftSetAP(0); 
	for (int i = 0; i< set.size(); i++){
		City M = set[i];
		if(point_location(A,P,M)==1){
			leftSetAP.push_back(M);
		}
	}

	vector<City> leftSetPB(0);
	for (int i = 0; i< set.size(); i++){
		City M = set[i];	
		if(point_location(P,B,M)==1){
			leftSetPB.push_back(M);
		}
	}
	
	hull_set(A,P,leftSetAP,hull);
	hull_set(P,B,leftSetPB,hull);

}

//qucikHull algorithm based on algorithm based on http://www.ahristov.com/tutorial/geometry-games/convex-hull.html java implimentation
vector<City>  quickHull(vector<City> &points_in){
	vector<City> convexHull(0);
	if(points_in.size() < 3){			//if our set is 3 point our hull is this set
		City A = points_in[0]; 		//Add the first point to the end so that we connect
		points_in.push_back(A);
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
	int x =	convexHull.size();
	points_in.erase(points_in.begin() + minCity);
	points_in.erase(points_in.begin() + maxCity); 
	
	vector<City> left_set(0);
	vector<City> right_set(0);

	for (int i = 0; i < points_in.size(); i++) {
		City p = points_in[i]; 
		if (point_location(A,B,p) == -1)
			left_set.push_back(p); 
		else 
			right_set.push_back(p); 
	}
	hull_set(A,B,right_set,convexHull);
	hull_set(B,A,left_set,convexHull);

	points_in.clear();
	for(int i =0; i < right_set.size();i++){
     		points_in.push_back(right_set[i]); 
	}
        for(int i =0; i<left_set.size(); i++){
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
	vector<float> min_dist(points.size(), INT_MAX);
	vector<Line> min_lines(points.size()); 
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
				line_city_pair[i].second.push_back(points[j]); 		
				//min_lines[j] = hull_lines[i]; 
				//min_dist[j] = dist; 
			}
		}
	}
return line_city_pair; 
}
vector<Line> draw_lines(vector<City> &hull_points, vector<City>  &inside_points){
	vector<Line> hull_lines;
	for(int i = 0; i < hull_points.size(); i++){
		if(i == hull_points.size()-1)
                        hull_lines.push_back(Line(hull_points[i].point(),hull_points[0].point()));
                else
                        hull_lines.push_back(Line(hull_points[i].point(),hull_points[i+1].point()));
               
                hull_lines[i].Print("hull lines ");
        }
return hull_lines;
}

void redraw_line(Line line_in, City p){
//draw a line from the start of line_in to point p
//and then draw a line from point p to the end of line_in
	Line start_to_P(line_in.points(), p.point());
	Line p_to_end(p.point(),line_in.vectors()); 
	start_to_P.Print();
	p_to_end.Print();
}
int main(){
	City  data_set[8] = City();
 	data_set[0] = City(1,5,5); 
	data_set[1] = City (2,-5,5);
	data_set[2] = City(3,-5,-5);
	data_set[3] = City(4,5,-5);  
	data_set[4] = City(9,3,1);
	data_set[5] = City(10,3,-1);
	data_set[6] = City(11,-3,1);
	data_set[7] = City(12,-3,-1);
/*	Line AB(data_set[0].point(),data_set[1].point());
	Line BC(data_set[1].point(),data_set[2].point()); 
	Line CD(data_set[2].point(),data_set[3].point());	
	Line DA(data_set[3].point(),data_set[0].point());

	double ab =	AB.ltp(data_set[4]); 
	double bc =     BC.ltp(data_set[4]);
	double cd =     CD.ltp(data_set[4]);
	double da =     DA.ltp(data_set[4]);
	
	cout <<"abe: "  << ab <<endl;
	cout <<"bce: "  << bc <<endl;
	cout <<"cde: "  << cd <<endl;
	cout <<"dae: "  << da <<endl;
*/
	vector<City> tsp; 
	int i = 0;
	for (int i = 0; i < 8; i++){
		tsp.push_back(data_set[i]);
	}
	vector<City> hull_points = quickHull(tsp); 
	vector<Line> hull_lines = draw_lines(hull_points, tsp);	
	vector< pair<Line, vector<City> > > closest_lines = determine_closest_lines(hull_lines, tsp);
        for( int i =0; i < closest_lines.size(); i++){
		tsp[i].Print();		        
		closest_lines[i].first.Print("closest line");
		float x = tsp[i].x() - closest_lines[i].first.vectors().x();	//= tsp[i].Dot(min_dist[i].vectors()); 
		float y = tsp[i].y() - closest_lines[i].first.vectors().y();
		float d = sqrt( x * x + y * y); 
		cout << "\tDistance "<< d <<endl<<endl;
		//redraw_line(min_dist[i], tsp[i]); 
	}	

//	closest_lines[0].second[1].Print("waaat"); 
	
//	array tuples(line array citys)
//	Hull_Line[0][0], Hull_line[0][1] city
//	vector< pair<Line,vector<City> > > closest_line_pair;
//	pair<Line,vector<City> > temp;
//	temp.first = hull_lines[0]; 
//	temp.second.push_back( tsp[0]); 
//	closest_line_pair.push_back(temp); 
//	closest_line_pair[0].first.Print();

return 0;
} 
