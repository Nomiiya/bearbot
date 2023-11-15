import discord, os, tweepy, re
from dotenv import load_dotenv

load_dotenv()
APP_ID=os.getenv('DEV_ID')
APP_TOKEN=os.getenv('DEV_TOKEN')


auth = tweepy.OAuth1UserHandler(consumer_key=os.getenv('TWITTER_KEY'),
                  consumer_secret=os.getenv('TWITTER_KEY_SECRET'),
                  access_token=os.getenv('ACCESS_TOKEN'),
                  access_token_secret=os.getenv('ACCESS_TOKEN_SECRET'))
api = tweepy.API(auth)

def discordClient():
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_message(message):
        if message.author == client.user or message.author.bot:
            return
        for link in re.findall('https:\/\/twitter\.com[\/\w]+', message.content):
            await message.channel.send("http://fxtwitter.com/" + link.split('.com/', 1)[1])
        for link in re.findall('https:\/\/x\.com[\/\w]+', message.content):
            await message.channel.send("http://fxtwitter.com/" + link.split('.com/', 1)[1])

    client.run(APP_TOKEN)

def main():
    discordClient()

main()