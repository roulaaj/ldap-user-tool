import pandas as pd

# Load "LDAP-like" data
df = pd.read_csv("users.csv")

print("LDAP User Search Tool")
print("1. Search by username")
print("2. Search by email")

choice = input("Choose option: ")

if choice == "1":
    username = input("Enter username: ")
    result = df[df["username"].str.contains(username, case=False, na=False)]
elif choice == "2":
    email = input("Enter email: ")
    result = df[df["email"].str.contains(email, case=False, na=False)]
else:
    print("Invalid choice")
    result = None

if result is not None and not result.empty:
    print("\nUser found:")
    print(result)
else:
    print("\nNo user found.")
