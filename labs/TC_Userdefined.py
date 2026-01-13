class MyError(Exception):
    pass
#raise MyError(this is a User defined exception)

class invalidAge (Exception):
    pass



try:
    age=int(input("Enter age"))
    if age<18:
        raise invalidAge("Age must be 18 or above")
    else:
        print("eligible to vote")
except invalidAge as e:
    print("Error ",e)