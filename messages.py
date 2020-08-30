from twilio.rest import Client
import yaml


# format new puppy alert
def send_message(line1, line2, line3, line4, line5=''):
    body = f"NEW DOG - {line1}\n\n{line2}\n{line3}\n{line4}\n{line5}"
    twilio_send_sms(body)


# use twilio to send sms
def twilio_send_sms(body):
    with open(r'twilio.yaml') as file:
        twilio_params = yaml.load(file, Loader=yaml.FullLoader)
        account_sid = twilio_params['prod_account_sid']
        auth_token = twilio_params['prod_auth_token']
        from_phone_number = twilio_params['from_phone_number']
        to_phone_number = twilio_params['to_phone_number']
        client = Client(account_sid, auth_token)
        message = client.messages.create(body=body, from_=from_phone_number, to=to_phone_number)
        print(message.sid)
