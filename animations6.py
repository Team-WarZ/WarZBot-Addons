import asyncio
from collections import deque
from . import *
from userbot import *
from LEGENDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp

@bot.on(admin_cmd(pattern=f"bigoof$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 7)
    await event.edit(
        "┏━━━┓╋╋╋╋┏━━━┓ \n┃┏━┓┃╋╋╋╋┃┏━┓┃ \n┃┃╋┃┣┓┏┓┏┫┃╋┃┃ \n┃┃╋┃┃┗┛┗┛┃┃╋┃┃ \n┃┗━┛┣┓┏┓┏┫┗━┛┃ \n┗━━━┛┗┛┗┛┗━━━┛"
    )
    animation_chars = [
        "╭━━━╮╱╱╱╭━╮ \n┃╭━╮┃╱╱╱┃╭╯ \n┃┃╱┃┣━━┳╯╰╮ \n┃┃╱┃┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃┃┃ \n╰━━━┻━━╯╰╯ ",
        "╭━━━╮╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃┃┃ \n ╰━━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━┻━━╯╰╯",
        "╭━━━╮╱╱╱╱╱╱╱╱╱╭━╮ \n┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭╯ \n┃┃╱┃┣━━┳━━┳━━┳╯╰╮ \n┃┃╱┃┃╭╮┃╭╮┃╭╮┣╮╭╯ \n┃╰━╯┃╰╯┃╰╯┃╰╯┃┃┃ \n╰━━━┻━━┻━━┻━━╯╰╯",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 7])
        
@bot.on(admin_cmd(pattern="birthday$", outgoing=True))
@bot.on(sudo_cmd(pattern="birthday$", allow_sudo=True))
async def gn(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, "╔╗╔╦══╦═╦═╦╗╔╗\n║╚╝║══║═║═║╚╝║\n║╔╗║╔╗║╔╣╔╩╗╔╝\n╚╝╚╩╝╚╩╝╚╝• B-day •"
    )

@bot.on(admin_cmd(pattern=f"g1$", outgoing=True))
async def payf(event):
    paytext = event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
    )
    await event.edit(pay)

@bot.on(admin_cmd(pattern=f"^uff$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 13)
    animation_chars = [
        "U",
        "Uf",
        "Uff",
        "Ufffff",
        "Uffffff",
        "Ufffffff",
        "Uffffffff",
        "Ufffffffff",
        "Uffffffffff",
        "Ufffffffffff",
        "Uffffffffffff",
        "Ufffffffffffff",
        "Uffffffffffffff",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 13])

@bot.on(admin_cmd(pattern=f"ctext$", outgoing=True))
async def payf(event):
    paytext = event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 8,
        paytext * 8,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 8,
        paytext * 8,
    )
    await event.edit(pay)

@bot.on(admin_cmd(pattern=f"ftext$", outgoing=True))
async def payf(event):
    paytext = event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 8,
        paytext * 8,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 6,
        paytext * 6,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
    )
    await event.edit(pay)


@bot.on(admin_cmd(pattern=f"kf$", outgoing=True))
async def _(event):
    r = random.randint(0, 3)
    logger.debug(r)
    if r == 0:
        await event.edit("┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛")
    else:
        r == 1
        await event.edit("╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯")

@bot.on(admin_cmd(pattern=f"f$", outgoing=True))
async def payf(e):
    paytext = e.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 5,
        paytext * 1,
        paytext * 1,
        paytext * 4,
        paytext * 1,
        paytext * 1,
        paytext * 1,
    )
    await event.edit(pay)
    
