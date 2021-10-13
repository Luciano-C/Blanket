import random

def hit(hitter, targets, target):


    hit_list = [f"{hitter.display_name} kicks {target.display_name} in the nuts.",
                f"{hitter.display_name} drops an anvil on {target.display_name}'s head.",
                f"{hitter.display_name} yells \"Biiitch\" and slaps {target.display_name}.",
                f"{hitter.display_name} hits {target.display_name} with a pillow.",
                f"{hitter.display_name} grabs {target.display_name} by the pussy.",
                f"{hitter.display_name} goes all Thor and hits {target.display_name} with a hammer.",
                f"{hitter.display_name} hits {target.display_name} with a chair in the back.",
                f"{hitter.display_name} threw {target.display_name} off a cliff.",
                f"{target.display_name} gets crushed under a piano! :musical_keyboard:",
                f"{hitter.display_name} slaps {target.display_name} with a large :eggplant:",
                f"{hitter.display_name} smacked {target.display_name}'s mouth with an old newspaper :newspaper2:",
                f"{hitter.display_name} bitchslapped {target.display_name} so hard than even their ancestors turned dizzy.",
                f"{hitter.display_name} combed {target.display_name} with a rake.",
                f"{hitter.display_name} tagged {targets[1].display_name} and they savagely clotheslined {targets[0].display_name}.",
                f"{hitter.display_name} added a powerful laxative to the beverage {target.display_name} was drinking :poop:",
                f"{hitter.display_name} told {target.display_name} they are ugly. No physical damage was done, but now {target.display_name} is crying inside :smiling_face_with_tear:",
                f"{hitter.display_name} used {target.display_name} as a battering ram to break down a castle door.",
                f"{hitter.display_name} knocks down {target.display_name} with an uppercut and then spits on them on the floor.",
                f"{hitter.display_name} performed a fatality on {target.display_name} :eyes:. Is it me or this thing is getting too violent? :thinking:", 
                f"{hitter.display_name} sent {target.display_name} on a one way ticket to the moon. Say hi to Willzyx! :hand_splayed:",
                f"{hitter.display_name} loaded a catapult with {target.display_name} and fired it.",
                f"{hitter.display_name} challenged {target.display_name} to a duel. Unfortunately their pistol didn't fire and got killed....Tough luck I guess.",
                f"{hitter.display_name} electrocuted {target.display_name}'s balls! :scream:",
                f"{hitter.display_name} shot {target.display_name} in the dick. That's just not cool, I think {hitter.display_name} owes {target.display_name} an apology.",
                f"{hitter.display_name} gave AIDS to {target.display_name}. Don't ask me how, but at least is not as bad as cancer.",
                f"{hitter.display_name} and {target.display_name} played chess. {hitter.display_name} lost and smashed the board on {target.display_name}'s head. After the rage subsided {hitter.display_name} said \"good game\" and politely asked for a rematch.",
                f"{hitter.display_name} and {targets[1].display_name} sacrificed {targets[0].display_name} to the devil. Merry christmas, everybody! :rabbit: :fox: :bear: :deer:"]

    hit_message = random.choice(hit_list)

    return hit_message


