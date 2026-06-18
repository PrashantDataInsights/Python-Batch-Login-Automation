import csv

with open("user.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
# Process all users from csv
import csv
with open("user.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        email = row["email"]

        pswd = row["pswd"]

        result = login(email, pswd)

        print(
            email,
            "->",
            result
        )
# Save login result into csv

import csv

with open("user.csv", "r") as input_file, \
     open("results.csv", "w", newline="") as output_file:

    reader = csv.DictReader(input_file)

    fieldnames = [
        "email",
        "pswd",
        "login_status"
    ]

    writer = csv.DictWriter(
        output_file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    for row in reader:

        email = row["email"]
        pswd = row["pswd"]

        result = login(
            email,
            pswd
        )

        writer.writerow({
            "email": email,
            "pswd": pswd,
            "login_status": result
        })

print("results.csv created successfully")
