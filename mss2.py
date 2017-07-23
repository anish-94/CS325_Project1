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
maxSum = 0

for i in range(0, totalLen):
	curSum = 0
	for j in range(i, totalLen):
		curSum = curSum + data[j]
		if(curSum > maxSum):
			maxSum = curSum
			result = data[i:j+1]

#print result[:]
#print maxSum

resultLen = len(result)
result = map(str, result)

with open("MSS_Results.txt", "w") as f:
	f.write(' '.join(result))
	f.write('\n')
	f.write("Sum is: %d" % maxSum)

stop = datetime.now()

print("Time taken = %s" % (stop-start))
