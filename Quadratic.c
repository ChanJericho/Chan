#include <stdio.h>
#include <math.h>

int main(int argc, char const *argv[])
{
	int a = 1, b, c;
	double answer1, answer2, value;
	
	while(a != 0){
		
		printf("Coeeficients: ");
		scanf("%d", &a);
		if(a != 0)
		{
		scanf("%d %d", &b, &c);
		value = (b * b) - (4 * a * c);
		
		if(value < 0)
		{
			printf("COMPLEX\n");
		}
		
		else
		{
			answer1 = (- b + sqrt(value)) / (2 * a);
			answer2 = (- b - sqrt(value)) / (2 * a);
			printf("%.4lf, %.4lf\n", answer1, answer2);
		}
		}
	}
	return 0;
}
