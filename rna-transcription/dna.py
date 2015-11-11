def to_rna(n):
	dict = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
	n.split()
	lst = []
	for i in n: 
		lst.append(dict[i])
	return ''.join(lst)

