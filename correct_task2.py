# it makes nosesnse to only check for the existance of '@' to make sure it is a valied email, that's why i'm using the regular expression
import re

def count_valid_emails(emails):
    # in the begining we need to make sure that the 'emails' paramter is a list or a tuple
    # to avoid any problems that could happen due to any invalid inputs, if not we need to stop the preocess
    if not isinstance(emails, (list, tuple)):
        raise ValueError("Input must be a list or tuple of strings.")
    
    # this is the regular expression that i'm using, it is allowed to have anything before the '@' sign
    # but to ensure the domain part we need to have a garenteed dot after the '@' sign with whatever before the dot and whatever after it.
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    count_of_valid_emails = 0
    for email in emails:
        # need to check that the 'email' is a string, and we can just ignore the edge whitespaces 
        if isinstance(email, str) and email.strip():
            if email_pattern.match(email.lower()):  # match the email with the regular expression created above to make sure it's valid
                count_of_valid_emails += 1


    return count_of_valid_emails
