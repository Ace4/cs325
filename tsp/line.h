#include "point.h"

class Line {
		Vec2 pts;
		Vec2 vecs;
	public:
		Line();
		Line(Vec2, Vec2);
		Vec2 points(){return pts;};
		Vec2 vectors(){return vecs;};
		bool operator==(Line&);
		void Print(char *str = "", FILE *fp = stderr);
		Line Dot(Vec2& that ); 
		double ltp(Point point); 
};
