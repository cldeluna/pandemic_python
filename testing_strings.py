import os

# This is a comment Note the first character is the # symbol
# The # character tells python this is a comment
print("\n==== Variables (Scalar Variables):")

today = "Monday"
print(f"variable name today with value {today}")
print(f"variable name today of type {type(today)}\n")

pi = 3.14
print(f"variable name pi with value {pi}")
print(f"variable name pi of type {type(pi)}\n")

mynum = 7
print(f"variable name mynum with value {mynum}")
print(f"variable name mynum of type {type(mynum)}\n")

print("\n==== Variables (Collections - Lists, Dictionaries):")
print("Lists")
interfaces = ["Gi1/0/1", "Gi1/0/2" ]
print(f"variable name interfaces with value {interfaces}")
print(f"variable name interfaces of type {type(interfaces)}")

print(f"The fist element in the list: {interfaces[0]} which is of type {type(interfaces[0])}")
print(f"The second element in the list: {interfaces[1]} which is of type {type(interfaces[1])}\n")
print("Iterate over the list of interfaces...")
for intf in interfaces:
    print(intf)
print()

print("\nDictionaries")
trucks = {"Ford": "F150", "Dodge": "Ram", "Toyota": "Tundra"}
print(trucks['Ford'])
#
print("Iterate over the key:value pairs of the trucks dictionary...")
for key, value in trucks.items():
    print(f"Key: {key}\t Value:{value}")
    if key == "Toyota":
        print(f"The {value} doesnt suck!\n")


# Multiline Variables
gems = """
ruby
sapphire
diamond
emerald
topaz
"""

gems2 = """
ruby,
sapphire,
diamond,
emerald,
topaz,
"""

# If you see something like below, thats the old Python 2 print statement
# This will not run on python3
# print today
print(f"\nPrint the required Hello World to STDOUT - {today}")
print("Hello World!")
print('hello', 'world', sep=' ')
print('hello', 'world', sep='\n')
#
print()
print()
print(today)
print(gems)
print("see what happens to the variable gems if you turn it into a list and print")
print(list(gems))
print("print the first element in the variable today, then print the second element")
print(today[0])
print(today[1])

print("\nVarious examples of print syntax as python evolved")
print('Hello, ' + os.getlogin() + '! How are you this fine ' + today + '?')
print('The year is %d'%2020)
print("Today is {}!".format(today))


print()
print(f"Hello {os.getlogin()}! How are you this fine {today.upper()}?")
print("Note the mix of quotation types...(in the code not in the output)")
print(f"Hello {os.getlogin()}! How are you this 'fine' {today.lower()}? <- What were the outer quotations used for this print statement?")
print(f'Hello {os.getlogin()}! How are you this "fine" {today}? <- What were the outer quotations used for this print statement?')

print()
print(f"\n printing help for a varialbe - dir() and type()")
print(dir(today))
print(type(today))
print(today.isdecimal())
