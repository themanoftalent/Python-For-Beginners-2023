
while True:

    try:
        the_number = 10
        my_input = int(input("Please enter the number you want\n"))
        result = the_number / my_input
        print(result)
        break

    except Exception:
        print("Something is not right")

    finally:
        print("Code has finished executing")
