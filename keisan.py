import numpy as np

def read_file(file_name):
	f = open(file_name)
	node_n = int(f.readline().split()[0])
	elem_n = int(f.readline().split()[0])
	#print (node_n)
	#print (elem_n)
	nodes = np.zeros((node_n+1, 2), dtype="float128")
	elems = np.zeros((elem_n+1, 3), dtype="int16")

	for i in range(node_n):
		x, y = map(float, f.readline().split()[1:])
		nodes[i+1, :]= x, y
		
	for i in range(elem_n):
		a, b, c= map(int, f.readline().split()[2:])
		elems[i+1, :]= a, b, c
		
	#for i in range(node_n):
	#	print (nodes[i+1])

	#for i in range(elem_n):
	#	print (elems[i+1])

	f.close()
	return (node_n, elem_n, nodes, elems)	

def delta(nodes, elem):
	a, b ,c = elem
	delta_mat= np.ones((3,3))
	delta_mat[:, [0,1]] = nodes[[a, b, c], :]
	return 0.5* np.abs(np.linalg.det(delta_mat))

if __name__ == "__main__":
	print(__name__)
	node_n, elem_n, nodes, elems = read_file("keisan.txt")

	for i in range(elem_n):
		#raw_input("Enter to continue")
		a, b, c =elems[i+1]
		#print(nodes[[a,b,c], :])
		delta_mat = np.ones((3,3))
		delta_mat[:,:2] = nodes[[a,b,c], :]
		#print(delta_mat)

		print(delta(nodes, elems[i+1]))
