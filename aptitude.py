def average(*n):
	if len(n)==0:
		return "pass arguments"
	else:
		print("average is :",sum(n)/len(n))
		return sum(n)/len(n)


	
def add(*n):
	if len(n)==0:
		return "pass arguments"
	else:
		print("total addition is:",sum(n))
		return sum(n)
		
		
def speed(distance,time):
	if time==0:
		print('invalid')
		return 'invalid'
	else:
		print("speed  is ",distance/time,"kmph" )
		return distance/time

def distance(speed,time):
	if time==0 or speed==0:
		print(0)
		return 0
	else:
		print("distance is ",speed*time,"km")
		return speed*time
def time(distance,speed):
	if speed==0 :
		print('invalid')
		return 0
	else:
		print("time  is ",distance/speed,"hrs" )
		return distance/speed 
		
