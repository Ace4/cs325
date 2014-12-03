#include <stdio.h>
#include "line.h"
#include <vector>

void quickCitySort(City city[], int arr[], int left, int right) {
      int i = left, j = right;
      int tmp1;
      City tmp2 = City();
      int pivot = arr[(left + right) / 2];

      /* partition */
      while (i <= j) {
            while (arr[i] < pivot)
                  i++;
            while (arr[j] > pivot)
                  j--;
            if (i <= j) {
                  tmp1 = arr[i];
                  arr[i] = arr[j];
                  arr[j] = tmp1;

		tmp2 = city[i];
		city[i] = city[j];
		city[j] = tmp2;	

                  i++;
                  j--;
            }
      };

      /* recursion */
      if (left < j)
            quickCitySort(city, arr, left, j);

      if (i < right)
            quickCitySort(city, arr, i, right);

}

int main(){
	int lengths[] = {4, 7, 2, 8, 1, 6, 9, 2};
	City  data_set[8] = City();
 	data_set[0] = City(1,5,5); 
	data_set[1] = City (2,-5,5);
	data_set[2] = City(3,-5,-5);
	data_set[3] = City(4,5,-5);  
	data_set[4] = City(9,3,1);
	data_set[5] = City(10,3,-1);
	data_set[6] = City(11,-3,1);
	data_set[7] = City(12,-3,-1);
	quickCitySort(data_set, lengths, 0, 7);
	for(int i = 0; i <= 7; i++){
		printf("Length: %d\t", lengths[i]);
		data_set[i].Print();
	}
	return 0;
}
