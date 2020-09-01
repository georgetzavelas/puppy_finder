## Puppy Finder

A collection of python scripts to help you find a dog! It uses Beautiful Soup to scrape some of the more common dog sites around Ottawa and 
when it finds a new dog, send you a SMS. Inspired by the work of https://github.com/KaraDaviduik!

### Configuration
Sign up for a Twilio developer account and use the money you get from the initial signup to buy a virtual phone number 
to be the originator of the SMS messages. Find your Account SID and Auth token. With all this information create 
a twilio.yaml file that looks like:

```
# Mobile numbers
from_phone_number: <originator_phone_number>
to_phone_number: <your_phone_number>

# Twilio credentials
prod_account_sid: <production_account_sid>
prod_auth_token: <production_auth_token>
```

### Installation
For a MAC (or Linux) system you should be able to use the attached plist file (you can remove my name, haha!) 
and change the paths to reflect your own.

```
chmod +x <path_to_puppy_finder>/find_dogs.sh
cd ~/Library/LaunchAgents/
cp <path_to_puppy_finder>/org.georgetzavelas.puppy-finder.plist .
launchctl load org.georgetzavelas.puppy-finder.plist
```

The plist file is configured to run every hour. Logs should appear in your puppy_finder directory.
