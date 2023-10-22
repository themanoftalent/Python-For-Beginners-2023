lang = input("Enter your specialized language\n")

if lang == "python" or lang == "c++":
    print("You can continue")
    fields = input("Enter your field\n")
    if fields == "data science" or fields == "web development" or fields == "graphics":
        print("You are definitely eligible for this job")
        expe = int(input("Enter the years of experience\n"))
        if expe >=3:
            print("Welcome to our company")
        else:
            print("Better luck next time fella")

    else:
        print("This place ain't for you")
else:
    print("You are not eligible for this job")