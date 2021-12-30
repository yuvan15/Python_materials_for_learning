"""
Type Casting
"""

# Number to String
num = int(5864)
print("Number = ",num)
print(type(num))
string = str(num)
print("String = ",string)
print(type(string))

# Number to Float
num1 = int(563)
print("Number = ",num1) 
print(type(num1))
flt = float(num1)
print("Float = ",flt)
print(type(flt))

# String to Number
gig = "565"
gig=int(565)
print(type(gig))

# String to List
'''
Synatx --> variable_name.split("delimiter")
'''
hooh = "Hai I am string created by hooman for learning"
print('String = ',hooh)
String_To_List = hooh.split(" ")
print("List = ",String_To_List)
print(type(String_To_List))

# List to String
delimiter= ' '
list_To_String = delimiter.join(String_To_List)
print("String = ",list_To_String)
print(type(list_To_String))

# List to Set
'''Remember Set never allows duplicate values'''
set_from_list = set(String_To_List)
print("Set_from_list = ",set_from_list)
print(type(set_from_list))

# Set to List
list_from_Set = list(set_from_list)
print("list_from_Set = ",list_from_Set)
print(type(list_from_Set))

# List to Dictionary
list_to_convert = ['Language','Python','Age',30,'Designed_By','GuidovanRossum']
dict_from_list = { i : list_to_convert[i] for i in range(1, len(list_to_convert))}
print(dict_from_list)
print(type(dict_from_list))

# Dictionary to List
values_from_dictionary = list(dict_from_list.values())
print("Values_from_dict = ",values_from_dictionary)
print(type(values_from_dictionary))
keys_from_dictionary = list(dict_from_list.keys())
print("Keys_from_dict = ",keys_from_dictionary)
print(type(keys_from_dictionary))
