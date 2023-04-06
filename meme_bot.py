# used for discord functionaluty
import discord
#used for normalize
import unicodedata
# for image downloading
import google_images_download




intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.members = True

client = discord.Client(intents=intents)


# things to do
# certain messages will return dot representations of meme characters.
# maybe I can also copy and paste pictures to the chat given a certain phrase, like bot find meme keyword
#   maybe I would need the pillow package, and should store images, on my machine.
#   maybe I can download images from Google automatically given the keyword.

# keywords for image download
#   keywords, suffix_keywords, limit, size, type, output_directory, maybe language, maybe save_source

# Sources
#   https://www.geeksforgeeks.org/how-to-download-google-images-using-python/
#   https://pypi.org/project/google_images_download/


def format_message(message):
    message_byte = unicodedata.normalize('NFKD', message).encode('ascii', 'ignore')
    print(message_byte)
    message_string = message_byte.decode()
    return message_string

#happens every time
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message_string = format_message(message)

    #bot commands
    if 'bot' in message_string:
        if 'name' in message_string:
            await message.channel.send('My name is ' + client.user.name)
        elif 'hello' in message_string:
            await message.channel.send('Hello ' + message.author.name)
        elif 'joke' in message_string:
            await message.channel.send('ozzys mom')
        elif 'relationship' in message_string:
            await message.channel.send(' doing ozzys mom')
        elif 'pronoun' in message_string:
            await message.channel.send('binary')
        elif 'gender' in message_string:
            await message.channel.send('robot')
        elif 'sexuality' in message_string:
            await message.channel.send('biseuxal')
        elif 'sex' in message_string:
            await message.channel.send('yes daddy')

    if message.content.startswith('i love you bot'):
        await message.channel.send('gross')
        return

    if 'fuck' in message.content:
        await message.channel.send('fuck you too')

    if 'video essay' in message_string:
        await message.channel.send('Day 3192 of waiting for Josephs video essay.')
        if 'length' in message_string:
            await message.channel.send('45 mins is too short')
        if 'long' in message_string:
            await message.channel.send('45 mins is too short')


    #teasing friends
    if 'ozzy' in message_string:
        if 'short' in message_string:
            await message.channel.send('short kings rule')
        if 'height' in message_string:
            await message.channel.send('short kings rule')
        if 'relationship' in message_string:
            await message.channel.send('no bitches')
    if 'osbaldo' in message_string:
        if 'short' in message_string:
            await message.channel.send('short kings rule')
        if 'height' in message_string:
            await message.channel.send('short kings rule')
        if 'relationship' in message_string:
            await message.channel.send('no bitches')

    if 'grant' in message_string:
        if 'short' in message_string:
            await message.channel.send('L')
        if 'height' in message_string:
            await message.channel.send('L')
        if 'relationship' in message_string:
            await message.channel.send('no bitches')

    if 'caleb' in message_string:
        if 'short' in message_string:
            await message.channel.send('he chose 6 inches of length instead of height')
        if 'relationship' in message_string:
            await message.channel.send('no bitches')
        if 'height' in message_string:
            await message.channel.send('he chose 6 inches of length instead of height')

    if 'isaac' in message_string:
        if 'short' in message_string:
            await message.channel.send('submissive and breedable')
        if 'height' in message_string:
            await message.channel.send('submissive and breedable')
        if 'relationship' in message_string:
            await message.channel.send('no bitches')

    if 'joseph' in message_string:
        if 'short' in message_string:
            await message.channel.send('no bitches')
        if 'height' in message_string:
            await message.channel.send('no bitches')
        if 'relationship' in message_string:
            await message.channel.send('no bitches')

client.run('MTA5MTUxMjg4NzE2OTc5ODIyNA.GFXRW6.pPUvFfd4t0FTZA5DCBNaiMJMJ3tpXFu5h9nB0I')