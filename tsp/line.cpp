#include "line.h"

Line::Line(){
	pts = Vec2(0,0);
	vecs = Vec2(0,0);
}

Line::Line(Vec2 pts_in, Vec2 vec_in){
	pts = pts_in;
	vecs = vec_in;
}
bool Line::operator==(Line &line_in){
	if(line_in.points() == pts && line_in.vectors() == vecs)
		return true;
	return false;
}

void Line::Print(char *str, FILE *fp){
	fprintf(fp, "\t%s x: %f + (%f)*t \n",str,  pts.x(), vecs.x());
	fprintf(fp, "\t%s y: %f + (%f)*t \n\n",str,	pts.y(), vecs.y());

}

Line Line::Dot(Vec2& that){
	Line result( pts.Dot(that),vecs.Dot(that));
	return result;

} 

//*** in ***
// a  point
//*** out *** 
// minimum distance from that point to this line 
double Line::ltp(Point point){
        float diffX = vecs.x() - pts.x();
        float diffY = vecs.y() - pts.y();
        if ((diffX == 0) && (diffY == 0)){
		diffX = point.x() - pts.x();
		diffY = point.y() - pts.y();
		return sqrt(diffX * diffX + diffY * diffY);
	} 
	
	float t = ((point.x() - pts.x()) * diffX + (point.y() - pts.y()) * diffY) / (diffX * diffX + diffY * diffY);


	if(t < 0){
		diffX = point.x() - pts.x();
		diffY = point.y() - pts.y();
	} else if (t > 1){
		diffX = point.x() - vecs.x();
		diffY = point.y() - vecs.y();
	} else { 
		//if perpendicular line intetsects the line segment
		diffX = point.x() - (pts.x() + t * diffX);
		diffY = point.y() - (pts.y() + t * diffY);
	}

	//return the distance
	return sqrt(diffX * diffX + diffY * diffY); 
}
