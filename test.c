#include <stdio.h>

int main()
{
	int capacity;
	do
	{printf("enter your capacity: ");
		scanf("%i", &capacity);}
	while (capacity < 0);

	int array [capacity];
	int size = 0; 
	int number;
	while (size < capacity)
	{
		printf("input value of your array: ");
		scanf("%i", &number);
		array [size] = number;
		size ++;
	}
	for (int i = 0; i < capacity; i++)
	{
		printf("you inputted: %i\n", array[i]);
	}
}