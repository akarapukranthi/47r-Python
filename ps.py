# #print the anagrams of two strings
s1="live"
s2="evil"
if len(s1)!=len(s2):
  print(s1,s2,"is not a anagram")
else:
  is_anagram=True
  for i in s1:
    if s1.count(i)!=s2.count(i):
      is_anagram=False
      break
  if is_anagram:
    print(s1,s2,"is a anagram")
  else:
    print(s1,s2,"is not a anagram")




#prime numbers
num=71
factors=0
for i in range(1,num+1):
  if num%i==0:
    factors+=1
if factors==2:
  print(num,"prime number")
else:
  print(num,"not prime number")



#Amstrong Number
num=153
num2=num
num3=num
count=0
while num2!=0:
  num=num//10
  count+=1
total=0
while num2!=0:
  last_digit=num1%10
  total=total+(last_digit**count)
  num2=num2//10
if total==num3:
  print("amstrong")
else:
  print("not amstrong")