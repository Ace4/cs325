#include "city.h"

#include <iostream>
#include <fstream>
#include <cstring>

#include <stdio.h>
#include <stdlib.h>

using std::ifstream;

const int MAX_CHARS_PER_LINE = 512;
const int MAX_TOKENS_PER_LINE = 4;
const char* const DELIMITER = " ";

int main()
{
	City city_list[76] = City();

	int n,city_ind = 0;
	int id, x, y;
	char buf[MAX_CHARS_PER_LINE];

	/* array to store memory addresses of the tokens in buf */
	const char* token[MAX_TOKENS_PER_LINE] = {};    //initialize to 0

	/* create a file-reading obj */
	ifstream f_in;

	f_in.open("example-input-1.txt");
	if (!f_in.good() ) {
		return 1;                               //exit if file not found
	}

	x = y = 0;
	while (!f_in.eof() ) {
		/* read an entire line into memory */
		f_in.getline(buf, MAX_CHARS_PER_LINE);

		/* parse the line and extract first token */
		token[0] = strtok(buf, DELIMITER);
		id = atoi(token[0]);
		city_list[city_ind] = City(id, x, y );  //city id    

		if (token[0]) {                         //zero if line is blank
			for (n = 1; n < MAX_TOKENS_PER_LINE; n++) {
				token[n] = strtok(0, DELIMITER); 

				if (n == 1) {           //city x-coord.  
					x = atoi(token[1]);
					city_list[city_ind] = City(id, x, y);
				}
				
				if (n == 2) {           //city y-coord.
					y = atoi(token[2]);
					city_list[city_ind] = City(id, x, y);
				}
				if (!token[n]) break;   //no more tokens
			}
		}
		/* increment to next city */
		city_ind++;
	}
	
	for (int j = 0; j < 76; j++) {
		city_list[j].Print();
	}
	
	return 0;
}

