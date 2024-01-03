print("Good day, how are you doing?")


def verify_inputs(name, email, password):
    if name == "":
        print("Name cannot be empty")
        return

    print("This function verifies input")


def verify_name():
    name = input("What is your name?: | ")
    if name == "":
        print("Name cannot be empty")
        verify_name()
        return False


def verify_email():
    email = input("Please provide your email: | ")
    if email.__contains__("@gmail.com") and email != "":
        return True
    else:
        print("Please use a valid email")
        verify_email()
        return False


def verify_password():
    password = input("Input a strong password: | ")
    print(len(password))
    if password == "" and (len(password) < 8):
        print("C`mon!, that is not strong, provide something stronger!")
        verify_password()
    elif len(password) < 8:
        print("Use a better password")
        verify_password()



def set_up_interaction():
    verify_name()
    verify_email()
    verify_password()
    print("Thank you for your time, this wasn't hard, was it?")


set_up_interaction()

# job = "danprecious@gmail.com"
# if job.__contains__("@gmail.com"):
#     value = job.find("@")
#     print("It does at index: " + str(value))