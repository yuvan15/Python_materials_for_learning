'''
Notes :-
  1.Without mentoning the datatype of variable,All datas is considerd as strings in python
  2.All string methods returns new values,They do not change the original string
  3.Strings can be mentioned as example = 'python' or example = "python" and same with triple quotation's
  4.This type of deceleration give us error we should use "" for this if ' is used in string
    String_value1= 'Hai I'm python String'
  5. Can't declare string like 'Python" or "python'
'''

"""
Error's to be noted:-
    1.Index Error = Trying to access a character out of index range 
    2.Type Error = The index must be an integer. We can't use other types
"""


value = "hai I am Python stRing"

#String Methods

#1.Captilize--> capitalise first letter
print(value.capitalize())

#2.Casefold --> converts whole string to lower case
print(value.casefold())

'''
3. Center() 

syntax => Center(length, character)
length(Required) - > length of the returned string
character(Optional) -> values to fill the missing space on each side.
 (Default=space)
 '''

print(value.center(50))

print(value.center(50,'#'))

'''
4. Count() -> counts how many time the value is present

syntax => Count(value_to_count,startIndex,endIndex)
value_to_count is Required parameter
startIndex & endIndex are Optional parameter and default is 0 & -1
Note :- It is case sensitive
'''
print(value.count('I'))

'''
5.Encoding->encodes String

syntax => Encode(encoding,errors)
encoding -> mention which encoding to use. Default is UTF-8

errors -> 
    'backslashreplace'- uses a backslash in character that could not be encoded
    'ignore'	- ignores the characters that cannot be encoded
    'namereplace'	- replaces the character with a text explaining the character
    'replace'	- replaces the character with a questionmark
    'xmlcharrefreplace'	- replaces the character with an xml character
    'strict'	- Default, raises an error on failure
'''
string_to_encode = "I åm going to hide"

print(string_to_encode.encode(encoding="ascii",errors="backslashreplace"))
print(string_to_encode.encode(encoding="ascii",errors="ignore"))
print(string_to_encode.encode(encoding="ascii",errors="namereplace"))
print(string_to_encode.encode(encoding="ascii",errors="replace"))
print(string_to_encode.encode(encoding="ascii",errors="xmlcharrefreplace"))
#print(string_to_encode.encode(encoding="ascii",errors='strict'))

'''
6.Endswith -> (string ending with value or not)

syntax => endswith(value, start, end)
 value is required
 start & endare Optional parameter and default is 0 & -1
 It is case sensitive
'''
print(value.endswith('e'))
print(value.endswith('g'))
print(value.endswith(('string')))
print(value.endswith(('stRing')))

'''
7. Expandtab -> expands space in tab(\t)

syntax = expandtabs(tabsize)
'''
text = "I love\t python"
print(text.expandtabs(10))

'''
8.Find() -> gives the position if the searching string

syntax => find(value_to_find,start_index,end_index)
value_to_count is Required parameter
startIndex & endIndex are Optional parameter and default is 0 & -1

Note :- If string is not there it'll return (-1)
'''
print(value.find("Python"))
print(value.find("python"))

'''
9. format - format value

syntax => format(value(1), value(2)...value(n))
'''
#Inside the placeholders you can add a formatting type to format the result:
'''

:<		Left aligns the result (within the available space)
:>		Right aligns the result (within the available space)
:^		Center aligns the result (within the available space)
:=		Places the sign to the left most position
:+		Use a plus sign to indicate if the result is positive or negative
:-		Use a minus sign for negative values only
: 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:,		Use a comma as a thousand separator
:_		Use a underscore as a thousand separator
:b		Binary format
:c		Converts the value into the corresponding unicode character
:d		Decimal format
:e		Scientific format, with a lower case e
:E		Scientific format, with an upper case E
:f		Fix point number format
:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g		General format
:G		General format (using a upper case E for scientific notations)
:o		Octal format
:x		Hex format, lower case
:X		Hex format, upper case
:n		Number format
:%		Percentage format

'''
format_string = "laptop cost around {:_} rupees" #thousand seperator
print(format_string.format(500000))

'''
10. Index() -> provide the index of the value

syntax => index(value_to_find,start_index,end_index)
alue_to_count is Required parameter
startIndex & endIndex are Optional parameter and default is 0 & -1

'''
print(value.index('Python'))

'''
11. isalNum() -> return true if the value is alphanumeric
'''
val_1 = 'pyhton30'
print(val_1.isalnum())

'''
12. isalpha() -> return true if the value is alphabetic
'''
val_2 = 'qsfhYojfg'
print(val_2.isalpha())

'''
13. isascii() - > return true if values in between (a-z)
'''
val_3 = 'qweryuvb785$#%'
print(val_3.isascii())

val_4 = 'ASFåyhcf674#%'
print(val_4.isascii())

'''
14. isdigit() -> returns true if all characters in the string are digits
'''
val_5 = '844984884'
print(val_5.isdigit())

'''
15.isidentifier() -> return true if the given string is a valid identifier

identifier:-
     1. Identifier  only contains alphanumeric letters (a-z) and (0-9), or underscores (_). 
     2. A valid identifier cannot start with number and contain any spaces.
'''

val_6 = 'I_amIdentifier123'
print(val_6.isidentifier())

val_7  = ' 2IamNotanIdentifier'
print(val_7.isidentifier())