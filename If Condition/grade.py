s= int(input("Enter your score: "))

if s >= 90:
    print("Your grade is A.")
elif 80 <= s < 90:
    print("Your grade is B.")
elif 70 <= s < 80:
    print("Your grade is C.")
elif 60 <= s < 70:
    print("Your grade is D.")
else:
    print("Your grade is F.")
