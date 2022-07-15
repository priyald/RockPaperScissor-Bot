import os
import discord
import random
import emojis
from replit import db
from keepalive import keepAlive

if "st" not in db:
  db["st"]=0
if "hs" not in db:
  db["hs"]=0

def emoji(a):
  if a==1:
    return emojis.encode(":rock:")
  elif a==2:
    return emojis.encode(":scissors:")
  elif a==3:
    return emojis.encode(":scroll:")
      
def go(x):
  poss=[1,2,3]
  poss.remove(x)
  y=random.choice(poss)

  if (x==1 and y==2) or (x==2 and y==3) or (x==3 and y==1):
    text="YOU WIN!"
    db["st"]=db["st"]+1
    db["hs"]=max(db["st"],db["hs"])
  
  else:
    text="YOU LOSE"
    db["st"]=0

  return y,text

cli = discord.Client()
token = os.environ['token']

@cli.event 
async def on_ready():
  print("We have logged in as {0.user}.format(cli)")

@cli.event
async def on_message(msg):
  if msg.author == cli.user:
    return

  if msg.content.startswith('highscore##'):
    te="Highscore = " + str(db["hs"])
    await msg.channel.send(te)
    return
  if msg.content.startswith('currstreak##'):
    te="Streak = " + str(db["st"])
    await msg.channel.send(te)
    return
  if msg.content.startswith('#rock'):
    y,t=go(1)
    x=1
  elif msg.content.startswith('#scissor'):
    y,t=go(2)
    x=2
  elif msg.content.startswith('#paper'):
    y,t=go(3)
    x=3
  
  text=emoji(x) + " vs " +emoji(y)
  txt="Streak = " + str(db["st"])
  txt2="HighScore = " + str(db["hs"])
  l= text+"\n"+t+"\n"+txt+"\n"+txt2
  await msg.channel.send(l)

keepAlive()
cli.run(token)
