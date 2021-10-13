import random

def love(lover, targets, target):


    love_list = [f"{lover.display_name} tells {target.display_name} that they are awesome.",
                 f"{lover.display_name} gives {target.display_name} a big hug.",
                 f"{lover.display_name} loves {target.display_name} :heart:",
                 f"{lover.display_name} gently caresses {target.display_name}'s face.",
                 f"{lover.display_name} sends a flying kiss to {target.display_name}.",
                 f"{lover.display_name} takes {target.display_name}'s hand and they walk together into the sunset.",
                 f"{lover.display_name} gives {target.display_name} a massage on their feet.",
                 f"{lover.display_name} and {target.display_name} made sweet love by the fire.",
                 f"{lover.display_name} and {target.display_name} melt affectionately in a warm embrace.",
                 f"{lover.display_name} and {target.display_name} decide to go on a cruise after feeling eachother's heartbeat.",
                 f"After months of awkward glances, {lover.display_name} decides to go and hug {target.display_name} :hugging:",
                 f"\"Hugs are worth more than a thousand words\", said {lover.display_name} when embraced {target.display_name}.",
                 f"{lover.display_name} whispers into {target.display_name}'s ear \"I want you\".",
                 f"{lover.display_name} and {targets[0].display_name} chinese finger cuffed {targets[1].display_name}.",
                 f"{lover.display_name} asked {target.display_name} for a strand of their beautiful hair, for {target.display_name} is the most beautiful creature in the land. {lover.display_name} got three.",
                 f"{lover.display_name} put their best outfit to impress {targets[0].display_name}. Unfortunately {targets[1].display_name} was looking hotter and they went away together. Now, I realize this may not be the love story we wanted to hear but these things happen and are beautiful in a certain way.",
                 f"{lover.display_name} sang a ballad at {target.display_name}'s balcony. That was some terrible singing but the gesture was appreciated and now they are deeply in love.",
                 f"{lover.display_name} and {target.display_name} were ready to make sweet love, but some of {lover.display_name}'s ...eeeer... parts.. wouldn't work so they watched some TV instead. Nothing wrong with that, right? I mean we have all been there sometimes, right?",
                 f"{lover.display_name} donated some sea men to {target.display_name}'s aquarium, how nice is that? All {target.display_name} had to do was suck a hose for a few minutes."]

    love_message = random.choice(love_list)

    return love_message


