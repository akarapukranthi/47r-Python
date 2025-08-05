#Callbacks functions
#a function passed as a parameter for another function
#or used inside a function

def goodevening():
    print("good evening")
def goodafternoon(fun):
    print("good afternoon")
    fun()
goodafternoon(goodevening)

#output:    
#goodafternoon
#goodevening

#HOF-Higher Order Function
#which takes a parameter in another function/returns another function

username="pythonprogramming"
password="python"
login=lambda u,p:username==u and password==p
def show_reels():
    if login("pythonprogramming","python"):
        print("show reels")
    else:
        print("login first")

show_reels()

#map
#track the iteration of function(perform on operation)
res=map(lambda x:x*x,[1,2,3,4,5])
print(list(res))

#output : [1, 4, 9, 16, 25]

res=map(lambda x:x%2==0,[1,2,3,4,5])
print(list(res))

#output : [False, True, False, True, False]

res=map(lambda x:x%2==1,[1,2,3,4,5])
print(list(res))

#output : [True, False, True, False, True]


#filter
#filters elements from an iterable based on a condition

res=filter(lambda x:x*x,[1,2,3,4,5])
print(list(res))

#output : [1, 2, 3, 4, 5]

res=filter(lambda x:x%2==0,[1,2,3,4,5])
print(list(res))

#output : [2,4]


names=["bhagrav","bhavani","jyothi","shiv","nani"]
res=filter(lambda n:len(n)==4,names)
print(list(res))
res=map(lambda n:len(n)==4,names)
print(list(res))
upper_case=map(lambda s:s.upper(),names)
print(list(upper_case))

#outputs:
# ['shiv', 'nani']
# [False, False, False, True, True]
# ['BHAGRAV', 'BHAVANI', 'JYOTHI', 'SHIV', 'NANI']