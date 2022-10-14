
def prime(start,end):
    for num in range (start,end+1):
    #start end is the range of given numbers
        if start>1 : 
   ''' A prime number is a whole number greater than 1 whose only factors are
   1 and itself.'''     
            for i in range(2,num):
                if num%i==0:
                    break
            else:
                print(num)
        else:print('error -1')       
prime(0,5)
