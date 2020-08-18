def LCS (x,y) :
	global X,Y
	if (x == 0) or (y == 0) :
		return 0
	else :
		if (X[x-1] == Y[y-1]) :
			return 1 + LCS (x-1,y-1)
		else :
			return max(LCS(x,y-1) , LCS(x-1,y))

X = input()
Y = input()
x = X.__len__()
y = Y.__len__()
print(LCS(x,y))
