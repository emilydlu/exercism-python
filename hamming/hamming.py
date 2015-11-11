
def distance(a, b):
	if len(a)!= len(b):
		return
	counter = 0 
	for i in range(len(a)):
		if a[i]!= b[i]:
			counter+=1
	return counter


