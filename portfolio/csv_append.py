import csv
from os import path

def csv_append(data):
    if not isinstance(data,dict):
        print ("This function only takes a dictionary object")
        return None

    if not path.exists('contacts.csv'):
        new = True
    else:
        new = False
    with open('contacts.csv', mode='a', newline='') as csvfile:
        fieldnames = ['user', 'email', 'subject', 'message']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if new:
            writer.writeheader()

        writer.writerow(data)
    return "Done"

csv_append({'user': 'Wasim Memon', 'email': 'wmemon579@gmail.com', 'subject': 'test', 'message': 'test'})
