astring = "Hello World!"
print("single quotes are ' '")
print(len(astring))

print (astring.index("o"))
print (astring.count("l"))
print (astring[3:7])

#if you write a negative number Python will treat it as
# n numbers from the end.
print (astring[2:-2])

#The syntax is [start:stop:step]
print (astring[3:7:2])

#To reverse the string use the following:
print(astring[::-1])

#To convert the letters into lowercase and uppercase use:
print(astring.lower())
print(astring.upper())

print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

afewwords = astring.split(" ")
print (afewwords)
