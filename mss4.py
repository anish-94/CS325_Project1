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
curSum = data[0]
maxSum = data[0]
temp = []

for i in range(1, totalLen):			#Leetcode helped here
	curSum = max(data[i], curSum + data[i])

	if(curSum > maxSum):
		maxSum = curSum
		temp.append(i)

init = temp[0]
end = temp[len(temp)-1] + 1 

result = data[init:end]

resultLen = len(result)
result = map(str, result)
with open("MSS_Results.txt", "w") as f:
	f.write(' '.join(result))
	f.write('\n')
	f.write("Sum is %d" % maxSum)

stop = datetime.now()

print("Time taken = %s" % (stop-start))
