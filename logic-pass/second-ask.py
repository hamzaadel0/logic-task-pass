def prime(start,end):
    for num in range (start,end+1):
    #start end is the range of given numbers
        if start>1 : 
      
            for i in range(2,num):
                if num%i==0:
                    break
            else:
                print(num)
        else: 
            return print('error -1')       
prime(0,5)
