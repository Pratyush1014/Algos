def subsetsum(N,s) :
	global dp , arr
	for i in range (N + 1) :
		for j in range (s + 1) :
			if (j == 0) :
				dp[i][j] == 1
			elif (i == 0) and (j != 0):
				dp [i][j] == 0
			else :
				if (arr[i-1] > j) :
					dp[i][j] = dp[i-1][j]
				else :
					dp[i][j] = dp[i-1][j - arr[i-1]] or dp[i-1][j]

def MinimumDiff () :
	global dp , arr
	d = 0
	for i in range(sum(arr)//2 + 1) :
		if (dp[N][i]) :
			d = max(d,i)
	print(sum(arr) - 2*d)

N = int(input())
arr = list(map(int , input().split()))
dp = [[-1 for i in range (sum(arr)//2+1)] for j in range (N+1) ]
subsetsum(N , sum(arr)//2)
MinimumDiff()
