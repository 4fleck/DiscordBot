import discord
from configBot import TOKEN
from discord import FFmpegPCMAudio
from discord.ext.commands import Bot
import configBot
import requests
import json


class Client(discord.Client):
    Client = discord.Client()
    def get_quote(self):
            response = requests.get(configBot.REQ)
            json_data = json.loads(response.text)
            quote = json_data[0]['q'] + " " + "-" + json_data[0]['a']
            return quote

    @Client.event
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(Client))


    @Client.event
    async def on_message(self,message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.author == Client.user:
            return
        if message.content.startswith('$in'):
            quote = self.get_quote()
            await message.channel.send(quote)
        elif message.content.startswith('$hi'):
            hi = (">>> {0.author} ``` hello ```".format(message))
            await message.channel.send(hi)


    @Client.event
    async def log_out(message):
        if message.content.startswith('$log'):
            message.channel.send("by")

    def runBot(self):
        Client.run(TOKEN)

#client.run(TOKEN)

