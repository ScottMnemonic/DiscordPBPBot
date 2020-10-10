#!/usr/bin/env python
import discord
import random
#self-updating
import os
import sys
from os.path import getmtime
from config import TOKEN

#self-update file watcher
WATCHED_FILES=[__file__]
WATCHED_FILES_MTIMES = [(f, getmtime(f)) for f in WATCHED_FILES]

class PBPClient(discord.Client):
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author == client.user:
            return

        if message.content.startswith('!help p'):
            msg = "Player Commands available:"
            msg += "\n> **!rps** <r(ock)|p(aper)|s(cissors)> [#Message]- Run RPS Simulation, with optional Message"
            msg += "\n> *BETA* **!enter** <room name>- Enter an IC Room. Automatically leaves other Rooms."
            msg += "\n> *BETA* **!leave** - Leave all Rooms"
            msg += "\n> *NOT WORKING* **!who** - How many people are in Rooms right now."
            msg += "\n> *NOT WORKING* **!scene-create <name>** - Create a private Scene."
            msg += "\n> *BETA* **!scene-delete <name>** - Create a PDF Backup and schedule deletion of your private Scene. **Cannot be undone**."
            msg += "\n> *BETA* **!scene-invite <name> <user>** - Add someone to your private Scene. Only the Scene Owner or STs can do this"
            msg += "\n> *BETA* **!scene-remove <name> <user>** - Remove someone from your Scene. Only the Scene Owner or STs can do this"
            await message.channel.send(msg)


        if message.content.startswith('!help st'):
            msg = "ST Commands available:"
            msg += "\n> *NOT WORKING* **!server-limits** - Show status of server limitations (Categories, Roles, and Rooms used)"
            await message.channel.send(msg)


        #Room migration Handler
        if message.content.startswith('!enter'):
            target_room = message.content.split()
            return


        #Rock Paper Scissors Handler
        if message.content.startswith('!rps'):
            wasrand = ""
            content = None
            #set Bot marker
            bm = random.randint(0,2)
            if bm == 0:
                bot_choice = "Rock"
            elif bm == 1:
                bot_choice = "Paper"
            elif bm == 2:
                bot_choice = "Scissors"
            #Set player marker
            if '!rps r' in message.content.lower():
                pm = 0
                player_choice = "Rock"
            elif '!rps p' in message.content.lower():
                pm = 1
                player_choice = "Paper"
            elif '!rps s' in message.content.lower():
                pm = 2
                player_choice = "Scissors"
            else:
                wasrand = "*randomly* "
                pm = random.randint(0,2)
                if pm == 0:
                    player_choice = "Rock"
                if pm == 1:
                    player_choice = "Paper"
                if pm == 2:
                    player_choice = "Scissors"
            # 0 draw, 1 loss, 2 win
            if bm == pm:
                result = "**Draw**"
            if bm == 0:
                if pm ==1:
                    result = "**Success**"
                if pm == 2:
                    result = "**Failure**"
            if bm == 1:
                if pm == 0:
                    result = "**Failure**"
                if pm == 2:
                    result = "**Success**"
            if bm == 2:
                if pm == 0:
                    result = "**Success**"
                if pm == 1:
                    result = "**Failure**"
            if '#' in message.content:
                content = "> " + message.content.split('#')[1]
            if content:
                msg = "{2}! {3.author.mention} {4}chose {0}, I chose {1}. Message:\n{5}".format(player_choice, bot_choice, result, message, wasrand, content)
            else:
                msg = "{2}! {3.author.mention} {4}chose {0}, I chose {1}.".format(player_choice, bot_choice, result, message, wasrand)
            await message.channel.send(msg)
            return

    async def on_ready(self):
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')
        return



client = PBPClient()
client.run(TOKEN)
