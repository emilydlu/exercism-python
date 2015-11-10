from collections import Counter

def word_count(n):
	return Counter(n.lower().split())

