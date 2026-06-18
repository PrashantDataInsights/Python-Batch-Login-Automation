# Authentication logic
VALID_USERS = {
    "admin@test.com": "1234",
    "user@test.com": "1111"
}
def login(email, password):
    if email in VALID_USERS:
        if VALID_USERS[email] == password:
            return True
    return False
  # Return True if login is successful
result = login(
    "admin@test.com",
    "1234"
)
print(result)
# Return False if login fails
result = login(
    "admin@test.com",
    "9999"
)
