def lcs(i,j,count):
	if(i==0 or j==0):
		return count
	if(a[i-1]== b[j-1]):
		count = lcs(i -1,j-1,count +1)
	count = max(count, max(lcs(i,j-1,0),lcs(i-1,j,0))
	return count

if __name__ == "__main__":
	a="abcdxyz"
	b="xyzabcd"
	
	n=len(a)
	m=len(b)
	print(lcs(n,m,0))