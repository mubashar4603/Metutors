import random
import datetime


class randomGenerate():
    # return email after adding random 3 integers on last
    @staticmethod
    def add_random_numbers_to_email(email, num_digits=5):
        # Split the email address into local part and domain
        local_part, domain = email.split('@')
        # Generate random digits
        random_digits = ''.join(str(random.randint(0, 9)) for _ in range(num_digits))
        # Add "+1" followed by random digits to the local part and recombine
        new_email = f"{local_part}+{random_digits}@{domain}"
        return new_email

    @staticmethod
    def generate_random_phone_number():
        area_code = 201  # Generate a random 3-digit area code
        prefix = 234  # Generate a random 3-digit prefix
        line_number = random.randint(1000, 9999)  # Generate a random 4-digit line number
        phone_number = f"{area_code}{prefix}{line_number}"  # Format the phone number
        return phone_number

    @staticmethod
    def generate_random_date():
        # Get today's date
        today = datetime.date.today()

        # Calculate the date for tomorrow
        tomorrow = today + datetime.timedelta(days=1)

        # Generate a random number of days between 1 and 365 (1 year)
        random_days = random.randint(1, 365)

        # Calculate the random date by adding the random number of days to tomorrow
        random_date = tomorrow + datetime.timedelta(days=random_days)
        formatted_date = random_date.strftime("%d/%m/%Y")

        return formatted_date

# Example usage:
# random_date = random_date_after_tomorrow()
# print("Random Date After Tomorrow:", random_date)
# print(randomGenerate.generate_random_date())
