def reverse(s):
    for char in s:
        reverse_str=char+reverse_str
        return reverse_str
    text=input("enter a string")
    print(f"{reverse(text)}")
