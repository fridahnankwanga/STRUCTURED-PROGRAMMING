credentials={
    'username': "B33343@students.ucu.ac.ug",
    'password': "12345"
}

print(credentials ["username"])

print("log in system")
username = input("Enter username")
password = input("Enter your password")

if username== credentials['username'] and password == credentials['password']:
    print("logged in successfully!")
else:
    print("invalid credential,please try again")
