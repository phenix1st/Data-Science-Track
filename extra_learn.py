#---------------------- Numpy Intro -------------------------------
# Numpy is a Python library for numerical computations. It provides support for large, multi-dimensional arrays
# and matrices, along with a wide range of high-performance mathematical functions to operate on these arrays.
#Numpy Stands for numberical python
#Numpy is an open source 
#Numpy supports Dealing with multidimensional arrays and matrices
#Numpy has Many Mathematical Function to deal with htis elements 
#------------------------------------------------------------------
#why we use Numpy aarays 
# consume less memory 
# very fast compared to python list 
# easy to use 
# Support elemnt wise operation
# Element are stored contiguons 
# -----------------------------------------------------------------
# Python Lists
# ---- Homogeneos --> can contains the same type of objects
# ---- Heterogeneos --> can contains different types of objects
#------------------------------------------------------------------
# the items in an array have to be the same type 
# you can be sure whats the storage size needed for the array 
# Numpy Arrays Are Indexed From 0
#------------------------------------------------------------------
# link githyb for nummby https://github.com/numpy/numpy
#------------------------------------------------------------------

import numpy as np
print("My numpy version is:", np.__version__)
#print(dir(np)) # this will al the content of numpy

my_list = [1,2,3,4,5]
my_array = np.array(my_list)
# print(my_list) # [1, 2, 3, 4, 5]
# print(my_array) # [1 2 3 4 5]

print(type(my_list)) # <class 'list'>
print(type(my_array)) # <class 'numpy.ndarray'>

#Accessing elemnts
print(my_array[0] ) # 1
print(my_list[0] ) # 2

a=np.array(10) # 1D array
b = np.array([10,20]) # 1D array with its content 10 20
c = np.array([1, 2] , [3 , 4]) # 2D array with its content 1 2 3 4
d = np.array([[[1,2], [3,4]], [[5,6], [7,8]],]) # 3D array with its content 1 2 3 4 5 6 7 8

print(d[0] ) # [[1 2] [3 4]]
print(d[0][0] ) # [1 2] 
print(d[0][0][0] ) # 1
print(d[1,1,1]) # 8

#Number of dimentsions 
print( a.ndim ) # 1
print( b.ndim ) # 1
print( c.ndim ) # 2
print( d.ndim ) # 3

#Custom of dimensions 

my_custom_array = np.array([1,2,3], ndim = 3) # this is a 3 dimensional array i made the minimum is three 3
print(my_custom_array[0]) # [[1 2 3]]
print(my_custom_array[0][0][0]) # 1
print(my_custom_array.ndim) # 3

# Compare Data Location and Type between lists and arrays
# arrays have the same memory space aalocation when u use id fucntion to a list and an array with the same content but elements in the array
# are stored in the same memory space but the lists elements are not stored in the same memory space
my_list_of_data = [1 , "abi", "jack" , True]
my_array_of_data = [1, "abi" , "jack" , True]
print(my_list_of_data) # [1 , "abi", "jack" , True]
print(my_array_of_data) #['1' "abi"  "jack"  'True']
# in the list took all the types as they are 
# in the array it took all the types as strings because it is the default type of the array

#------------------------------------------------------------
import time
import sys

elements = 150000000000000
my_list2 =  range( 0 , elements)

for n in my_list2 :
    print (n)

my_array1 = np.arange(elements)
my_array2= np.arange ( elements)

list_start = time.time()

# for n1, n2 in zip(my_list2, my_list2):
#    print(n1+n2)

list_result = [ (n1+n2) for n1, n2 in zip(my_list2, my_list2)] # give the same result as the loop 
print(f"list time = {time.time() - list_start} seconds") 

# no the same with  array 
array_time = time.time()
array_result = my_array1 + my_array2 
print(array_result) # give the same result as the others

print(f"array time = {time.time() - array_time} seconds") 

# the excution time of the list is too much bigger than a an array in the array u are too fast than lists

my_array5 = np.range(100) 
print(my_array5.itemsize) # 4 bytes take by each elements
print(my_array5.size) # 100 number of elements
print(f"all Bytes used : {my_array5.itemsize * my_array5.size}") # 400 bytes

my_list3 =range (100)
print(sys.getsizeof(1)) # 28 bytes
print(len(my_list3)) # 100 number of elements

print(f"all Bytes used : {len(my_list3) * sys.getsizeof(1)} ") 

#Slicing arrays 
# slicing => [start:end:steps] not including end 

abc = np.array ["a" , "b" , "c" , "d" , "e" , "f"]
print(abc.ndim)
print(abc[1:4]) 
print (abc[:4])

