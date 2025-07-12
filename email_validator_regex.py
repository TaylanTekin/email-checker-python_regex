import re

pattern = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"

while True:
    email = input("Enter your e-mail address (or type 'q' to quit): ")
    if email.lower() == "q":
        print("Goodbye!")
        break
    elif re.match(pattern, email):
        print(f"{email} is a Valid e-mail")
        input("Press Enter to continue...")
        continue
    else:
        print("Please enter a valid e-mail")
        input("Press Enter to continue...")
        continue
