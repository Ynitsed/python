# Chapter 2 Page 24 1_name.py
name = "gabriel k. lu\n"
print(name.title())

#In this example, the lowercase string "ada lovelace" is stored in the variable
#name . The method title() appears after the variable in the print() statement. 
#A method is an action that Python can perform on a piece of data. The
#dot ( . ) after name in name.title() tells Python to make the title() method
#act on the variable name .

print(name.upper())
print(name.lower())

first_name = "gabriel"
last_name = "lu"
full_name = first_name + " " + last_name
print(full_name)

print("\nHello, " + full_name.title() + "!\n")

message = "\nHello, " + full_name.title() + "!\n"
print(message)