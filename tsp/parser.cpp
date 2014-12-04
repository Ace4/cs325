#include "parser.h"
using std::ifstream;

void city_parser(string file_in, vector<City> &city_list)
{
	const int MAX_CHARS_PER_LINE = 512;
	const int MAX_TOKENS_PER_LINE = 4;
	const char* const DELIMITER = " ";


	int n,city_ind = 0;
	int id, x, y;
	char buf[MAX_CHARS_PER_LINE];

	/* array to store memory addresses of the tokens in buf */
	const char* token[MAX_TOKENS_PER_LINE] = {};    //initialize to 0

	/* create a file-reading obj */
	ifstream f_in;
	

	f_in.open(file_in.c_str()); // , fstream::in);
	if (!f_in.good() ) {
		printf ("Error opening file\n");
		exit(EXIT_FAILURE);                               //exit if file not found
	}

	id = x = y = 0;
	while (!f_in.eof() ) {
		/* read an entire line into memory */
		f_in.getline(buf, MAX_CHARS_PER_LINE);

		/* parse the line and extract first token */
		if(buf != NULL){
			token[0] = strtok(buf, DELIMITER);
				if(token[0] != NULL)
				id = atoi(token[0]);
		}

		city_list.push_back(City(id, x, y ));  //city id    

		if (token[0]) {                         //zero if line is blank
			for (n = 1; n < MAX_TOKENS_PER_LINE; n++) {
				token[n] = strtok(0, DELIMITER); 

				if (n == 1) {           //city x-coord.  
					if(token[1] != NULL)
						x = atoi(token[1]);
					city_list[n].set_x(x);
				}
				
				if (n == 2) {           //city y-coord.
					if(token[2] != NULL)
						y = atoi(token[2]);
					city_list[n].set_y(y); //=  City(id, x, y);
				}
				if (!token[n]) break;   //no more tokens
			}
		
		/* increment to next city */
		city_ind++;
		}
	}
	
//	for (int j = 0; j < city_list.size() ; j++) {
//		city_list[j].Print();
//	}
}

