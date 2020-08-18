def CountSubsets (N , s) :
	global arr,dp
	if (dp[N][s] != -1) :
		return dp[N][s]
	if (s == 0) :
		return 1
	elif (s != 0 ) and (N == 0) :
		return 0
	elif (s != 0) and (N != 0) :
		if (arr[N-1] <= s) :  
			dp[N][s] =  CountSubsets (N-1 , s) + CountSubsets (N-1 , s - arr[N-1])
		else :
			dp[N][s] = CountSubsets (N-1 , s) 
		return dp[N][s]
N = int(input())
arr = list(map(int , input().split()))
s = int(input())
dp = [[-1 for i in range (s+1)] for j in range(N+1)]

print(CountSubsets(N,s))
