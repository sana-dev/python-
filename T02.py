lower_limit = int(input("specify the lower_limit"))
upper_limit = int(input("specify the upper_limit"))
print(f'\n The range is from {lower_limit} to {upper_limit}\n')

number = int(input("input a number:"))

if number >= lower_limit and number <= upper_limit:
    print("the number lies inside the specific range")

else:
    print("the number lies outside the specific range")    
