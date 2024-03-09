def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        return sorted(str1.lower()) == sorted(str2.lower())

string1 = input("Enter the 1st string: ")
string2 = input("Enter the 2nd string: ")

if is_anagram(string1,string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
