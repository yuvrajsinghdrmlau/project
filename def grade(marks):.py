# Grade calculator by Yuvraj Singh.

def grade(marks):

    if marks >= 50:
        if marks >= 90:
             print("grade a")
        elif marks >= 70:
             if marks >= 80:
                  print(" grade b++")
             else :
                  print(" grade b")
                  
   
        else:
             print(" grade c")

    
    
    else:
            print(" grade fail")
            
            
            
marks = int(input("enter the number : "))

grade(marks)
