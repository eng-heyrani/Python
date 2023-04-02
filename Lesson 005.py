# A variety of string capabilities

s = """Hello World
Plase Enter Name : """
print(s)
print(s[0:5])
print(s[0:5:2])
print(s[::2])
print(s[::-2])
print(s.upper())
print(s.lower())


print("hello" + "world")
print("hello" +  " " + "world")


age = int(input("Please Enter Age : "))
# print("i am" + age + "yers old") ===> (false)
print("i am {} years old".format(age))
print(f"i am {age} years old")
print("i am %d years old"% age)

a = "Alireza Heyrani"
print(a.replace('h','A',2))