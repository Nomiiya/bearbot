import discord, os, tweepy
from dotenv import load_dotenv

load_dotenv()
APP_ID=os.getenv('APP_ID')
APP_TOKEN=os.getenv('APP_TOKEN')

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

        if message.content.startswith('https://x') or message.content.startswith('https://twitter'):
            msg = message.content
            url = "http://fxtwitter.com/" + msg.split('.com/', 1)[1]
            await message.channel.send(url)

    client.run(APP_TOKEN)

def main():
    discordClient()

main()