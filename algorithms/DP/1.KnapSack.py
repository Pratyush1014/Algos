def Knapsack (val , wt , N , w) :
	global  dp
	if ( w == 0 ) or (N == 0) :
		return 0 
	if (wt[N-1] <= w) :
		if (dp[N][w] != -1 ) :
			return dp[N][w]
		else :
			a = val[N-1] + Knapsack(val , wt , N-1 , w - wt[N-1])
			b = Knapsack(val , wt , N-1 , w) 
	
			dp[N][w] = max(a,b)
			return max(a,b)
	elif (wt[N-1] > w) :
		dp[N][w] = Knapsack(val , wt , N-1 , w)
		return dp[N][w]

N = int(input())
val = list(map(int , input().split()))
wt = list(map(int , input().split()))
w = int(input())

dp = [[-1 for i in range (w + 1)] for j in range (N + 1)]

profit = Knapsack(val , wt , N , w)

print(profit)
