from datetime import datetime

start = datetime.now()

with open("MSS_Problems.txt") as f:
	data = []
	for line in f.readlines():
		data = line.split(" ")
		data = [x.strip() for x in data]
		data = map(int, data)


totalLen = len(data)
result = []

def findSubArray(data, left, right):

	if (left == right): 
		return data[left], left, right

	middle = (left+right)/2
	leftres, _ , _ = findSubArray(data, left, middle)
	rightres, _ , _ = findSubArray(data, middle+1, right)	
	
	leftmax = data[middle]
	rightmax = data[middle+1]
	
	indx = middle	
	endx = middle+1
	
	temp = 0
	
	for i in range(middle, left-1, -1):
		temp = temp + data[i]

		if(temp > leftmax):
			leftmax = temp
			indx = i
	
	temp = 0
	for i in range(middle+1, right):
		temp = temp + data[i]
		
		if(temp > rightmax):
			rightmax = temp
			endx = i
	
	maxSum =  max(max(leftres, rightres), leftmax+rightmax)
	
	return maxSum, indx, endx

maxSum, begin, final = findSubArray(data, 0, totalLen-1)

result = data[begin:final+1]
resultLen = len(result)
result = map(str, result)

with open("MSS_Results.txt", "w") as f:
	f.write(' '.join(result))
	f.write('\n')
	f.write("Sum is " + str(maxSum))

stop = datetime.now()

print("Time taken = %s" % (stop-start))
