while True:
    user_input = int(input("Enter a number: "))
    if user_input < 0:
        print("Negative number entered! Exiting loop.")
        break
    else:
        print(f"You entered: {user_input}")
