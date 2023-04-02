# Types of conditions
a = int(input("Please Enter age : "))
b = int(input("Please Enter Frend age : "))

if (a > b):
    print(f"{a} > {b}")
elif (a < b):
    print(f"{b} > {a}")
else:
    print(f"{a} == {b}")

# Example (false)
a = input("Enter a value for input1: ")
b = input("Enter a value for input2: ")
c = input("Enter a value for input3: ")
d = input("Enter a value for input4: ")
if (a > b):
    print(f"{a} > {b}")
elif (a < b):
    print(f"{b} > {a}")
else:
    print(f"{a} == {b}")