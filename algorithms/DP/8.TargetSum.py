def SubsetSum (N , s) :
	global arr , dp
	for i in range (N + 1) :
		for j in range(s + 1) :
			if  (j == 0 ) :
				dp[i][j] = 1
			elif (i == 0) and (j != 0) :
				dp[i][j] = 0
			else :
				dp[i][j] = dp[i-1][j] + dp[i-1][j - arr[i-1]]

def Count(T) :
	global dp,s
	for i in range (s//2 + 1) :
		if (s - 2*i == T) :
			print(dp[-1][i])
			break
	else :
		print(0)


N = int(input("Enter size : "))
arr = list(map(int , input().split()))
T = int(input("TargetSum : "))
s = sum(arr)
dp = [[0 for i in range (s//2 + 1)] for j in range(N+1)]
SubsetSum(N,s//2)
Count(T)
