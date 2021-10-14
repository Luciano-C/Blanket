# Blanket
## Discord Bot
Blanket is a discord bot created to perform some tasks to help planning for team wars on the game South Park Phone Destroyer and to spam a bit funny stuff.
The bot is written in Python and uses the library discord.py. I created it while I was learning Python as a way to practice the stuff I was learning at the moment, so probably there are things that could be done more efficiently, but still the bot does everyhing I wanted it to do with no bugs as far as I can tell.

## Libraries used
- Discord
- Textblob
- Random
- Pandas
- Flask
- Threading

## Commands
<ul>
<li>-bl quote: Sends a random quote from a list. </li>
<li>-bl quote #: Sends quote number # from the list. </li>
<li>-bl joke: Sends a random joke.</li>
<li>-bl project caps: This is a game related funcionality. It takes a list of players and their ranks and assings a number or "caps" they are likely to earn in the week based on the rank.</li>
<li>-bl caps: Another game related functionality. Takes a list of cards and levels and calculates the required "caps".</li>
<li>-bl to eng (message): Uses textblob to translate a message to english.</li>
<li>-bl to spa (message): Uses textblob to translate a message to spanish.</li>
<li>-bl love: Uses the member list of the server. Chooses a random love phrase and sends love to a random member. Optional: You can mention a specific member to send love.</li>
<li>-bl hit: Uses the member list of the server. Chooses a random hit phrase and hits a random member. Optional: You can mention a specific member to hit.</li>
<li>-bl brawl: Uses the hit command multiple times to create a big fight.</li>
<li>-bl lovefest: Uses the love command multiple times to create a love fest.</li>
</ul>

## Other features
<ul>
<li>There are some random phrases the bot will say when someone mispells a command as long as it starts with "-b".</li>
<li>The bot has a conversation package which triggers when someone says it's name or mentions it. It's based on dictionaries, each one represents a topic and each topic has a list of patterns to recognize, a list of possible responses and a priority. The bot will take the message, remove the special characters (?,@, #...) and then check each topic for a match in their patterns list. All topics that are a match are then ordered by prioriy and the bot will select a random answer from the topic with the highest priority. If no pattern is recognized the bot will select a random answer from a default list.</li>
</ul>  


