"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function

SKILL_NAME = 'Stocky'
NUM_STOCK_ITEMS = '5'
STOCK_ITEMS = [
    {
        'name': 'IKEA FRAKA cap',
        'img_url': 'https://hypebeast.imgix.net/http%3A%2F%2Fhypebeast.com%2Fimage%2F2017%2F05%2Fpleasures-chinatown-market-ikea-frakta-hat-1.jpg?auto=compress%2Cformat&fit=max&fm=pjpg&ixlib=php-1.1.0&q=90&w=1580&s=c892a1cd55036f675d8f37c1d7efa637',
        'amount': '3 left',
        'description': 'Estimated out of stock in 2 days.',
        'restock_amount': '100',
        'arrival_date': 'Arriving Oct 24'
    },
    {
        'name': 'HOLISHOUSE TRI-SPINNER',
        'img_url': 'http://cdn.hiconsumption.com/wp-content/uploads/2017/05/Holishouse-Tri-Spinner.jpg',
        'amount': '5 left',
        'description': 'Estimated out of stock in 4 days.',
        'restock_amount': '300',
        'arrival_date': 'Arriving Oct 25'
    },
    {
        'name': 'Amazon Echo Show Black B01J24C0TI',
        'img_url': 'https://cdn.vox-cdn.com/thumbor/G7YBCvj4gPY8k45Lmogr8de7zIs=/0x0:1737x1156/1200x800/filters:focal(731x440:1007x716)/cdn.vox-cdn.com/uploads/chorus_image/image/54685933/C_Fbr9sXoAA3YT_.0.jpg',
        'amount': '8 left',
        'description': 'Estiamted out of stock in 6 days.',
        'restock_amount': '300',
        'arrival_date': 'Arriving Oct 25'
    },
    {
        'name': 'Yeezy Boost 350 V2',
        'img_url': 'https://smhttp-ssl-58252.nexcesscdn.net/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/s/p/sply_grey.jpg',
        'amount': 'Out of stock',
        'description': 'Hot item',
        'restock_amount': '300',
        'arrival_date': 'Arriving Oct 25'
    },
    {
        'name': 'Calvin Klein Faux-Leather Moto Jacket',
        'img_url': 'https://slimages.macysassets.com/is/image/MCY/products/8/optimized/2474358_fpx.tif?op_sharpen=1',
        'amount': '2 left',
        'description': 'Estimated out of stock in 1 day.',
        'restock_amount': '300',
        'arrival_date': 'Arriving Oct 25'
    }
]


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_launch_response(output, reprompt_text):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': None,
        'directives': [
            {
                'type': 'Display.RenderTemplate',
                'template': {
                    'type': 'BodyTemplate6',
                    'token': 'launch',
                    'backgroundImage': {
                        'contentDescription': SKILL_NAME,
                        'sources': [
                            {
                                'url': 'https://i.imgur.com/4luvtkz.png'
                            }
                        ]
                    },
                    'textContent': {
                        'primaryText': {
                            'type': 'RichText',
                            'text': 'Welcome to <b>' + SKILL_NAME + '</b>.'
                        }
                    }
                }
            },
            {
                'type': 'Hint',
                'hint': {
                    'type': 'PlainText',
                    'text': 'update me about the current stock levels'
                }
            }
        ],
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': False
    }

def build_stock_update_response(output, reprompt_text):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': None,
        'directives': [
            {
                'type': 'Display.RenderTemplate',
                'template': {
                    'type': 'ListTemplate2',
                    'token': 'stockwarnings',
                    'title': 'Current stock levels',
                    'listItems': [
                        {
                            'token': item['name'],
                            'image': {
                                'sources': [
                                    {
                                        'url': item['img_url']
                                    }
                                ]
                            },
                            'textContent': {
                                'primaryText': {
                                    'type': 'RichText',
                                    'text': '<b><u>' + item['name'] + '</u></b>'
                                },
                                'secondaryText': {
                                    'type': 'RichText',
                                    'text': '<b><font size="2">[' + item['amount'] + ']</font></b>'
                                },
                                'tertiaryText': {
                                    'type': 'RichText',
                                    'text': '<i><font size="1">' + item['description'] + '</font></i>'
                                }
                            }
                        }
                        for item in STOCK_ITEMS
                    ]
                }
            }
        ],
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': False
    }

def build_confirm_restock_response(output):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': None,
        'directives': [
            {
                'type': 'Display.RenderTemplate',
                'template': {
                    'type': 'ListTemplate1',
                    'token': 'stockconfirm',
                    'title': 'Items to restock',
                    'listItems': [
                        {
                            'token': item['name'],
                            'image': {
                                'sources': [
                                    {
                                        'url': item['img_url']
                                    }
                                ]
                            },
                            'textContent': {
                                'primaryText': {
                                    'type': 'RichText',
                                    'text': '<b><u>' + item[
                                        'name'] + '</u></b>'
                                },
                                'secondaryText': {
                                    'type': 'RichText',
                                    'text': '<b><font size="2">[' + item['restock_amount'] + ' ordered]</font></b>'
                                },
                                'tertiaryText': {
                                    'type': 'RichText',
                                    'text': '<i><font size="1">' + item[
                                        'arrival_date'] + '</font></i>'
                                }
                            }
                        }
                        for item in STOCK_ITEMS
                    ][:2]
                }
            }
        ],
        'shouldEndSession': False
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = 'Welcome'
    speech_output = 'Welcome to ' + SKILL_NAME + '. ' \
                    'What would you like to know?'
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = 'Ask me anything about your store, for example: ' \
                    'Tell me about the current stock levels in the store.'
    should_end_session = False
    return build_response(session_attributes, build_launch_response(
        speech_output, reprompt_text))


def handle_session_end_request():
    card_title = "Goodbye"
    speech_output = "Have a nice day!"
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def get_stock_updates_from_session():
    session_attributes = {}
    speech_output = 'I found ' + NUM_STOCK_ITEMS + ' items that are low on stock. ' \
                    'Which items would you like me to order more of?'
    reprompt_text = 'These items are either out of stock or are about to run' \
                    'out of stock soon. Just let me know if you would like me' \
                    'to restock them for you.'

    return build_response(session_attributes, build_stock_update_response(
        speech_output, reprompt_text))

def select_items_to_restock(intent):
    session_attributes = {}
    should_end_session = False

    if 'item_one' in intent['slots'] and 'item_two' in intent['slots']:
        item1 = intent['slots']['item_one']['value']
        item2 = intent['slots']['item_two']['value']
        session_attributes = {'item1': item1, 'item2': item2}
        speech_output = 'Placing orders to restock items ' + item1 \
                        + ' and ' + item2 + ' for you.'
        return build_response(session_attributes, build_confirm_restock_response(speech_output))



# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == 'GetStockUpdatesIntent':
        return get_stock_updates_from_session()
    elif intent_name == 'RestockSelectedItemsIntent':
        return select_items_to_restock(intent)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
