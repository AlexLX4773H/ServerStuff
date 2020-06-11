import os

Src = "/home/lx/Continue"
list = os.listdir(Src)
list.sort()


#count =0
#count2 =0
n =len(list)

for ded in list:
	temp = Src +"/"+ ded
	listt = os.listdir(temp)
	listt.sort()
	#print (listt)

	#numbers = []
	for word in ded.split():		
		if word.isdigit():
			#numbers.append(int(word))
			ww=float(word)
			#print(numbers)
			#print (str(ww).zfill(5))
	
	#count =0
	for x in listt:
		
		#print (x)
		#print (temp)
		
		sorc=temp +"/"+ x
		
		
		#filename, file_extension = os.path.splitext(sorc)
		filename, file_extension = os.path.splitext(x)
		#print (file_extension)
		#print (filename.zfill(3))
		
		dest=temp +"/"+ str(ww).zfill(5) +"-"+ filename.zfill(3) +" ("+ ded +")"+ file_extension
		#count = count +1
		
		os.rename(sorc, dest) 
		
print ("done")
