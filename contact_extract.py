import re
import os
from pprint import pprint

# the function define below helps remove unwanted string so that the vcf file can become more human readable
def parsing_contact(file_path):
    with open(file_path, 'r') as txt:
        raw_txt = txt.read()
        raw_txt = raw_txt.strip().split('END:VCARD')
        parsed_contact = []
        for a in raw_txt:
            a = a.replace('BEGIN:VCARD\n', '').replace('VERSION:2.1\n', '').replace(';CELL', '').replace('FN', 'NAME')
            a = re.sub('N.*;', '', a)
            a = a.strip().strip()
            a = a.replace('\n', '; ')
            for b in re.findall(r'PHOTO.*', a):
                a = a.replace(b, '')
            parsed_contact.append(a)
        return parsed_contact


# This function will help you sort the contact by name
def sort_key(elem):
    a = elem.find(':')
    b = elem.find(';')
    return elem[ a + 1: b ].lower()

# extracting the path for the file
file_dir = r'C:\Users\BOLAJI\Desktop'
file_name = r'contacts.txt'
file_path = os.path.join(file_dir, file_name)

# checking the raw vcf file so as to be able to compare it with the parsed_contact
raw_file = open(file_path, 'r').read()
pprint(raw_file)

# printing the parsed_contact
parsed_contact = sorted(parsing_contact(file_path), key = sort_key)
pprint(parsed_contact)
print(len(parsed_contact))