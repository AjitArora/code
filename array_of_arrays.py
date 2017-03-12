def solve(arr, size, p, l, item, ans):
	if item:
		l.append(item)
	if p == size:
		ans.append(l)
		return ans
	for a in arr[p]:
		solve(arr, size, p+1, l, a, ans)
	return ans

arr=[[1, 2, 3], [4], [5, 6]]
r = solve(arr, len(arr), 0, [], None, [])
print r


