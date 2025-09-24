#------------------ Generators ------------------
# generator is a fucntion uses "yield " keyword instead of "return"
# it supports iterator and return generator iterator by calling "yield"
# By using next() it resume from where it called "yield" not from beginning 
# when called its not start automatically from beginning it start from where it left off
# its only gives u control 
# --------------------------------------------------
def my_generator():
    yield 1
    yield 2
    yield 3 
    yield 4

# print(my_generator()) # <generator object my_generator at 0x0000023C5
print(my_generator())
mygen = my_generator()
#print(next(mygen)) # 1
#print(next(mygen)) # 2
#print(next(mygen)) # 3
#print(next(mygen)) # 4
for number in mygen : 
    print(number)


#-------------------------------- Decorators ------------------------------
# sometimes called meta programmming 
# everything in python is an object even fucntions 
# Decorator takes a function and add some fucnctionability and return it 
# decorator wrap other fucntion and enhance their web behaviour 
# decorator is a higher order function ( fucntion acceptes a fucntion as a parameter )
#--------------------------------------------------------------------------
def myDecorator(func) : # decorator
    
    def nestedfunc() : # pick any name for this fucntion its just fofr decoration 
         print("before")
         func() # execute function 
         print("after")
    
    return nestedfunc # return all data 

def hellowrodl() :
    print("hello wrold from the hellowrodl fucntion")

afterdecoration = myDecorator(hellowrodl)
afterdecoration()
# a better way to write this code 
# ------------------ Sugar Synthax in Decorators ----------------------
@myDecorator
def hellowrodl() :
    print("hello wrold from the hellowrodl fucntion")
hellowrodl()

# use can use parameters in the nested fucntion for example to add a+b we use a and b 
# we can use two decorators @mydecorate1 @mydecorate2 
# it execute the content of the first decorator and then the second decorator then the function

# Speed Test with Decorators
# this another idea not speed test  
def mydecroration (func) :
    def wrapper(*numbers) : # like this u got unlimited number of arguments
        for number in numbers : 
            if number <10 : 
                print("danger less than 10")
    
        func(* numbers)
    return wrapper

@mydecroration
def add(a,b) :
    print(a+b)

add(30,20)

# ----------- speed test with decorations -------------------
def speedtest(func) : 
    def wrapper(a,b) :
        import time
        start = time.time()
        func(a,b)
        end = time.time()
        print(f"the function run time : {end - start}")
    return wrapper

@speedtest
def multi(a,b) : 
    for i in range(1,5000) : 
        pass
    print(a*b)

multi(3,1)

# -------------------------- Loop on many iterators using ZIP ------------
list1 = [ 1,2,3,4,5,6]
list2 = ["A","B"]
ultimatelist = zip(list1, list2)
print(ultimatelist)
for item in ultimatelist :
    print(item)

for item1, item2 in zip(list1,list2) :
    print(f"here {item1} ,{item2}")
# zip picks the length of the samller one and works with it 
# zip can merge more than two elements 










