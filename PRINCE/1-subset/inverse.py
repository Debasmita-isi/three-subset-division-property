# Python3 program to find adjoint and
# inverse of a matrix
N = 16

# Function to get cofactor of
# A[p][q] in temp[][]. n is current
# dimension of A[][]
def getCofactor(A, temp, p, q, n):

	i = 0
	j = 0

	# Looping for each element of the matrix
	for row in range(n):

		for col in range(n):

			# Copying into temporary matrix only those element
			# which are not in given row and column
			if (row != p and col != q):

				temp[i][j] = A[row][col]
				j += 1

				# Row is filled, so increase row index and
				# reset col index
				if (j == n - 1):
					j = 0
					i += 1


# Recursive function for finding determinant of matrix.
# n is current dimension of A[][].
def determinant(A, n):

	D = 0 # Initialize result

	# Base case : if matrix contains single element
	if (n == 1):
		return A[0][0]

	temp = [] # To store cofactors
	for i in range(N):
		temp.append([None for _ in range(N)])

	sign = 1 # To store sign multiplier

	# Iterate for each element of first row
	for f in range(n):

		# Getting Cofactor of A[0][f]
		getCofactor(A, temp, 0, f, n)
		D += sign * A[0][f] * determinant(temp, n - 1)

		# terms are to be added with alternate sign
		sign = -sign

	return D


# Function to get adjoint of A[N][N] in adj[N][N].
def adjoint(A, adj):

	if (N == 1):
		adj[0][0] = 1
		return

	# temp is used to store cofactors of A[][]
	sign = 1
	temp = [] # To store cofactors
	for i in range(N):
		temp.append([None for _ in range(N)])

	for i in range(N):
		for j in range(N):
			# Get cofactor of A[i][j]
			getCofactor(A, temp, i, j, N)

			# sign of adj[j][i] positive if sum of row
			# and column indexes is even.
			sign = [1, -1][(i + j) % 2]

			# Interchanging rows and columns to get the
			# transpose of the cofactor matrix
			adj[j][i] = (sign)*(determinant(temp, N-1))


# Function to calculate and store inverse, returns false if
# matrix is singular
def inverse(A, inverse):

	# Find determinant of A[][]
	det = determinant(A, N)
	if (det == 0):
		print("Singular matrix, can't find its inverse")
		return False

	# Find adjoint
	adj = []
	for i in range(N):
		adj.append([None for _ in range(N)])
	adjoint(A, adj)

	# Find Inverse using formula "inverse(A) = adj(A)/det(A)"
	for i in range(N):
		for j in range(N):
			inverse[i][j] = adj[i][j] / det

	return True


# Generic function to display the
# matrix. We use it to display
# both adjoin and inverse. adjoin
# is integer matrix and inverse
# is a float.
def display(A):
	for i in range(N):
		for j in range(N):
			print(A[i][j], end=" ")
		print()


def displays(A):
	for i in range(N):
		for j in range(N):
			print(round(A[i][j], 6), end=" ")
		print()


# Driver program

A = [[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]]
adj = [None for _ in range(N)]
inv = [None for _ in range(N)]

for i in range(N):
	adj[i] = [None for _ in range(N)]
	inv[i] = [None for _ in range(N)]


print("Input matrix is :")
display(A)

"""
print("\nThe Adjoint is :")
adjoint(A, adj)
display(adj)
"""
print("\nThe Inverse is :")
if (inverse(A, inv)):
	displays(inv)

# This code is contributed by phasing17

