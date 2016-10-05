import csv

with open('Python for QA - bugs list - Sheet1.csv', 'r') as csvfile, open('first_edit.csv', 'wb') as csvout:

    fieldnames = ['#', 'Description', 'Environment', 'Priority', 'Owner', 'Created At']
    writer = csv.DictWriter(csvout, fieldnames=fieldnames)
    writer.writeheader()

    for row in csv.DictReader(csvfile):
        if row['Priority'] != 'low':
            if row['Priority'] == 'critical':
                row['Priority'] = 'high'
            elif row['Priority'] == 'high':
                row['Priority'] = 'medium'
            elif row['Priority'] == 'medium':
                row['Priority'] = 'low'
            writer.writerow(row)
