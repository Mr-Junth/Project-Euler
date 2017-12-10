//Author@Junth Basnet
//Discrete Mathematics[Prime Numbers]
//Time Complexity:O(n)

#include<bits/stdc++.h>

using namespace std;

int main()
{
	int test;
	scanf("%d",&test);
	while(test--)
	{
		long long number;
		scanf("%lld",&number);
		long long primefactor=1;
		for(long long i=2;i<=sqrt(number);i++)
		{
			while(number%i==0)
			{
				primefactor=i;
				number/=i;
			}
		}
		if(number>1)
		{
			primefactor=number;
		}
		printf("%lld\n",primefactor);
	}
	return 0;
}