
credentials = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3",
    "user4": "password4",
    "user5": "password5",
}
def registro (user,password):
    global credentials
    credentials[user] =password

def main():
    print(credentials)

if __name__ == "__main__":
    main()