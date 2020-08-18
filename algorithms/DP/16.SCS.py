def SCS (x,y) :
	global X , Y
	for i in range (x + 1) :
		for j in range (y + 1) :
			if (i == 0) or (j == 0) :
				dp[i][j] = 0
			if (X[i-1] == Y[j-1]) :
				dp[i][j] = 1 + dp[i-1][j-1]
			else :
				dp[i][j] = max (dp[i-1][j] , dp[i][j-1])
	return x + y - dp[-1][-1]

X = input()
Y = input()
x = X.__len__()
y = Y.__len__()
dp = [[ 0 for i in range (y+1)] for j in range (x+1)]
print(SCS(x,y))
