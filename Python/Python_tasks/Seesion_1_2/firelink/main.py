# Define the dictionary with URLs
import firelink

print(firelink.links_menu())

while True:
    var = int(input("please selsect usrl [index starts with 0 ]"))  
    firelink.firefox(var)
