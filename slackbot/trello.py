import requests
import config
import json

def create_card_on_cleanup_board(card_name):
    headers = {
        "Accept": "application/json"
    }
    query = {
        'idList': '63ac4859a10869013ba8ca94',
        'key': '8122f7e2f62e550e043dd23cc6addba2',
        'token': '76e9d397f422b221cbfce2281459848c26e8a03069b471f889456fcddb319bbd',
        'name': card_name,
    }

    response = requests.request(
        "POST",
        f"{config.TRELLO_API_URL}cards",
        headers=headers,
        params=query
    )

    return response.ok