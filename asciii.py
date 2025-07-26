#ascii values is an represtation of charactes into numeric codes
print(ord("S"))
print(ord("m"))
print(ord("a"))
print(ord("9"))



#print the given character is in lower case or not
char="u"
asc_code=ord(char)
if asc_code>=97 and asc_code<=122:
  print("lower case")
else:
  print("not lower case")



  #print the ascii value is in lower or upper or alphabets
char="Z"
asc_code=ord(char)
if asc_code>=97 and asc_code<=122:
  print("lower case")
elif asc_code>=65 and asc_code<=90:
  print("upper case")
else:
  print("not alphabet")



  #to find how many uppercase or lowercase charcaters in a string
sentence="ChiittII"
upper_code=0
for i in range(len(sentence)):
  code=ord(sentence[i])
  if code>=65 and code<=90:
               upper_code += 1
print("there are",upper_code,"uppercase characters")



#print the string name next letter and create a new string according
name="chitti"
secret=" "
for i in range(len(name)):
  code=ord(name[i])
  new_char=chr(code+1)
  secret+=new_char
print(secret)



#print the sum of all ascii values in the string
name ="chitti"
total=0
for i in range(len(name)):
  total+=ord(name[i])
print(total)




#print the letters seperated by uppercase or lowercase or number sums
char=[1,"A","B","C",2,"a","z","b"]
Upper=[]
Lower=[]
sum=0
for i in char:
 s=str(i)
 ascii=ord(s)
 if ascii>=65 and ascii<=90:
  Upper.append(s)
 elif ascii<=97 and ascii<=122:
  Lower.append(s)
 else:
  sum+=int(s)

c="".join(Upper)
l="".join(Lower)