bcd =np.array [["a" , "b"] , ["c" , "d"] , ["e" , "f"] , ["g" , "h"]]
print(bcd.ndim)
print(bcd[1]) 
print (bcd[0:3]) # the same print (bcd[:3])
print (bcd[:3 , :2]) # the same print (bcd[0:3 , 0:2])

#------------------- Numpy Data Types and Control Array ----------------------------
#'?' boolean
# 'b' sughned byte 
# 'B' unsigned byte
# 'u' unsigned int
# 'i' signed int
# 'f' floating point 
# 'c' complex floating point 
# 'm' timedelta 
# 'M' Datetime 
# 'O' (Pyhton) objects 
# 'S' , 'a' zero terminated bytes (not recommended)
# 'U' unicode string
# 'V' raw data (void) 
# ----------------------------------------------------------------------------------

import  numpy as np

ab = np.array ["a" , "b" , "c" , "d" , "e" , "f"]
#.dtype workd as type for nrml types same work but with the characters we used earlier 
print(ab.dtype) # u1 (unicode string)
print(ab.dtype.kind) # S (string)
 
# create an array with specific data types 
my_arra = np.array([1,2,3] , dtype= "f") # float or f or 'f' or 'float' and this the same with any type 
print(my_arra.dtype) # float32
my_arra = np.array([1,2,3] , dtype= "float")
print(my_arra.dtype) # float64

# changing the types of the array
my_arra = my_arra.astype('float') # float64
print(my_arra.dtype) # float64
# and this way we change the type of the array to any type we want

# Test Capacity 
# for example float64 items size is 8 bytes but float32 is 4 bytes



#----------------------------- Arithmetic & useful Operations ---------------------------------
# Addition 
# Subtraction
# Multiplication
# Division
#---------------------
# Min 
# Max 
# Sum
# Ravel => Returns one falttened arrray 1-dimension  with same type 

jack1 = np.array([1,2,3,4,5])
jack2 = np.array([10,20,30,40,50])
print ( jack1 + jack2 ) # result is [11 22 33 44 55]
print ( jack1 - jack2 ) # result is [-9 -18 -27 -36 -45 ]
print ( jack1 * jack2 ) # result is [ 10  40  90 160 250]
print ( jack1 / jack2 ) # result is [0.1 0.1 0.1 0.1 0.1]

# in 2 dimensional Array we can use the same operations but we need to use the dot function for multiplication
adem =  np.array([[1,2], [3,4]])
adem2 = np.array([[5,6], [7,8]])
print(adem + adem2) # result is [[6 8] [10 12]]
print(adem - adem2) # result is [[-4 -4] [-4 - 4]]
print(adem * adem2) # result is [[ 5 12] [21 32]]
print(adem / adem2) # result is [[0.2 0.33333333] [0.42857143 0.5 ]]
print(np.dot(adem,adem2)) # result is [[19 22] [43 50]] this is the Dot product of two dimensional arrays

# Note : to add or multiply or divide or substract the two arrays should be the same size both of them

# Min Max Sum 
print (jack1.max()) # result is 5
print (jack1.min()) # result is 1
print (jack1.sum()) # result is 15

# Max Min Sum of 2 dimensional array
adem =  np.array([[1,2], [3,4]])
adem2 = np.array([[5,6], [7,8]])
print(adem.max()) # result is 4
print(adem.min()) # result is 1
print(adem.sum()) # result is 10
print(adem2.max()) # result is 8
print(adem2.min()) # result is 5
print(adem2.sum()) # result is 30
#----------------------------- Ravel --------------------------------
# it takes number of arrays of different types and returns a one arrays with one 1-dimension ( Flattned array )
yaakoub = np.array([1,2], [2,3])
print(yaakoub.ravel()) # result is [1 2 2 3]
yaakoub2 = np.array([[[1,2], [3,4]], [[5,6],[7,8]]])
print(yaakoub2.ravel()) # result is [1 2 3 4 5 6 7 8]

#------------------------------------- Numpy Shape & Reshape -----------------------------------------------
# shape => return a tuple contains the number of elements in each dimension of the array

haja = np.array([1,2, 3,4])
print(haja.shape) # result is (4,) a tuple contains the number of elements
haja2 = np.array([1,2,3,4] , [1,2,3,4] , [1,2,3,4])
print(haja2.shape) # result is (3, 4) 3 is the number of elements and 4 is the number of elements of each small array (element)

# Reshape => change the shape of the array to the new shape that we want to give it
# the new shape should be the same size of the old shape
haja = np.array([1,2, 3,4])
print(haja.shape) # result is (4,)
haja = haja.reshape(2,2) # change the shape of the array to 2x2
print(haja.shape) # result is (2, 2)




