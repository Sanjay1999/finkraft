def ps(l1,t1):
	for i in range(len(l1)-1):
		for j in range(i+1,len(l1)):
			if l1[i]+l1[j]==t1:
				return(l1[i]+l1[j])

ps([3,1,2,6,5,4],7)