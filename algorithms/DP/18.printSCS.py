def printSCS (x , y) :
	global X , Y ,dp
	for i in range (x + 1) :
		for j in range (y + 1) :
			if (i == 0) or ( j == 0 ) :
				dp[i][j] = 0
			else :
				if (X[i-1] == Y[j-1]) :
					dp[i][j] = 1 + dp[i-1][j-1]
				else :
					a = dp[i-1][j]
					b = dp[i][j-1]
					if (a > b) :
						dp[i][j] = a
					else :
						dp[i][j] = b
	i = x-1
	j = y-1
	l = []
	while (j >= 0)and(i >= 0) :
		if (X[i] == Y[j]) :
			l.append(X[i])
			i -= 1
			j -= 1
		else :
			a = dp[i+1][j]	
			b = dp[i][j+1]
			if (a > b) :
				l.append(Y[j])
				j -= 1
				continue
			else :
				l.append(X[i])
				i -= 1
				continue
	l.reverse()
	print("".join(l))			
		

X = input()
Y = input()
x = X.__len__()
y = Y.__len__()
dp = [[0 for i in range (y+1)] for j in range (x+1)]
printSCS(x,y)
