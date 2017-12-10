#Author@Junth Basnet
#Greatest Common Factor[Discrete Mathematics]
#Time Complexity:O(n^2)

from __future__ import division
from fractions import gcd

for i in range(input()):
	prod=1
	n=input()
	for i in range(2,n+1):
		prod=(prod*i)//gcd(prod,i)
	print prod
