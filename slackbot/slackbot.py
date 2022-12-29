import requests
import config
import slack
from slackeventsapi import SlackEventAdapter
import health
import trello

COMMAND_OPTIONS = [
    "`temp`",
    "`cleanup`"
]

def daily_cleanup_list():
    client = slack.WebClient(token=config.SLACK_API_TOKEN)
    client.chat_postMessage(channel="#voice_of_the_hawk", text="10 seconds have passed")

def respond_to_message(text):
    split_text = text.split(" ")
    command = split_text[0]
    parameters = ""
    if len(split_text) > 0:
        parameters = " ".join(split_text[1:])

    if command == "temp":
        return health.core_temperatures()
    elif command == "cleanup":
        if parameters == "":
            return "Please specify card name"
        else:
            card_created = trello.create_card_on_cleanup_board(parameters)
            if card_created:
                return f"Created card for `{parameters}`"
            else:
                return "Card creation failed"
    else:
        command_options_string = "\n".join(COMMAND_OPTIONS)
        return "Current supported commands are:\n" + command_options_string