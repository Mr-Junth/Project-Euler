#Author@Junth Basnet
#Lowest Common Multiple
#Euclidean Algorithm
#Time Complexity:O(n)



def gcd(a, b):
	if(b==0):
		return a
	else:
		return gcd(b,a%b)
def lcm(a,b):
	return (a*b)/gcd(a,b)

for i in range(int(raw_input())):
	n=int(raw_input())
	print reduce(lambda a,b:lcm(a,b),range(1,n+1))
	
