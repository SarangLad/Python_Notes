print("thank you for watching");

#Variables
myVar = "test";
a,b,c = 20, 30, 50;
globalVar = "This is global variable"

#semicolon is optional in python programming
if 5 > 2:
    print("5 greater then 2")
else:
    print("5 less then 2");
    
print(myVar);

#Many values to multiple variable
x,y,z = 10, 20, 30;
print(x); print(y); print(z);

#One values multiple variables
x=y=z = 10;
print(x); print(y); print(z);

# Unpack a collection
fruits = ["banana", "mango", "coconut"];
x,y,z = fruits;
print("---------"); print(x); print(y); print(z);

print("---------");
# Multiple variables display using comma seperated
print(x,y,z);

# Multiple variables also use + operator concate variables
print(x + y + z);

# Print multiple Values
print(a + b + c);

def myFunc():
    # this variable will be local, and can only be used inside the function
    globalVar = "change value";
    print("Output is - "+ globalVar);

myFunc();
# The global variable with the same name will remain as it was, global and with the original value.
print("Output is - "+ globalVar);
