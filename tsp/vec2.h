#include <stdio.h>
#include <string.h>
#define _USE_MATH_DEFINES
#include <cmath>

#ifndef VEC3_H
#define VEC3_H

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
	float	x() {return v0;};
	float 	y() {return v1;};
	float   Cross( Vec2& );
        float   Dot( Vec2& );
        float   Length( );
        void    Print( char * = "", FILE * = stderr );
        Vec2    Unit( );

	friend class Mat4;
};

inline float 
SWR( float f)
{
	return f * f; 
}

#endif

