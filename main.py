
from mailtm import Email
import os

save_to_files = input("Save mails into files? y/n > ")

def listener(message):
    print("-----------------")
    print("\nSubject: " + message['subject'])
    print("Content: " + message['text'] if message['text'] else message['html'])
    if save_to_files == "y":
        with open(message['subject'] + ".txt", "w") as file:
            file.write(message['text'] if message['text'] else message['html'])

    else:
        pass

# Get Domains
test = Email()
print("\nDomain: " + test.domain)

# Make new email address
test.register()
print("\nEmail Adress: " + str(test.address))

# Start listening
test.start(listener)
print("\nWaiting for new emails...")
