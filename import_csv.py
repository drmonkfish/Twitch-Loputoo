import csv

# Read the content of the file
with open("D:\PYTHONTWITCH\chat_logs_ironmouse\ironmouse_20250331_1051+results.txt", 'r') as file:
    content = file.read()

# Split the content into lines
lines = content.split('\n')

# Open a new CSV file to write the content
with open('ironmouse_20250331_1051+results 1.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Write each line to the CSV file
    for line in lines:
        # Split each line by tab character
        row = line.split('\t')
        csvwriter.writerow(row)

print("The content has been successfully converted to ironmouse_20250331_1051+results 1.csv")