import random

def love(lover, targets):


    love_list = [f"{lover.display_name} tells {targets[0].display_name} that they are awesome.",
                 f"{lover.display_name} gives {targets[0].display_name} a big hug.",
                 f"{lover.display_name} loves {targets[0].display_name} :heart:",
                 f"{lover.display_name} gently caresses {targets[0].display_name}'s face.",
                 f"{lover.display_name} sends a flying kiss to {targets[0].display_name}.",
                 f"{lover.display_name} takes {targets[0].display_name}'s hand and they walk together into the sunset.",
                 f"{lover.display_name} gives {targets[0].display_name} a massage on their feet.",
                 f"{lover.display_name} and {targets[0].display_name} melt affectionately in a warm embrace.",
                 f"{lover.display_name} and {targets[0].display_name} decide to go on a cruise after feeling eachother's heartbeat.",
                 f"After months of awkward glances, {lover.display_name} decides to go and hug {targets[0].display_name} :hugging:",
                 f"\"Hugs are worth more than a thousand words\", said {lover.display_name} when embraced {targets[0].display_name}.",
                 f"{lover.display_name} asked {targets[0].display_name} for a strand of their beautiful hair, for {targets[0].display_name} is the most beautiful creature in the land. {lover.display_name} got three.",
                 f"{lover.display_name} put their best outfit to impress {targets[0].display_name}. Unfortunately {targets[1].display_name} was looking hotter and they went away together. Now, I realize this may not be the love story we wanted to hear but these things happen and are beautiful in a certain way.",
                 f"{lover.display_name} sang a ballad at {targets[0].display_name}'s balcony. That was some terrible singing but the gesture was appreciated and now they are deeply in love."]

    love_message = random.choice(love_list)

    return love_message


