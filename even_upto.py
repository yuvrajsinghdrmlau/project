def even_num():
    n = int(input("Enter the number to print number upto: "))
    
    for i in range(1,n):
        if i % 2 == 0:
            print(i)
            
            
even_num()