@bot.on(admin_cmd(pattern=f"animate$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"animate$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(11)
    await edit_or_reply(event, "animate")
    animation_chars = [
        f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
        f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
        f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
        f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
        f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
        f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
        f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n", 
        f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
        f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
        f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n", 
        f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval) 
        await event.edit(animation_chars[i%192])
        
        
@borg.on(admin_cmd(pattern=r"^Tlol"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🤔🧐🤨🤔🧐🤨"))
    for _ in range(999):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)
    
@borg.on(admin_cmd(pattern=r"^Lol"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("😂🤣😂🤣😂🤣"))
    for _ in range(999):
        await asyncio.sleep(1)
        await event.edit("".join(deq))
        deq.rotate(1)

@bot.on(admin_cmd(pattern=f"chutiye$"))
@bot.on(sudo_cmd(pattern=f"chutiye$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 4
    animation_ttl = range(0, 82)
    event = await edit_or_reply(event, "ThInKiNg...")
    animation_chars = [
        "Maderchod- MOTHERFUCKER",
        "Bhosadike-BORN FROM A ROTTEN PUSSY",
        "Bhen chod-Sister fucker",
        "Bhadhava- Pimp",
        "Bhadhava- Pimp",
        "Chodu- Fucker",
        "Chutiya- Fucker, bastard",
        "Gaand- ASS",
        "Gaandu-Asshole",
        "Gadha Bakland- Idiot",
        "Lauda Lund- Penis, dick, cock",
        "Hijra- Gay, Transsexual",
        "Kuttiya- Bitch",
        "Paad- FART",
        "Randi- HOOKER",
        "Saala kutta- Bloody dog",
        "Saali kutti- Bloody bitch",
        "Tatti- Shit",
        "Kamina- bastard",
        "Chut ke pasine mein talay huye bhajiye- Snack fried in pussy sweat",
        "Chut ke dhakkan- Pussy lid",
        "Chut ke gulam- Pussy whipped",
        "Chutiya ka bheja ghas khane gaya hai- idiot’s brain has gone to eat grass",
        "Choot marani ka- Pussy whipped",
        "Choot ka baal- Hair of vagina",
        "Chipkali ke jhaat ke baal- Lizard’s cunt hairs",
        "Chipkali ke jhaat ke paseene- Sweat of Lizard’s pubic hair",
        "Chipkali ke gaand ke pasine-  Sweat of a lizard’s ass",
        "Chipkali ke chut ke pasine- Sweat of reptiles cunt",
        "Chipkali ki bhigi chut- Wet pussy of a wall lizard",
        "Chinaal ke gadde ke nipple ke baal ke joon- Prostitute’s breast’s nipple’s hair’s lice",
        "Chullu bhar muth mein doob mar-  Drown yourself in a handful of semen",
        "Cuntmama- Vaginal uncle",
        "Chhed- Vagina,Hole",
        "Apni gaand mein muthi daal- Put your fist up your ass",
        "Apni lund choos- Go and suck your own dick",
        "Apni ma ko ja choos- Go suck your mom",
        "Bhen ke laude- Sister’s dick",
        "Bhen ke takke: Go and suck your sister’s balls",
        "Abla naari tera buble bhaari-  woman, your tits are huge",
        "Bhonsri-Waalaa- You fucker",
        "Bhadwe ka awlat- Son of a pimp",
        "Bhains ki aulad- Son of a buffalo",
        "Buddha Khoosat- Old fart",
        "Bol teri gand kaise maru- let me know how to fuck you in the ass",
        "Bur ki chatani- Ketchup of cunt",
        "Chunni- Clit",
        "Chinaal- Whore",
        "Chudai khana- Whore house",
        "Chudan chuda- Fucking games",
        "Chut ka pujari- pussy worshipper",
        "Chut ka bhoot- Vaginal Ghost",
        "Gaand ka makhan- Butter from the ass",
        "Gaand main lassan- Garlic in ass",
        "Gaand main danda- Stick in ass",
        "Gaand main keera- Bug up your ass",
        "Gaand mein bambu- A bambooup your ass",
        "Gaandfat- Busted ass",
        "Pote kitne bhi bade ho, lund ke niche hi rehte hai- However big the balls might be, they have to stay beneath the penis",
        "Hazaar lund teri gaand main-Thousand dicks in your ass",
        "Jhat ke baal- Pubic hair",
        "Jhaant ke pissu- Bug of pubic hair",
        "Kadak Mall- Sexy Girl",
        "Kali Choot Ke Safaid Jhaat- White hair of a black pussy",
        "Khotey ki aulda- Son of donkey",
        "Kutte ka awlat- Son of a dog",
        "Kutte ki jat- Breed of dog",
        "Kutte ke tatte- Dog’s balls",
        "Kutte ke poot, teri maa ki choot-  Son of a dog, your mother’s pussy",
        "Lavde ke bal- Hair on your penis",
        "muh mei lele: Suck my dick",
        "Lund Chus: Suck dick",
        "Lund Ke Pasine- Sweat of dick",
        "Meri Gand Ka Khatmal: Bug of my Ass",
        "Moot, Mootna- Piss off",
        "Najayaz paidaish- Illegitimately born",
        "Randi khana- whore house",
        "Sadi hui gaand- Stinking ass",
        "Teri gaand main kute ka lund- A dog’s dick in your ass",
        "Teri maa ka bhosda- Your mother’s breasts",
        "Teri maa ki chut- Your mother’s pussy",
        "Tere gaand mein keede paday- May worms infest your ass-hole",
        "Ullu ke pathe- Idiot",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 82])

@borg.on(admin_cmd(pattern=f"sadmin", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 13)
    await event.edit("sadmin")
    animation_chars = [



            "@aaaaaaaaaaaaadddddddddddddmmmmmmmmmmmmmiiiiiiiiiiiiinnnnnnnnnnnnn",

            "@aaaaaaaaaaaaddddddddddddmmmmmmmmmmmmiiiiiiiiiiiinnnnnnnnnnnn",    

            "@aaaaaaaaaaadddddddddddmmmmmmmmmmmiiiiiiiiiiinnnnnnnnnnn",

            "@aaaaaaaaaaddddddddddmmmmmmmmmmiiiiiiiiiinnnnnnnnnn",

            "@aaaaaaaaadddddddddmmmmmmmmmiiiiiiiiinnnnnnnnn",

            "@aaaaaaaaddddddddmmmmmmmmiiiiiiiinnnnnnnn",

            "@aaaaaaadddddddmmmmmmmiiiiiiinnnnnnn",

            "@aaaaaaddddddmmmmmmiiiiiinnnnnn",

            "@aaaaadddddmmmmmiiiiinnnnn",    

            "@aaaaddddmmmmiiiinnnn",

            "@aaadddmmmiiinnn",

            "@aaddmmiinn",

            "@admin"

        ]

    for i in animation_ttl:
            await asyncio.sleep(1)
            await event.edit(animation_chars[i % 13])


CmdHelp("shoutadmin").add_command(
    'sadmin', None, 'υѕє αи∂ ѕєє'
).add()
CmdHelp("animations6").add_command(
  'bigoof', None, '🇮🇳🇮🇳🇮🇳'
).add_command(
  'g1', None, 'Use and see'
).add_command(
  'uff', None, 'Use and see'
).add_command(
  'ctext', None, 'Use and see'
).add_command(
  'ftext', None, 'Use and see'
).add_command(
  'animate', None, 'Use a d See'
).add_command(
  'kf', None, 'Use and see'
).add_command(
  'f', None, 'Use and see'
).add_command(
  'muth', None, 'Use And See'
).add_command(
  'birthday', None, 'Use And See'
).add_command(
  '^Lol', None, 'Use and See'
).add_command(
  '^Tlol', None, 'Use and See'
).add_command(
  'chutiye', None, 'Animation Abuse'
).add_command(
  "sadmin", None, "Its Shout Admin"
).add_info(
  "Its all Animation Use As Anywhere"
).add_warning(
  "Harmless Module✅"
).add_type(
  "Addons"
).add()

#legendbot
