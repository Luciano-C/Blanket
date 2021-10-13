import random
from Conversation.conversation_data import conversation_data
from Conversation.clean_message import clean_message
from Lists.roasting import roasting


def generate_reply(message):

    message_to_reply = clean_message(message)

    tags_picked = []
    for tag in conversation_data:

        for pattern in conversation_data[tag]["patterns"]:
            if pattern != message_to_reply:
                if pattern in message_to_reply and message_to_reply[message_to_reply.index(pattern) + len(pattern)] == " " and message_to_reply[message_to_reply.index(pattern) - 1] == " ":
                    tags_picked.append(tag)
            elif pattern == message_to_reply:
                tags_picked.append(tag)

    if len(tags_picked) == 1:
        reply = random.choice(conversation_data[tags_picked[0]]["responses"])
    elif len(tags_picked) >= 1:
        tags_picked.sort(key = lambda x: conversation_data[x]["priority"], reverse= True)
        reply = random.choice(conversation_data[tags_picked[0]]["responses"])
    else:
        reply = random.choice(roasting)


    return reply


