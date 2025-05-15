def is_pali(s):
    
    s = s.lower()
    # keep only alphanumeric characters
    new = ''.join(char for char in s if char.isalnum())
   # check alphobets with its reverse
    return new == new[::-1]


input_str = input("enter string to check  palindrome: ")

if is_pali(input_str):
    print("palindrome.")
else:
    print("not palindrome.")


