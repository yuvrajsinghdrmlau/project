def grade(marks):
    if marks >= 50:
        if marks >= 60:
            
            if  marks >= 70:
                 
                 if marks >= 80:
                    
                    if marks >= 90:
                        print("Grade a")
                 print("Grade b")
            print("Grade c")
        print("Grade d")
    else:
        print("Fail")

marks = int(input("Enter the marks: "))
grade(marks)