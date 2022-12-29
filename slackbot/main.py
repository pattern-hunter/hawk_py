import config
import slack
from flask import Flask
from slackeventsapi import SlackEventAdapter
import slackbot

# https://7ce4-2600-1700-3b80-a460-c193-1cbb-3a9e-5d02.ngrok.io
# Running steps
# run ngrok http 5000, copy url into this file
# run python main.py in another terminal
# run redis-server in another terminal
# run rqscheduler or rqscheduler --host localhost --port 6379 --db 0 in another terminal
# rqscheduler -v -i 1 v is verbose, interval is 1 second


app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(config.SLACK_SIGNING_SECRET, "/slack/events", app)
client = slack.WebClient(token=config.SLACK_API_TOKEN)
BOT_ID = client.api_call("auth.test")['user_id']

@slack_event_adapter.on('message')
def post_simple_message_to_slack(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    response = slackbot.respond_to_message(text)
    if BOT_ID != user_id:
        client.chat_postMessage(channel=channel_id, text=response)

if __name__ == "__main__":
    app.run(debug=True)
