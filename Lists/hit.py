import random

def hit(hitter, targets):


    hit_list = [f"{hitter.display_name} drops an anvil on {targets[0].display_name}'s head.",
                f"{hitter.display_name} yells \"Biiitch\" and slaps {targets[0].display_name}.",
                f"{hitter.display_name} hits {targets[0].display_name} with a pillow.",
                f"{hitter.display_name} goes all Thor and hits {targets[0].display_name} with a hammer.",
                f"{hitter.display_name} hits {targets[0].display_name} with a chair in the back.",
                f"{hitter.display_name} threw {targets[0].display_name} off a cliff.",
                f"{targets[0].display_name} gets crushed under a piano! :musical_keyboard:",
                f"{hitter.display_name} smacked {targets[0].display_name}'s mouth with an old newspaper :newspaper2:",
                f"{hitter.display_name} bitchslapped {targets[0].display_name} so hard than even their ancestors turned dizzy.",
                f"{hitter.display_name} combed {targets[0].display_name} with a rake.",
                f"{hitter.display_name} tagged {targets[1].display_name} and they savagely clotheslined {targets[0].display_name}.",
                f"{hitter.display_name} added a powerful laxative to the beverage {targets[0].display_name} was drinking :poop:",
                f"{hitter.display_name} told {targets[0].display_name} they are ugly. No physical damage was done, but now {targets[0].display_name} is crying inside :smiling_face_with_tear:",
                f"{hitter.display_name} used {targets[0].display_name} as a battering ram to break down a castle door.",
                f"{hitter.display_name} knocks down {targets[0].display_name} with an uppercut and then spits on them on the floor.",
                f"{hitter.display_name} performed a fatality on {targets[0].display_name} :eyes:. Is it me or this thing is getting too violent? :thinking:",
                f"{hitter.display_name} sent {targets[0].display_name} on a one way ticket to the moon. Say hi to Willzyx! :hand_splayed:",
                f"{hitter.display_name} loaded a catapult with {targets[0].display_name} and fired it.",
                f"{hitter.display_name} challenged {targets[0].display_name} to a duel. Unfortunately their pistol didn't fire and got killed....Tough luck I guess.",
                f"{hitter.display_name} and {targets[0].display_name} played chess. {hitter.display_name} lost and smashed the board on {targets[0].display_name}'s head. After the rage subsided {hitter.display_name} said \"good game\" and politely asked for a rematch.",
                ]

    hit_message = random.choice(hit_list)

    return hit_message


