#Ex 1
def checkPalindrome(S):
	n = len(S)
	for i in (n//2):
		if L[i] != L[n-i]:
			return False
	return True
 

#Ex 2
def primalityTest(n):
	for i in range(int(sqrt(n))):
		if n  % i == 0:
			return False
	return True


#Ex 3
def rangeCheck(a, b, n):
	return ((n >= a) and (n <= b))


#Ex 4
	#Iterative process
def IteFacto(n):
	k = 1
	for i in range(1, n+1):
		k *= i

	#Recursive process
def RecFacto(n):
	if n == 1:
		return 1
	else:
		n*RecFacto(n-1)


#Ex 5
def ReverseString(S):
	revS = ""
	n = len(S)
	for i in range(n):
		revS.append(S[n-i])
	return revS

#Ex 6
def SumList(L):
	s = 0
	for x in L:
		s += x
	return s

#Ex 7
def maxi2(a, b):
	if a >= b:
		return a
	else:
		return b

def maxi3(a, b, c):
	return maxi2(maxi2(a, b), c)

