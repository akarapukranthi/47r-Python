#basic python function program on power
def power(a,b):
  print(a**b)
power(5,6)


#function to print odd nunmbers for 1 to 10
def odd():
  for i in range(1,21):
    if i%2!=0:
      print(i)
odd()


#Function to find the factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))


#print the palindrome using slicing the string
word="markram"
if(word==word[::-1]):
  print("palindrome")
else:
  print("not palindrome")



#print the sub-str value is present in the string
word="tfhjmahi"
sub_str="mahi"
for i in range(len(word)):
  part=word[i:i+4]
  print(part)
  if part==sub_str:
    print(sub_str,"is part of",word)
    break


print the palindrome which is present in the string or character
sentence="my mom makes the lunch and anna drops me"
sentence=sentence.split()
palindrome_exixts=False
for i in range(len(sentence)):
  word=sentence[i]
  if word==word[::-1]:
    print(word,"is palindrome")
    palindrome_exixts=True
if not palindrome_exixts:
  print("no palindrome found")



#print fibanocci series from first 10 numbers
a=0
b=1
for i in range(10):
  print(a)
  c=a+b
  a=b
  b=c



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


#print prime numbers from which is nearest position
num=30
next_prime=0
while prime_not_found=True:
  num+=1
  factors=0
  for i in range(1,num+1):
    if num%i==0:
      factors+=1
      break
   if factors==2:
    print("next prime number is",num)
    prime_not_found=False

num=25
prev_prime=0
for i in range(num-1,1,-1):
  factors=0
  for j in range(2,j):
    if i%j==0:
      factors+=1
      break
  if factors==2:
    print("previous prime number is",i)
    break



print(next_prime,prev_prime,num)

if(num-prev_prime) < (next_prime-num):
  print(prev_prime,"is the nearest number")
elif(next_prime-num) < (num-pre_prime):
  print(next_prime,"is the nearest number")
else:
  print("both are equal")



#print the anagrams of two strings
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