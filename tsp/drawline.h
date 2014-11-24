
void draw_line(Point start_point, Point end_point){ 
	int x = 0;
	int y = 0;

	for (float t = 0; t<10.0; ++t){
		x += start_point.x() + t*(end_point.x() - start_point.x()); 
		y += start_point.y() + t*(end_point.y() - start_point.y());
		cout << x << y <<endl;
	} 
} 
