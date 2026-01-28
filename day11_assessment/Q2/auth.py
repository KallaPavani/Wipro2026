def login(username, password):
    if username == "admin" and password == "Welcome123":
        return "Login Successful"
    return "Login Unsuccessful, Invalid Credentials"