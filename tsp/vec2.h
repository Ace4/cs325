#include <stdio.h>
#include <string.h>
#define _USE_MATH_DEFINES
#include <cmath>

#ifndef VEC2_H
#define VEC2_H

class Vec2
{
    protected:
        float v0, v1;

    public:
        Vec2( float=0, float=0);
        Vec2&   operator=( const Vec2& );
        bool	operator==( const Vec2& ); 
	Vec2    operator+( const Vec2& );
        Vec2    operator-( const Vec2& );       // binary -
        Vec2    operator-( );                   // unary -
	Vec2	operator*( const Vec2& );
	void	set_x(float x) {v0 = x;};
	void	set_y(float y) {v1 = y;};
	float	x() {return v0;};
	float 	y() {return v1;};
	float   Cross( Vec2& );
        float   Dot( Vec2& );
      	Vec2	Shoot(const Vec2&, float t);
	void	CreateLine(const Vec2&, const Vec2&);
	float   Length( );
        void    Print( char * = "", FILE * = stderr );
        Vec2    Unit( );

};

inline float 
SWR( float f)
{
	return f * f; 
}

#endif

