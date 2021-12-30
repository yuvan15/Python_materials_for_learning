#Data Types in python
'''
* Text Type:	    string
* Numeric Types:	integer, float, complex
* Sequence Types:	list, tuple
* Mapping Type:	    dictionary
* Set Types:	    set, frozenset
* Boolean Type:	    boolean
* Binary Types:	    bytes, bytearray, memoryview

'''
#Integer
num = int(560)
print(type(num))

#Float
float_num = float(2.015)
print(type(float_num))

#String
string =str("I'm String in Python")
String1=("I'm also string in python")
print(type(string))
print(type(String1))

#Complex
complex_val = complex(2+5j)
print(type(complex_val))

#Boolean
val = True
print(type(val))

val_1 = False
print(type(val_1))

#List
values =list(("Hai","I","am","list"))
print(type(values))

list = ["hai","I","am","also","list"]
print(type(list))

#Tuple
tuple_1 = tuple(("I'm","tuple","in","python"))
print(type(tuple_1))

tuple_2 = ("I'm","also","tuple","in","python")
print(type(tuple_2))

#Dictionary
dct = {"language":"python","data-type":"Dictionary",
       "ordered":" for pyt version 3.7 & above",
       "unordered":"for pyt version 3.6 & below"}
print(type(dct))

#Set & Frozen-Set
set_1 = set(("Hi, ","I'm set in python , ","I'm unordered ",", unchangable","& never allow duplicate"))
print(type(set_1))

set_2={"unordered","unchangable","non-duplicate","Is my power"}
print(type(set_2))

frozen = frozenset({"I'm","frozen"})
print(type(frozen))

#Byte
byt = b"Byte_data-type"
print(byt)
print(type(byt))

#Byte array
byt_arr = bytearray(5)
print(byt_arr)
print(type(byt_arr))

#byte memory allocation
byte_mem = memoryview(bytes(5))
print(byte_mem)
print(type(byte_mem))
