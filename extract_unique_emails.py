# This code will first find all the .txt files in the 
# specified directory, and extract all the email
# addresses into a set unique_emails, which will 
# automatically remove duplicates. Then it writes
# the sorted list of unique email addresses to a new # file unique_emails.txt.

import os
import re


def get_unique_emails(file_list):
    unique_emails = set()
    for file in file_list:
        print ("Reading file", file)
        with open(file, 'r') as f:
            for line in f:
                email = line.strip()
                print (email)
                unique_emails.add(email)
    print (len(unique_emails),"emails in list")
    return unique_emails


def write_to_file(file_name, email_list):
    with open(file_name, 'w') as f:
        if is_valid_email(email):
            f.write(','.join(email_list))
        else:
            print(email,"is not valid.")
    print ("File written to", file_name)


def main():
    directory = '/Users/scottorwig/Documents/rowing/rowing_code/email_txt_files'
    file_list = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.txt')]
    unique_emails = sorted(get_unique_emails(file_list))
    write_to_file('unique_emails.txt', unique_emails)

def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None


if __name__ == '__main__':
    main()