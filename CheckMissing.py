import os

Src = "/home/lx/Continue"
list = os.listdir(Src)
list.sort()


#count =0
#count2 =0
n =len(list)

for ded in list:
	temp = Src +"/"+ ded
	

	numbers = []
	for word in ded.split():		
		if word.isdigit():
			#numbers.append(int(word))
			ww=int(word)
			print(ww)
	
	listt = os.listdir(temp)
	listt.sort()
	#print (listt)
	
	num = []
	for no in listt:
		filename, file_extension = os.path.splitext(no)
		num.append(int(filename))
	num.sort()
	#print(num)
	
	#count =0
	filename, file_extension = os.path.splitext(listt[0])
	count = int(filename)
	for x in listt:
		
		#print (x)
		#print (temp)
		
		#sorc=temp +"/"+ x
		
		
		#filename, file_extension = os.path.splitext(sorc)
		filename, file_extension = os.path.splitext(x)
		#print (file_extension)
		#print (filename.zfill(3))
		count2 = int(filename)
		#dest=temp +"/"+ str(ww).zfill(5) +"-"+ filename.zfill(3) +" ("+ ded +")"+ file_extension
		
		#print(count)
		#print(count2)
		count = count +1
		
		#os.rename(sorc, dest) 
		
		
print ("done")
