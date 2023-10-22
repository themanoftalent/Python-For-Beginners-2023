def bubbleSort(listem):
	for passnum in range(len(listem)-1,0,-1):
		#print( passnum)
		for i in range(passnum):
			if listem[i]>listem[i+1]:
				temp = listem[i]
				listem[i] = listem[i+1]
				listem[i+1] = temp
listem = [54,26,93,17,77,31,44,55,20,4,5,7,22,87,45,8,345,100]
bubbleSort(listem)
print(listem)
