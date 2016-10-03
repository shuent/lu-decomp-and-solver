import numpy as np
import copy

def lu_decomp(mtrx):
	if len(mtrx)!=len(mtrx[0]):
			raise NameError("this is not N dimention matrix")
	mtrx = copy.copy(mtrx)
	l=[]
	u=[]
	dim = len(mtrx)
	try:
		# fill taikaku with 1 rest 0
		for i in range(dim):
			temp = []
			al0 = []
			for j in range(dim):
				al0.append(0.0)
				if i == j:
					temp.append(1.0)
				else:
					temp.append(0.0)
			l.append(temp)
			u.append(al0)
		
		# lu decomp algorithm
		for i in range(dim):
			# 対角が0にならない処理
			# if mtrx[i][j] < maxcol:
			# 	mtrx[i] = mtrx[index of maxcol]
			maxcol = mtrx[i][i]
			for k in range(i,dim):
				if maxcol < mtrx[k][i]:
					maxcol = mtrx[k][i] 
					mtrx[k],mtrx[i] = mtrx[i],mtrx[k]

			for j in range(dim):
				if i > j:
					sum1=0
					for k in range(j):
						sum1 += l[i][k]*u[k][j]
					l[i][j]=((mtrx[i][j]-sum1)/u[j][j])
				else:
					sum2=0
					for k in range(i):
						sum2 += l[i][k]*u[k][j]
					u[i][j]=((mtrx[i][j]-sum2))
	except ZeroDivisionError:
		return "zero division error"
	else:
		return l,u
	
def lu_solver(l,u,b):
	dim = len(l)
	# 1. L forward substitution
	y = np.zeros(dim)
	sum1=0
	for i in range(dim):
		for k in range(i):
			sum1 += l[i][k]*y[k]  
		y[i] = b[i] - sum1
	
	# 2. U backward substitution
	x = np.zeros(dim)
	for i in range(dim):
		x[i] = y[i]
	for i in reversed(range(dim)):
		sum1 = 0
		for j in range(i+1,dim):
			sum1 = u[i][j]*x[j]
		x[i]=(y[i]-sum1) / u[i][i]

	return x

def solve(mtrx,b):
	try:
		l,u = lu_decomp(mtrx)
		return lu_solver(l,u,b)
	except NameError:
		return "could not solved"

		



def main():
	# matrix
	a1=[[3,4,5],[0,5,2],[2,5,7]]
	a2=[[0,2],[3,4]]
	a3=[[0,2,2],[3,4,2]]

	# vector
	b= [1,2]
	b1=[5,7,1]


	# test

	print(solve(a1,b1))
	print(solve(a2,b))
	print(solve(a3,b))
	print(solve(a1,b1))

	

if __name__ == '__main__':
	main()