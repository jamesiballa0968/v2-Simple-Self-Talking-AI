print("Initializing.......----=============\n ===============>>>>>>")
print("process initialized successfully.....")
print("Hello there fellow programmer! This is JAMES AI")

name = input("May I ask your name? ")
print("Hello " + name + ". Can you put your age?")

age = int(input("Your age is? "))
seconds = str((float(((3600 * 24)*7)*4.3)*12) * age)
minutes = str((float(((60 * 24)*7)*4.3)*12) * age)
hours = str(((float((24*7)*4.3)*12) * age))
days = str(((float(7 * 4.3)*12) * age))

#testing for seperate branch!

print("--------------\nTRIVIA TIME!\n--------------\nThis is your age when translated to seconds:" + seconds + " seconds")
print("This is your age when translated to minutes:" + minutes + " minutes")
print("This is your age when translated to hours:" + hours + " hours")
print("This is your age when translated to days:" + days + " days")
print("--------------")

hobby = input("And lastly, your favorite hobby?")
print(hobby + "?.Interesting hobby")
print("--------------------------------------")
print("Time to go out now " + name + "!.\nSee yah ")
