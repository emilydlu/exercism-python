from collections import Counter

def word_count(n):
	return Counter(n.lower().split())

# def word_count(n): 
# 	wordcount = {}
# 	n = n.lower()
# 	lst = n.split()
# 	for word in lst:
# 		if word not in wordcount: 
# 			wordcount[word] =1
# 		else: 
# 			wordcount[word]+=1
# 	return wordcount
