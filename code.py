def buildA(count):
	a = []
	i = 0
	while(i < count):
		a = a + [count]
		i = i + 1
	return a


def decrease(aList, size):
	# f.write("left vertex set: (number indicates the degree of each vertex)")
	# f.write(writeL(aList))

	total = size * size
	count = 0
	graph = []

	while(total > 0):
		length = aList[0]
		graph = graph + [length]
		j = 0
		while(j < length):
			aList[j] = aList[j] - 1
			total = total - 1
			j = j + 1
		count = count + 1
		aList = sortT(aList)
	#	print(aList)

		

		
		
	# 	#print("==================================")
	# f.write("right vertex set: (number indicates the degree of each vertex)\n")
	# f.write(writeL(graph) + "\n")
	# #print("right vertex set: (number indicates the degree of each vertex)")
	# #print(graph)
	# f.write("number of vertext in left set: " + str(size) + "\n")
	# f.write("number of vertext in right set: " + str(len(graph)) + "\n")
	# f.write("ratio is: " + str((float)(len(graph))/len(aList)) + "\n")
	# f.write("==================================\n")
	print(str((float)(len(graph))/len(aList)))
	return count

def writeL(a):
	result = "["
	for i in a:
		result = result + str(i) + ", "
	result = result + "]"
	return result




def sortT(a):
	#print(sorted(a, reverse=True))
	return sorted(a, reverse=True)


q = 1
while(q <= 1000):
	#f = open("result.txt", "a")
	decrease(buildA(q), q)
	
	q = q + 1