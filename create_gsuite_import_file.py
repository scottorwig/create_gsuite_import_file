import csv
import datetime

"""Set the paths for the input files and output files."""
rowers_input_file = 'rowers.txt'
parents_input_file = 'parents.txt'
rowers_output_file = f'gs_list_rowers_import_{datetime.datetime.today().strftime("%Y-%m-%d")}.csv'
parents_output_file = f'gs_list_parents_import_{datetime.datetime.today().strftime("%Y-%m-%d")}.csv'
rowers_invalid_file = 'rowers_invalid.txt'
parents_invalid_file = 'parents_invalid.txt'

# create lists to store the email addresses
rower_emails = []
parent_emails = []
rower_invalid_emails = []
parent_invalid_emails = []

# read the email addresses from the input files
with open(rowers_input_file, 'r') as file:
    for row in file:
        rower_emails_in_row = [email.strip() for email in row.split(',') if '@' in email.strip()]
        # validate the email addresses and add them to the appropriate list
        for rower_email in rower_emails_in_row:
            if '@' in rower_email:
                rower_emails.append(rower_email)
            else:
                rower_invalid_emails.append(rower_email)

with open(parents_input_file, 'r') as file:
    for row in file:
        parent_emails_in_row = [email.strip() for email in row.split(',') if '@' in email.strip()]
        # validate the email addresses and add them to the appropriate list
        for parent_email in parent_emails_in_row:
            if '@' in parent_email:
                parent_emails.append(parent_email)
            else:
                parent_invalid_emails.append(parent_email)

# write the valid email addresses to files
with open(rowers_output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Group Email [Required]', 'Member Email', 'Member Type', 'Member Role'])
    # write each email address as a row in the csv file
    for email in rower_emails:
        writer.writerow(['rowers@salinerowing.org', email, 'USER', 'MEMBER'])
    print ("File", rowers_output_file,"written")

with open(parents_output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Group Email [Required]', 'Member Email', 'Member Type', 'Member Role'])
    # write each email address as a row in the csv file
    for email in parent_emails:
        writer.writerow(['parents@salinerowing.org', email, 'USER', 'MEMBER'])
    print ("File", parents_output_file,"written")

# write the invalid email addresses to files
with open(rowers_invalid_file, 'w') as file:
    file.write('\n'.join(rower_invalid_emails))
    print ("File", rowers_invalid_file,"written")

with open(parents_invalid_file, 'w') as file:
    file.write('\n'.join(parent_invalid_emails))
    print ("File", parents_invalid_file,"written")
