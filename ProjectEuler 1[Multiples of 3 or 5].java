//Author@Junth Basnet
//Arithmetic Progression
//Time Complexity:O(n)

import java.util.*;



public class Solution
{
	public static void main (String[] args)
	{
		Scanner scan=new Scanner(System.in);
		long test=scan.nextLong();
		for(long i=0;i<test;i++)
		{
			long n=scan.nextLong();
			long a=0;
			long b=0;
			long c=0;
			
			a=(n-1)/3;
			b=(n-1)/5;
			c=(n-1)/15;
			
			long sum3=0,sum5=0,sum15=0;
			
			sum3=3*a*(a+1)/2;
			sum5=5*b*(b+1)/2;
			sum15=15*c*(c+1)/2;
			
			long result=sum3+sum5-sum15;
			System.out.println(result);
		}
	}
}