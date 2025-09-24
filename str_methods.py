"""Case Manipulation:
lower(): Converts all characters in a string to lowercase.
upper(): Converts all characters in a string to uppercase.
capitalize(): Capitalizes the first character of the string and converts the rest to lowercase.
title(): Converts the first character of each word to uppercase and the rest to lowercase.
swapcase(): Swaps the case of all characters (uppercase to lowercase, lowercase to uppercase).
Searching and Finding:
find(substring): Returns the lowest index of the first occurrence of substring. Returns -1 if not found.
rfind(substring): Returns the highest index of the last occurrence of substring. Returns -1 if not found.
index(substring): Similar to find(), but raises a ValueError if the substring is not found.
count(substring): Returns the number of non-overlapping occurrences of substring in the string.
startswith(prefix): Returns True if the string starts with the specified prefix, False otherwise.
endswith(suffix): Returns True if the string ends with the specified suffix, False otherwise. 
Modification and Replacement:
replace(old, new): Returns a new string with all occurrences of old replaced by new.
strip(): Removes leading and trailing whitespace characters.
lstrip(): Removes leading whitespace characters.
rstrip(): Removes trailing whitespace characters.
join(iterable): Concatenates the elements of an iterable (e.g., a list of strings) with the string on which it's called as a separator.
split(separator): Splits the string into a list of substrings using separator as the delimiter. If no separator is given, it splits by whitespace.
splitlines(): Splits the string into a list of lines, breaking at line boundaries.
Checking String Properties:
isalnum(): Returns True if all characters are alphanumeric (letters or numbers).
isalpha(): Returns True if all characters are alphabetic.
isdigit(): Returns True if all characters are digits.
islower(): Returns True if all cased characters are lowercase.
isupper(): Returns True if all cased characters are uppercase.
isspace(): Returns True if all characters are whitespace.
istitle(): Returns True if the string is in title case. 
"""