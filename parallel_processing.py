# Run multiple login jobs in parallel

from concurrent.futures import ThreadPoolExecutor

users = [
    ("admin@test.com", "1234"),
    ("user@test.com", "1111"),
    ("admin@test.com", "9999"),
    ("hello@test.com", "4344")
]

def process_user(user):
    
    email = user[0]
    pswd = user[1]

    result = login(email, pswd)

    print(
        email,
        "->",
        result
    )

    return result


with ThreadPoolExecutor(max_workers=3) as executor:

    executor.map(
        process_user,
        users
    )
