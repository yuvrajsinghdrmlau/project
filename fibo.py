list1 = []
N = int(input("Enter Number oF Fibonacci Series do you want: "))
for i in range(N):
    if i == 0:
        list1.append(0)
    elif i == 1 :
        list1.append(1)
        
    else:
        x = list1[i-1]+ list1[i -2]
        list1.append(x)
                                               
print(list1)
    
        


        
