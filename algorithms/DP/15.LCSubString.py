def LCs (x , y) :
	global X,Y,dp
	for i in range (x+1) :
		for j in range (y+1) :
			if (i == 0) or (j == 0) :
				dp[i][j] = 0
			else :
				if (X[i-1] == Y[j-1]) :
					dp[i][j] = 1 + dp[i-1][j-1]
				else :
					dp[i][j] = 0
	return max ([max(i) for i in dp])
X = input()
Y = input()
x = X.__len__()
y = Y.__len__()
dp = [[0 for i in range (y+1)]for j in range(x+1)]
print(LCs(x,y))
