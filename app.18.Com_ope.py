name= "Alex_Writer"

print(f"numbers of characters : {len(name)}")

if len(name) < 3:
    print("must be more than 3 characters")
elif len(name) > 20:
    print("it must be less than 20 characters")
else:
    print("name looks good!")