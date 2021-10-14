import discord
import random
from Caps import _01_projected_caps
from Caps import _02_required_caps
from textblob import TextBlob
from Lists.quotes import quotes
from Lists.jokes import jokes
from Lists.roasting import roasting
from Lists.love import love
from Lists.hit import hit


from reply_generator import generate_reply


intents = discord.Intents.default()
intents.members = True

from keep_alive import keep_alive

client = discord.Client(intents=intents,activity=discord.Game(name='-bl help for commands.'))




def es_entero(text):
    try:
        int(text)
        return True
    except:
        return False




@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content.startswith('- bl') and not message.author.bot:
        random_roast = random.choice(roasting)
        await message.channel.send(random_roast)

    if message.content.startswith("-b") and not message.author.bot:

        if message.content == '-bl quote':
            random_quote = random.choice(quotes)
            await message.channel.send(random_quote)

        elif message.content.startswith('-bl quote') and es_entero(str(message.content[10:])):
            number = int(message.content[10:]) - 1
            total_quotes = len(quotes)
            if number >= 0 and number < total_quotes:
                quote = quotes[number]
                await message.channel.send(quote)
            else:
                await message.channel.send(f"That's a poopie number try one from 1-{len(quotes)}")


        elif message.content.startswith('-bl quote') and not es_entero(str(message.content[10:])) and len(message.content) > 9:
            random_roast = random.choice(roasting)
            await message.channel.send(random_roast)


        elif message.content.startswith('-bl joke'):
            random_joke = random.choice(jokes)
            await message.channel.send(random_joke)


        elif message.content == '-bl project caps':
            if message.attachments == []:  # Checks if there is an attachment on the message
                await message.channel.send("You are being ignorant. Attach csv file named <01_rankdata> and in message type <-bl project caps>")
                return
            else:
                split_v1 = str(message.attachments).split("filename='")[1]
                filename = str(split_v1).split("' ")[0]                         #Gets the file name

                if filename == "01_rankdata.csv":
                    await message.attachments[0].save(fp="{}".format(filename)) #Saves the file

                    try:
                        players_ranks = _01_projected_caps.ranks_function()
                        await message.channel.send(
                            f'Projected caps: {players_ranks.loc[len(players_ranks) - 1, "Caps"]} ({players_ranks.loc[len(players_ranks) - 1, "+"]}/{players_ranks.loc[len(players_ranks) - 1, "-"]})',
                        file=discord.File('report_projected_caps.txt'))

                    except:
                        await message.channel.send("That's a poopie file, you are being ignorant. Try another, hee-heee!")

                elif filename != "01_rankdata.csv":
                    await message.channel.send("Attach csv file named <01_rankdata> and in message type <-bl project caps>")



        elif message.content == '-bl caps':
            if message.attachments == []:  # Checks if there is an attachment on the message
                await message.channel.send("You are being ignorant. Attach txt file named <02_levels_tvt> and in message type <-bl caps>")
                return
            else:
                split_v1 = str(message.attachments).split("filename='")[1]
                filename = str(split_v1).split("' ")[0]                         #Gets the file name

                if filename == "02_levels_tvt.txt":
                    await message.attachments[0].save(fp="{}".format(filename)) #Saves the file

                    try:
                        await message.channel.send(f"Caps needed = {_02_required_caps.caps_function()}",
                                                   file=discord.File('report_required_caps.txt'))
                        return

                    except:
                        await message.channel.send("That's a poopie file, you are being ignorant. Try another, hee-heee!")

                elif filename != "02_levels_tvt.txt":
                    await message.channel.send("Attach txt file named <02_levels_tvt> and in message type <-bl caps>")



        elif message.content.startswith('-bl to eng'):
            try:
                to_translate = message.content[10:]
                translator = TextBlob(to_translate)
                translation = translator.translate(to="en")
                translation = str(translation).capitalize()
                await message.channel.send(f"\"{translation}\"")
            except:
                await message.channel.send("I can't translate that, that's ignorant. Try something else.")


        elif message.content.startswith('-bl to spa'):
            try:
                to_translate = message.content[10:]
                translator = TextBlob(to_translate)
                translation = translator.translate(to="es")
                translation = str(translation).capitalize()
                await message.channel.send(f"\"{translation}\"")
            except:
                await message.channel.send("I can't translate that, that's ignorant. Try something else.")


        elif message.content == '-bl help':
            try:
                await message.channel.send('<-bl quote>: Sends a random quote.' + '\n' + '\n' + '<-bl quote #>: Sends quote number #.' + '\n' + '\n' + '<-bl nude>: Sends a random low res nude.' + '\n' + '\n'
                                           + '<-bl joke>: Sends a random joke.' + '\n' + '\n'
                                           + '<-bl project caps> (This requires to attach a csv file named "01_rankdata" obtained from the sppdreplay website and type the command in the message): Projects the caps we can get considering each players current rank. Also provides a possible +2 per day if the player is within 100 elo of their next rank and -2 per day is the player is within 100 points from their rank below.'
                                           + '\n' + '\n'
                                           + '<-bl caps> (This requires you to attach a txt file named "02_levels_tvt", example file below. It\'s important that the names are in capital and as shown in the game): Calculates the caps required for the list of cards and levels in the file.' + '\n' + '\n'
                                           + '<-bl to eng (message)>: Translates the message to english.' + '\n' + '\n'
                                           + '<-bl to spa (message)>: Translates the message to spanish.' + '\n' + '\n'
                                           + '<-bl love>: Sends love to a random user.' + '\n' + '\n'
                                           + '<-bl hit>: Hits a random user.' + '\n' + '\n'
                                           + '<-bl love @user>: Sends love to @user.' + '\n' + '\n'
                                           + '<-bl hit @user>: Hits @user.' + '\n' + '\n'
                                           + '<-bl brawl>: Starts a big fight.' + '\n' + '\n'
                                           + '<-bl lovefest>: Starts a lovefest.' + '\n' + '\n'
                                           + '<-bl help>: Shows Blanket\'s commands.' + '\n' + '\n' + 'Note: Remove <> when writing the commands.' + '\n' + '\n' + '\n'
                                           + "**Example of the 02_levels_tvt text file:**", file=discord.File('02_levels_tvt example.PNG'))
                await message.channel.send(file=discord.File("02_levels_tvt - example.txt"))


            except:
                await message.channel.send("No help file available lol")
                return


        elif message.content == '-bl love':

            list_of_members = [member for member in message.guild.members if
                               not member.bot and member != message.author]

            lover = message.author
            targets = random.sample(list_of_members, 2)
            target = random.choice(list_of_members)

            await message.channel.send(love(lover, targets, target))


        elif message.content == '-bl hit':   #Para etiquetar escribir {user.mention}

            list_of_members = [member for member in message.guild.members if
                               not member.bot and member != message.author]

            hitter = message.author
            targets = random.sample(list_of_members, 2)
            target = random.choice(list_of_members)

            await message.channel.send(hit(hitter, targets, target))


        elif message.content.startswith('-bl love') and len(message.mentions) == 1 and not message.mentions[0].bot:

            list_of_members = [member for member in message.guild.members if not member.bot and member != message.author]

            lover = message.author
            targets = [message.mentions[0], random.choice(list_of_members)]
            target = message.mentions[0]

            await message.channel.send(love(lover, targets, target))



        elif message.content.startswith('-bl hit') and len(message.mentions) == 1 and not message.mentions[0].bot:

            list_of_members = [member for member in message.guild.members if not member.bot and member != message.author]

            hitter = message.author
            targets = [message.mentions[0], random.choice(list_of_members)]
            target = message.mentions[0]

            await message.channel.send(hit(hitter, targets, target))

        elif message.content.startswith('-bl love') and len(message.mentions) == 1 and message.mentions[0].bot:
            await message.channel.send("Imagine being in love with a bot :joy:")


        elif message.content.startswith('-bl hit') and len(message.mentions) == 1 and message.mentions[0].bot:

            list_of_members = [member for member in message.guild.members if not member.bot and member != message.author]

            hitter = client.user
            targets = [message.author, random.choice(list_of_members)]
            target = message.author

            await message.channel.send("Hitting bots is not cool." + "\n" + hit(hitter, targets, target))


        elif message.content == '-bl brawl':

            list_of_members = [member for member in message.guild.members if not member.bot]
            mensaje = []

            for fight in range(random.randint(5,8)):
                hitter = random.choice(list_of_members)
                targets = random.sample([member for member in list_of_members if member != hitter],2)
                target = random.choice([member for member in list_of_members if member != hitter])

                mensaje.append(hit(hitter,targets,target))

            await message.channel.send("FIGHT! Ding, ding, ding :bell:" + "\n \n" + "\n \n".join(mensaje))


        elif message.content == '-bl lovefest':

            list_of_members = [member for member in message.guild.members if not member.bot]
            mensaje = []

            for romance in range(random.randint(5,8)):
                lover = random.choice(list_of_members)
                targets = random.sample([member for member in list_of_members if member != lover],2)
                target = random.choice([member for member in list_of_members if member != lover])

                mensaje.append(love(lover,targets,target))

            await message.channel.send("Love is in the air, tee hee hee! :cupid:" + "\n \n" + "\n \n".join(mensaje))

        else:
            random_roast = random.choice(roasting)
            await message.channel.send(random_roast)


    elif "Blanket" in message.clean_content or "blanket" in message.clean_content:
        reply = generate_reply(message)
        await message.channel.send(reply)

keep_alive()
client.run("token")  ## insert discord token here


