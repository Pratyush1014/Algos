def SubsetSum (N , s) :
	global wt 
	dp = [[False for i in range (s+1)] for i in range (N + 1)]
	for i in range (N + 1) :
		for j in range (s + 1) :
			if (i == 0) : 
				dp [i][j] = False
			if (j == 0) :
				dp [i][j] = True
			else :
				dp [i][j] = dp[i-1][j] or dp[i-1][j - wt[i-1]]	
		
	print(dp[-1][-1])
N = int (input())

wt = list(map(int ,input().split()))
s = int(input())

SubsetSum(N , s)
