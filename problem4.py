def is_palindromic(str):
	for i in range(0, len(str)/2):
		if (str[i] != str[len(str) - 1 - i]):
			return False
	return True

def solution():
	result=0
	for i in range (100, 1000):
		for j in range (i, 1000):
			tmp = i * j
			if is_palindromic(repr(tmp)):
				if result == 0 or tmp > result:
					#print i,j, tmp
					result = i*j
	print result
