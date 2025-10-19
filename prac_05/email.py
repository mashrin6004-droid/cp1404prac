"""
CP1404/CP5632 Practical
Email to name dictionary
"""


def main():
    """Create a dictionary mapping emails to names."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation not in ("y", ""):
            name = input("Name: ").strip().title()
        email_to_name[email] = name
        email = input("Email: ")

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract the expected name from an email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


if __name__ == "__main__":
    main()
