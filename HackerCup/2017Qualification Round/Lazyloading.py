import sys

def get_ans(arr):
	arr.sort()
	ans =0
	#print arr
	while True:
		if not arr:
			break
		tsum = arr.pop(-1)
		ans +=1
		#print ans
		if not arr:
			break
		length = len(arr)
		if tsum < 50:
			last_check = 0
			for x in range(0, length):
				last_check = x
				tsum += arr[x]
				if tsum >=50:
					break

			i = 0
			while(i<length):
				if (tsum-arr[i]) >=50:
					tsum-=arr[i]
					i+=1
				else:
					break
			#print arr, i, last_check
			for y in xrange(i, last_check+1):
				arr.pop(i)
			#print arr
	return ans



def lazyloading():
	fin = open("lazy_loading.txt", "r")
	T = int(fin.readline())
	x = 1
	while(x<=T):
		N = int(fin.readline())
		arr = []
		while(N != 0):
			arr.append(int(fin.readline()))
			N-=1
		ret = get_ans(arr)
		print "Case #%s: %s"%(x, ret)
		x+=1

if __name__ == '__main__':
	lazyloading()