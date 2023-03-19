# create_gsuite_import_file
Given text files, create G Suite import CSVs for groups

Created to use with a high school rowing team, which has "parents" and "rowers" groups. Two text files are created by manually copy/pasting from the
roster in a Google Sheet. Named:
parents.txt
rowers.txt

This code reads the text files and outputs date-stamped CSV files that can be 
imported into G Suite to update our mailing lists.

Configuration info is stored in a json file.
