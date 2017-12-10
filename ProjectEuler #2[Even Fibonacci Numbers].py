#!/usr/bim/python

#Author@ Junth Basnet

#Mathematics(Fibonacci numbers)
#Time Complexity:O(28*T)
#Formula:f(n)=f(n-1)+f(n-2)
#Even Numbers:E(n)=4E(n-1)+E(n-2)

import sys

def fibonacci(max=4*10**16):
	a,b=0,1
	while(a<max):
		yield a
		a,b=b,a+b

fib=[]
for i in fibonacci():
	if i%2==0:
		fib.append(i)

for i in range(input()):
	n=input()
	evennumbers = filter(lambda x:x<=n,fib)
	print sum(evennumbers)
	
