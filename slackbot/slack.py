import requests
import config

def post_simple_message_to_slack(text):
    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': config.SLACK_API_TOKEN,
        'channel': config.SLACK_CHANNEL_ID,
        'text': text,
    }).json()