
# a list of integers that needs to be converted into character to obtain the flag.
Alist = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

print(Alist)

#print the integers by first converting them into chr "ASCII character" using chr() function and then join them with no spaces ("".join()) to generate a flag.
print("".join(chr(x) for x in Alist))

print("--------REVERSE ENGINEERING-------------")
# Now, using ord() function to do reverse ASCII conversion
# Taking the String as Flag
flag = "crypto{ASCII_pr1nt4bl3}"
print("The String to be converted with ord() function: ", flag)

#create an Empty list
Blist=[]

# Use for loop to iterate over the list elements and 
# convert them into the ASCII equivalent integer using ord() function
for ch in flag:
    Blist.append(ord(ch))

print (Blist)