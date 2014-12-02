#include "vec2.h"

Vec2::Vec2( float x, float y )
{
	v0 = x;
	v1 = y;
}

Vec2& Vec2::operator=( const Vec2& rhs )
{
	this->v0 = rhs.v0;
	this->v1 = rhs.v1;
	return *this;
}

bool Vec2::operator==( const Vec2& rhs)
{
	if(this->v0 == rhs.v0 && this->v1 == rhs.v1)
		return true;
	return false;
}
Vec2 Vec2::operator+( const Vec2& that )
{
	Vec2 result;
	result.v0 = this->v0 + that.v0;
	result.v1 = this->v1 + that.v1;
	return result;
}

Vec2 Vec2::operator-( const Vec2& that )
{
	Vec2 result;
	result.v0 = this->v0 - that.v0;
	result.v1 = this->v1 - that.v1;
	return result;
}

Vec2 Vec2::operator-( )
{
	Vec2 result;
	result.v0 = -this->v0;
	result.v1 = -this->v1;
	return result;
}

Vec2 Vec2::operator*(const Vec2& that)
{
	Vec2 result;
	result.v0 = this->v0 * that.v0;
	result.v1 = this->v1 * that.v1;
	return result;
}
float Vec2::Cross( Vec2& that )
{
	return (this->v0 * that.v1) - (this->v1 * that.v0);	
}

Vec2 Vec2::Shoot(const Vec2& that, float t){
	Vec2 result;
	result.v0 = this->v0 + t *(that.v0 - this->v0);
	result.v1 = this->v1 + t *(that.v1 - this->v1); 	
	return result; 
}


float Vec2::Dot( Vec2& that )
{
	float d = (this->v0 * that.v0) + (this->v1 * that.v1);
	return d;
}

float Vec2::Length()
{
	float len = sqrt(pow(this->v0,2) +pow(this->v1,2));
	return len;
}

void Vec2::Print( char *str, FILE *fp )
{
	fprintf( fp, "%s [ %8.3f %8.3f ]\n", str, this->v0, this->v1);
}

Vec2 Vec2::Unit( )
{
	Vec2 result;
	float len = this->Length(); 
	result.v0 = this->v0 / len;
	result.v1 = this->v1 / len;
	return result;
}

