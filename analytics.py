import requests
import os

analytics_token = os.environ["ANALYTICS_TOKEN"]

headers = {'content-type': "application/json"}
message = {
    'message':
        {
            'text': '',
            'kind': 'incoming',
            'conversation_identifier': '',
            'sender_identifier': '',
            'platform': 'telegram'
        }
}

URL = 'http://www.botlytics.co/api/v1/messages?token=' + analytics_token


def incoming(text, conversation_identifier, sender_identifier=' '):
    message['message']['text'] = str(text)
    if sender_identifier is None:
        sender_identifier = 'user'
    message['message']['conversation_identifier'] = str(sender_identifier) + '_' + str(conversation_identifier)
    message['message']['sender_identifier'] = str(sender_identifier) + '_' + str(conversation_identifier)
    header = {'content-type': "application/json"}
    requests.post(url=URL, headers=header, json=message)
