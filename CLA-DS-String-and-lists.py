#Ex 1
L = []
for i in range(299):
	if i % 2 == 0:
		L.append(i)
print(L)


#Ex 2
print("L length is : ", L.length)
for x in L:
	print(x**2)


#Ex 3
print(L.__contains__(57))
