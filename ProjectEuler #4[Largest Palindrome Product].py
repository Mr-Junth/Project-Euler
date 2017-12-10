#Author@Junth Basnet
#Algorithm and Data Structures[Binary Search Algorithm]
#Palindrome
#Time Complexity:O(n^2)

import bisect

array=[]

for i in range(999,100,-1):
	for j in range(999,100,-1):
		numbers=str(i*j)
		if numbers==numbers[::-1]:
			array.append(i*j)

array.sort()

for i in range(int(raw_input())):
	number=bisect.bisect_left(array,int(raw_input()))
	print array[number-1]