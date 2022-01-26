#Question_1
#(a)
#given- take input as 'Python is a case sensitive language'
print("(a)")
input_string=input("Give the statement:")
print(input_string)
length=len(input_string)
print(length)

#Part_(b)
print("(b)")
reverse_string=input_string[length::-1]
print(reverse_string)

#Part_(c)
print("(c)")
new_string=input_string[10:26]
print(new_string)

#Part_(d)
print("(d)")
#replace 'a case sensitive' with 'oject oriented'
replaced_string=input_string[0:10]+'object oriented'+input_string[26:35]
print(replaced_string)

#Part_(e)
print("(e)")
index_a=input_string.find('a')
print(index_a)

#Part_(f) first check the index of white spaces and then write the new string by not using those index
print("(f)")
remove_whitespaces=input_string.replace(" ","")
print(remove_whitespaces)


#Question_2
name="Devesh"
SID=20109009
department_name="PROD"
CGPA="9.9"

print("Hey,%s Here!"%(name))
print("My SID is %d"%(SID))
print("I am from %s department and my CGPA is %s"%(department_name,CGPA))


#Question_3
#a=56 b=10
a=0b111000
b=0b1010

#Part_(a)
print("(a)")
#&
print(bin(a&b))

#Part_(b)
print("(b)")
#|
print(bin(a|b))

#Part_(c)
print("(c)")
#^
print(bin(a^b))

#Part_(d)
print("(d)")
#a<<2 b<<2 ,left shift 2
print(bin(a<<2))
print(bin(b<<2))

#Part_(e)
print("(e)")
#a>>2 b>>4 right shift a with 2 bits and b with 4 bits
print(bin(a>>2))
print(bin(b>>4))


#Question_4
num_1=int(input("Give a number:"))
num_2=int(input("Give a number:"))
num_3=int(input("Give a number:"))

if(num_1>num_2):
    if(num_1>num_3):
        print(num_1,"is greatest number")
    else:
        print(num_3,"is greatest number")
else:
    if(num_2>num_3):
        print(num_2,"is greatest number")
    else:
        print(num_3,"is greatest number")


#Question_5
user_input=input("Give a word:")
if("name"in user_input):
    print("Yes")
else:
    print("No")


#Question_6
side_1=int(input("Give a number:"))
side_2=int(input("Give a number:"))
side_3=int(input("Give a number:"))

if(side_1+side_2>side_3 and side_2+side_3>side_1 and side_1+side_3>side_2):
    print("The triangle is possible")
else:
    print("The triangle is not possible")
