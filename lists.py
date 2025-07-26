Objects = ["mani",26,"not enough","hyd",500072]
print(Objects[0])


#append
num=[1,2,3,4,5,6,7,8,9,10]
num.append(11)
print(num)         #[1,2,3,4,5,6,7,8,9,10,11]
num=[1,2,3,4,5,6,7,8,9,10]
num.append(12)
num.append((12,13,15))
print(num)         #[1,2,3,4,5,6,7,8,9,10,11,12,(13,14,15)]

#extend
l1=[1,2,3]
l2=[4,5,6]
l1.extend(l2)
print(l1)        #[1,2,3,4,5,6]

#insert
num=[1,2,5,6]
num.insert(2,4)
print(num)     #[1, 2, 4, 5, 6]

#remove(item)
lang=["java","JS","CSS","Python"]
lang.remove("CSS")
print(lang)            #lang=["java","JS","Python"]

#clear
lang=["java","JS","CSS","Python"]
lang.clear()
print(lang)           #[]

#reverse
animals=["cat","dog","lion","tiger","frog"]
animals.reverse()
print(animals)         #['frog','tiger','lion','dog','cat']

#sort
num=[1,3,4,8,9,2,6,5]
num.sort()
print(num)            #[1,2,3,4,5,6,7,8,9]

animals=["cat","dog","lion","tiger","frog"]
animals.sort()
print(animals)         #['cat','dog','frog','lion','tiger']


#count
animals=["cat","dog","lion","tiger","frog"]
time=animals.count("cat")
print(time)         #1
time=animals.count("c")
print(time)         #0

#index
animals=["cat","dog","lion","tiger","frog"]
time=animals.index("cat")
print(time)         #0
animals=["cat","dog","lion","tiger","frog"]
time=animals.count("tiger")
print(time)         #3

#copy
color=["green","red","white","blue","black"]
copied=color.copy()
print(copied)     #["green","red","white","blue","black"]
copied.append("aqua")
print(copied)     #["green","red","white","blue","black","aqua"]

#sum
num=[1,2,3,4,5,6]
num1=sum(num)
print(num1)   #21

#max
num=[1,2,3,4,5,6]
highest=max(num)
print(highest)      #6
num=[1,2,3,4,5,6,17,78,18,90]
highest=max(num)
print(highest)      #90

num=[1,2,3,4,5,6,7,8,9]
highest=max(num)
num.remove(highest) 
sec_highest=max(num)
print(sec_highest     #8
      
      )
#min
num=[1,2,3,4,5,6]
smallest=min(num)
print(smallestest)   #1
num=[1,2,3,4,5,-1,-10,-12]
smallestest=max(num)
print(smallestest)     #-1
 





 #def the function  method by using 3rd highest position
 num=[2,5,9,11,13,56,92,74,128,512,256]
pos=3
def find_highest(li,n):
 if len(li)<n:
  return "not possible"
 else:
  for i in range(n):
   li.remove(max(li))
  return max(li)

print(find_highest(num,pos))     #128


#print the list to remove duplicates and find position in list
num=[9,6,7,8,7,8,6,12]
unq_num=[]
for i in num:
 if i not in unq_num:
  unq_num.append(i)
print(unq_num)    #[9,6,7,8,12]


#print the list to find the highest value without methods
num=[256,256,256,104,108,100,2000,10000]
temp=0
for i in num:
 if i>temp:
  temp=i
print(temp)    #10000


#print the list to find sum of an elements
num=[1,2,3,4,5,6]
temp=0
for i in num:
 temp+=1
print(temp)   #21


#print the list to return the index value
food=["biryani","pizza","rice","manchuria","momo","fish"]
val="momo"
for i in range(len(food)):
 if food[i]==val:
  print({f"{val} is present in {i+1} position"})
  break                                           #{'momo is present in 5 position'}
 


 #print the list to return the count value
 food=["biryani","pizza","rice","manchuria","momo","fish","momo"]
 count=0
 item="momo"
 for i in food:
  if i==item:
   count+= 1                                #momo is present 2 times
print(f"{item} is present {count} times")
         


#print the list to return the given list is in reverse order
movie=["salaar","kgf","og","akanda","dil"]
rev=[]
for i in range(len(movie)-1,-1,-1):
 rev.append(movie(i))
print(rev)     #['dil','akanda','og','kgf','salaar']


#print the given list into seperate list according to numbers or uppercase or lowercase
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


