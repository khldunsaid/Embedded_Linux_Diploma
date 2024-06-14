l = input ("enter your charcter; ")

if l.lower() in ('a','e','i','o','u') or l.upper() in ('A', 'E', 'I', 'O', 'U') :
    print("Vowel")
# elif l.upper() in ('A', 'E', 'I', 'O', 'U'):
#     print("Vowel")
else:
    print("Consonant")