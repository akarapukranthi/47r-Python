
# name="rakesh"
# print(name)

# name="rakesh"
# first_char=name[0]
# print(first_char)

# name="rakesh"
# last_char=name[-1]
# print(last_char)

# name1="hello"
# name2="world"
# print(str(name1)+' '+str(name2))


# name="kranthi"
# print((name+" ")*3)


# name="kranthi"
# print(name[:5])

# name="kranthi"
# print(name[::-1])

# name1 = "kranthi is good boy"
# name2 = "kranthi"
# if name1 in name2:
#       print("substring is exist")
# else:
#       print("substring is not exist")


# name="kranthi"
# print(len(name))

# name="kranthi"
# name=name.upper()
# print(name)


# name="KRANTHI"
# name=name.lower()
# print(name)

# name="kranthi"
# name=name.capitalize()
# print(name)

# name="kranthi kumar"
# name=name.title()
# print(name)

# name="        kranthi          "
# name=name.lstrip()
# print(name)




# name="        kranthi          "
# name=name.rstrip()
# print(name)

#Write a while loop to reverse a number
# num=1234
# rev=0
# while num > 0:
#     num1 = num % 10
#     rev=rev*10+num1
#     num//=10
# print("Reversed number :",rev)




# name="        kranthi          "
# name=name.strip()
# print(len(name),name)


name="kranthi"
name1=name.split()
print(name1)

#string methods
username="    python programming"
print(username.upper())
print(username.lower())
print(username.title())
print(username.capitalize())
print(username.strip())
print(username.lstrip())


#print whether the string in upper or lower case
char=input("enter the char:")
if char==char.upper():
  print("char is in upper case")
else:
  print("char is in lower case")


#print the string which are vowels and in even position of the string
sentence="iam learning python"
for i in range(len(sentence)):
  c=sentence[i]
  if (c=="a" or c=="e" or c=="o" or c=="i" or c=="u") and (i%2==0):
    print(c,i)


#strings methods
name="python"
print(name.startswith("p"))     #startswith is a method which starts with given character or not

name="python"
print(name.endswith("n"))       #endswith is a method which ends with given character or not

name="python@1"
print(name.isalpha())          #isalpha is a method string is in only character

name = "123456987"
print(name.isdigit())         #isdigit is a method which string is only in numbers

name="python123"
print(name.isalnum())        #isalnum is method which the string can be characters and numbers


#which convert the lower to upper or upper to lower given by the character condition
name="python"
for i in range(len(name)):
  if name[i]==name[i].upper():
    print(name[i].lower())
  else:
    print(name[i].upper())


#zfill method
name="panduranga"
length=15
req=length-len(name)
new_str=" "
for i in range(req):
  new_str+="0"
print(new_str+name)


#splict string which is used to seperate the words in sentence
word="i woke up,i went to class"
print(word.split())


#join method used to join the seperate words into sentence
word=['i', 'woke', 'up','i', 'went', 'to', 'class']
print(" ".join(word))