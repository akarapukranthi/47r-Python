name="rakesh"
print(name)

#print fibanocci series from first 10 numbers
a=0
b=1
for i in range(10):
  print(a)
  c=a+b
  a=b
  b=c



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