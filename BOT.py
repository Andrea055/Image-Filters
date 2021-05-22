import argparse as arg
import sys
import cv2
import blacknwhite_filter
import discord                                          #import libraries
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as dt
import uuid
import requests
import shutil
from requests import Response
from PIL import Image
import time
import os
import sys
import cartoon_filter
import vintage_filter

client = commands.Bot(command_prefix=".") 
bnw = blacknwhite_filter.BlacknWhite()
crt = cartoon_filter.Cartoonizer()
vntg = vintage_filter.Vintage()



@client.event                                           #message connect!
async def on_ready():
    print("Bot is ready")


@client.command()                                       # blackwhite command and processing 
async def cartoon(ctx):
    try:
        url = ctx.message.attachments[0].url            # check for an image, call exception if none found
    except IndexError:
        print("Error: No attachments")                  # check attachments presence
        await ctx.send("No attachments detected!")
    else:
        if url[0:26] == "https://cdn.discordapp.com":   # look to see if url is from discord
            r = requests.get(url, stream=True)
            imageName = 'nocrt' + '.png'                   # save bw image
            with open(imageName, 'wb') as out_file:
                print('Saving image: ' + imageName)
                shutil.copyfileobj(r.raw, out_file)
    crt.start('nocrt.png')
    await ctx.send('Cartoon!', file=discord.File('Cartoon_version.jpg'))

@client.command()                                       # blackwhite command and processing 
async def bw(ctx):
    try:
        url = ctx.message.attachments[0].url            # check for an image, call exception if none found
    except IndexError:
        print("Error: No attachments")                  # check attachments presence
        await ctx.send("No attachments detected!")
    else:
        if url[0:26] == "https://cdn.discordapp.com":   # look to see if url is from discord
            r = requests.get(url, stream=True)
            imageName = 'nobw' + '.png'                   # save bw image
            with open(imageName, 'wb') as out_file:
                print('Saving image: ' + imageName)
                shutil.copyfileobj(r.raw, out_file)
    bnw.start('nobw.png')
    await ctx.send('BlackAndWhite!', file=discord.File('BlacNwhite_version.jpg'))

@client.command()                                       # blackwhite command and processing 
async def vintage(ctx):
    try:
        url = ctx.message.attachments[0].url            # check for an image, call exception if none found
    except IndexError:
        print("Error: No attachments")                  # check attachments presence
        await ctx.send("No attachments detected!")
    else:
        if url[0:26] == "https://cdn.discordapp.com":   # look to see if url is from discord
            r = requests.get(url, stream=True)
            imageName = 'novintage' + '.png'                   # save bw image
            with open(imageName, 'wb') as out_file:
                print('Saving image: ' + imageName)
                shutil.copyfileobj(r.raw, out_file)
    vntg.start('novintage.png')
    await ctx.send('Vintage!', file=discord.File('Vintage_version.jpg'))
		
client.run('ODQ1MzYzNDQ1Nzk2NzAwMTgw.YKf4Dw.cOFEzcwoZGEXeV0MuLq6P0MLgx0')
		
