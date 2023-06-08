#include <stdio.h>

int main(void)
{
	int arrays[1001];
	int index, i, j, temp, min, number;

	scanf("%d", &number);

	for ( int i = 0; i < number; i++ )
	{
		scanf("%d", &arrays[i]);
	}

	for ( int i = 0; i < number; i++ )
	{
		min = 1001;

		for ( int j = i; j < number; j++ )
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

	for ( i = 0; i < number; i++ )
	{
		printf("%d\n", arrays[i]);
	}

	return 0;
}