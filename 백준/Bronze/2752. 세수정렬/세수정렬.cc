#include <stdio.h>

int main(void)
{
	int arrays[3];
	int index, i, j, temp, min;

	for ( int i = 0; i < 3; i++ )
	{
		scanf("%d", &arrays[i]);
	}

	for ( int i = 0; i < 3; i++ )
	{
		min = 1000001;

		for ( int j = i; j < 3; j++ )
		{
			if ( min > arrays[j] )
			{
				min = arrays[j];
				index = j;
			}
		}
		temp = arrays[i];
		arrays[i] = arrays[index];
		arrays[index] = temp;
	}

	for ( i = 0; i < 3; i++ )
	{
		printf("%d ", arrays[i]);
	}

	return 0;
}