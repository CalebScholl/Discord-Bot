# used for discord functionaluty
import discord
# used for normalizing special chars and different fonts
import unicodedata
# used to flip things right side up
import upsidedown


intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.members = True

client = discord.Client(intents=intents)

member_list = []
guild_list = []
channel_list = []
replacements_dict = {
    '*': '',
    '~': '',
    '_': '',
    '@': 'a',
    '$': 's',
    '!': 'i',
    '0': 'o'
}

swear_words = open('swearwords.txt', 'r')
swear_words_list_temp = swear_words.readlines()
swear_words_list = []
for item in swear_words_list_temp:
    swear_words_list.append(item.strip('\n'))

swear_words.close()


def profanity_filter(message):
    for item in swear_words_list:
        if item + ' ' in message + ' ':
            return " said " + item + ", what a bad boy."


def format_message(message):
    # maybe make a check for @ and special chars including stuff that looks like letters, 0 to o, ! to i
    # upside down, tiny case
    # different fonts, emojis
    # things ending with swear words
    # horseshitshoe problem because you are comparing the swear word + ' ' with message + ' ',
    # but if I remove the + ' ' on the swear word then stuff like assume would work.
    # Might just let it go.
    # HorseSHITshoe

    # loop through each char in the message
    # use normalize to see if you should flip a char,
    # this has some limitations like flipping weird chars,
    # but if you flip those they should get deleted by normalized

    # maybe check ! for l or for i, same with other special chars,
    # this would need to be done before the chars are removed.


    #maybe make this into a seperate flip method
    #message_string = ''
    #for char in message:
        #char_byte = unicodedata.normalize('NFKD', char).encode('ascii', 'ignore')
        #char_temp = char_byte.decode()
        #if len(char_temp) == 0:
            #if the len is 0 then you need to flip it
            #pass
            #then add the flipped char to the message
        #else:
            #message_string += char_temp



    #need to use these before the normalizer
    message = message.replace('ß', 'b')
    message = message.replace('€', 'e')
    message = message.replace('£', 'f')
    message = message.replace('§', 's')
    #gets rid of new line character, so it can work with multiline swear words.
    message = message.replace('\n', '')


    #you need to evaluate the string in reverse order if it is flipped, also is broken
    #message_temp = ''
    #for char in reversed(message):
        #print(char)
        #if(unicodedata.normalize('NFKD', char).encode('ascii', 'ignore') == 'n'):
            #message_temp += upsidedown.transform(char)
        #else:
            #message_temp += char
        #print(message_temp)

    message_byte = unicodedata.normalize('NFKD', message).encode('ascii', 'ignore')
    print(message_byte)
    message_string = message_byte.decode()

    # removes bold and italics
    message_string = message_string.replace('*', '')
    # removes strikethrough
    message_string = message_string.replace('~', '')
    # removes underline
    message_string = message_string.replace('_', '')
    # replaces @ with a
    message_string = message_string.replace('@', 'a')
    # replace $ with s
    message_string = message_string.replace('$', 's')
    # replace ! with i
    message_string = message_string.replace('!', 'i')
    # replace 0 with o
    message_string = message_string.replace('0', 'o')
    # replace ä with a
    message_string = message_string.replace('ä', 'a')
    # replace š with s
    message_string = message_string.replace('š', 's')
    # replace | with i
    message_string = message_string.replace('|', 'i')
    # replace . with space
    message_string = message_string.replace('.', '')
    # replace , with space
    message_string = message_string.replace(',', '')
    # removes cases
    message_string = message_string.lower()

    print(message_string)
    return message_string

#maybe make this program run everytime i open discord, using task scheduler.
#this will run everytime
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    #gets guilds the bot is in then adds them to a list.
    for guild in client.guilds:
        guild_list.append(guild.name)

    #gets all member from all guilds that the bot is in.
    for guild in client.guilds:
        for member in guild.members:
            print(member)
            member_list.append(member)

    #gets channels from all guilds and adds them to a list
    for guild in client.guilds:
        for channel in guild.channels:
            channel_list.append(channel)
            #general channel id
            if(channel.name == 'general'):
                generalChannelID = channel.id
                #channel = client.get_channel(generalChannelID)
                #await channel.send('ouch')

    #prints activity for each member
    for member in member_list:
        print(member.activity)
        if(member.activity == 'Guild Wars 2'):
            print(member.__str__() + ' has been a bad boy')

    for member in member_list:
        print(member.status)
        if(member.status == 'online'):
            channel = client.get_channel(generalChannelID)
            await channel.send('damn, ' + member + 'is such a bitch')

    #1091511743236280451 gw2sc channel id

    member_list[1].activities

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(message.content)

    #catch edits

    if message.content.startswith('i love you bot'):
        await message.channel.send('gross')
        return

    if message.content.startswith('I love you bot'):
        await message.channel.send('gross')
        return

    if message.content.startswith('print members'):
        await message.channel.send(member_list)

    if message.content.startswith('print guilds'):
        await message.channel.send(guild_list)

    if message.content.startswith('print channels'):
        await message.channel.send(channel_list)

    if 'fuck' in message.content:
        await message.channel.send('fuck you too')

    if 'Fuck' in message.content:
        await message.channel.send('Fuck you too')

    message_string = format_message(message.content)

    if 'horny' in message_string:
        await message.channel.send('go to horny jail')

    if 'deez' in message_string:
        await message.channel.send('suck deez nuts ozzy')

    if 'suck' in message_string:
        if 'ball' in message_string:
            await message.channel.send('suck yourself off')

    if 'ass' in message_string:
        if 'tit' in message_string:
            await message.channel.send('dicks')

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

    if 'controversy' in message_string:
        if 'doom eternal' in message_string:
            await message.channel.send('no you ignoramus')

    if 'tell a joke' in message_string:
        await message.channel.send('ozzys mom')

    if 'tell me a joke' in message_string:
        await message.channel.send('ozzys mom')

    if 'women the same' in message_string:
        await message.channel.send('No. ')

    if 'trans rights' in message_string:
        await message.channel.send('Trans rights are human rights.')

    if 'gay people' in message_string:
        await message.channel.send('Gay people are people too.')

    if 'video essay' in message_string:
        await message.channel.send('Day 3192 of waiting for Josephs video essay.')
        if 'length' in message_string:
            await message.channel.send('45 mins is too short')
        if 'long' in message_string:
            await message.channel.send('45 mins is too short')

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

    #if message.author equals

    try:
        await message.channel.send(message.author.name + profanity_filter(message_string))
    except:
        pass

@client.event
async def on_raw_message_edit(message):
    message_edit = format_message(message.content)
    await message.channel.send(message.author.name + profanity_filter(message_edit))

client.run('MTA5MTUxMjg4NzE2OTc5ODIyNA.GFXRW6.pPUvFfd4t0FTZA5DCBNaiMJMJ3tpXFu5h9nB0I')