import csv
import random
import string

def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))

def random_email():
    return f"{random_string(7)}@example.com"

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "age", "email"])
    
    for i in range(1, 10001):  # 1 million rows
        writer.writerow([i, random_string(12), random.randint(18, 90), random_email()])

print("Dataset generated: data.csv")
