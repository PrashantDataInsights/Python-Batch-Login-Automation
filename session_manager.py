# UserSession class is used to manage login session
class UserSession:
    # Constructor initializes default session values
    def __init__(self):
        self.is_authenticated = False
        self.user_email = None
    # Constructor initializes default session values
    def create_session(self, email):    
        self.is_authenticated = True
        self.user_email = email
    # Destroy session during logout
    def destroy_session(self):
        self.is_authenticated = False
        self.user_email = None
     # Return current session details
    def get_session_info(self):
        return {
            "authenticated": self.is_authenticated,
            "email": self.user_email
        }
# Example usage of UserSession class
session = UserSession()

print(session.get_session_info())

session.create_session("admin@test.com")

print(session.get_session_info())

session.destroy_session()

print(session.get_session_info())

# Login function that creates a session if authentication is successful
def login_user(email, password):

    if login(email, password):

        session = UserSession()

        session.create_session(email)

        return session

    return None
user_session = login_user(
    "admin@test.com",
    "1234"
)

if user_session:
    print("Login Success")
    print(
        user_session.get_session_info()
    )

else:
