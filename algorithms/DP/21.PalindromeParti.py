def isPalindrome(s,i,j) :
	d = [i for i in s[i:j+1]]
	d.reverse()
	d = ''.join(d)
	if (d == s) :
		return True
	else :
		return False
def PP (i , j) :
	global s
	if (i >= j) :
		return 0
	else :
		if (isPalindrome(s,i,j)) :
			return 0
		else :
			minimum = float('inf')
			for k in range (i,j) :
				c = PP(i,k) + PP(k+1,j) + 1
				if (c < minimum) :
					minimum = c
			return minimum	
N = int(input())
s = input()
c = PP(0,N-1)
print(c)
