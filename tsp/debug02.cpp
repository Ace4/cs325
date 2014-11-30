#include "vec2.h"

int main( int argc, char * argv[ ] )
{
	Vec2 b( 1., 2. );
	Vec2 c( 5., 6. );

	Vec2 a = c;
	Vec2 au = a.Unit( );
	a.Print( "a =" );
	au.Print( "a normalized =" );
	b.Print( "b =" );
	c.Print( "c =" );

	a = Vec2( 2., -5);
	a.Print( "a =" );

	Vec2 ma = -a;
	ma.Print( "-a = " );

	Vec2 e = a + b;
	e.Print( "a+b =" );

	e = a - b;
	e.Print( "a-b =" );


	float f = ( a + b ).Length( );

	Vec2 g = a.Cross(b);
	g.Print( "a cross b ="); 	

	float length = a.Length();
	printf("length = %f\n", length);
	float h = a.Dot(b); 	
	printf("a DOT b = %f\n", h);

	return 0;
}
