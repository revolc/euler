import math
def is_prime(n):
	if (n == 2):
		return True
	i = 2
	while i <= math.sqrt(n):
		if n % i == 0:
			return False
		i += 1
	return True

def solve():
	order = 0
	num = 2
	N = 10001
	while order < N:
		#print num, order
		if is_prime(num):
			order += 1
			if (order == N):
				print N,"th: ", num
				break
		num += 1
