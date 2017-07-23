import random

n = 100				#change n as needed
data = []

while len(data) < n:
	data.append(random.randint(-5000, 5000))	#Change range as needed but make sure to have negative values

print data[:] 

