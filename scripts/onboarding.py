'''Completely automated on-boarding from HR adding to payroll then auto creating AD/O365 Accounts & licensing, then sending appropriate auto generated emails to respective teams using html templates'''

import csv
from pyad import aduser, pyad

def addUserFromCSV(csv_path:str) -> None:
    try:
        # Connect to AD Server
        pyad.set_defaults(ldap_server="$LDAP Server")

        #Read data from csv
        with open(csv_path, "r") as file:
            reader = csv.DictReader(csv_path)

            for row in reader:
                first_name = row["First Name"]
                last_name = row["Last Name"]
                ou = row["Organizational Unit"]
                external_email = row["Notification Email"]
                employee_number = row["Employee number"]

                # Construct corporat email
                corporate_email = f'{first_name.lower()}.{last_name.lower()}@DOMAIN.COM'

                # Create Account
                user = aduser.ADUser.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    organizational_unit=ou,
                    employee_number=employee_number,
                    email=corporate_email
                )

                print(f"user account created:\nUsername: {user.get_username()}\nEmail: {user.get_email()}")

    except Exception as e:
        print(f"An error occured: {e}")

    if __name__ == "__main__":
        addUserFromCSV("path/to/csv")
