import discord
import random
from discord.ext import commands
import donkenponkenförsäljning as donken
import statistics

intents = discord.Intents.default()
intents.message_content = True


# Här sätter vi prefixet till komma (,)
bot = commands.Bot(command_prefix=',', intents=intents)

@bot.event
async def on_ready():
    print(f'Inloggad som {bot.user}')
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    await bot.process_commands(message)

skämt_list = ["Vilken tid på året tar militärer sin examen?     Framåt mars", "Vilken fransk byggnad har alltid rätt?    Ej-feltornet.", "Varför spikade Hitler upp judar på väggen?    Han ville få det judesolerat.", "Vad har två ben och blöder?    En halv hund…", "Vad är det för likhet mellan en snöstorm och en man?    Man vet aldrig när den kommer, hur många tum man får eller hur länge den stannar."]
gif_list = ["https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdTFpZ28xc3JzYzU4N2pieG83cDhlNDdmNTdyajZoMXYxY3BwcGdnOSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/LGePaj8mRTPEI/giphy.gif", "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmc4NWdzdGlldjVpbTg3cXNiMGVmYTRkNXV1bG1uZWNidm43cWs5NSZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/GCO5WNzFmlc0vjK8cA/giphy.gif", "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmc4NWdzdGlldjVpbTg3cXNiMGVmYTRkNXV1bG1uZWNidm43cWs5NSZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/ehwuBgKNA2NACoFa7w/giphy.gif", "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3cHEwcWl0M2RtMm13cnMwY256YWFxdmlubGNxazF0ZXQ1enE5c2Z6NiZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/ftHNle25rthTu19OAd/giphy.gif", "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNW8zY2NxM2N1aTJoMm5mb3EyaHI4ZWFrenNlbHFmYWZ4bDdhaWIyYyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3tNAbEPc3CILr3h4K5/giphy.gif"]
slap_gifs_list = ["https://media.giphy.com/media/Gf3AUz3eBNbTW/giphy.gif","https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2NrNWV6Z2U0a29pYnM3OWdhZG0yMGdqdHprd2hqdHRwa3B0OGQxMiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/jauNHUg3yB9ZmDtzOv/giphy.gif","https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2NrNWV6Z2U0a29pYnM3OWdhZG0yMGdqdHprd2hqdHRwa3B0OGQxMiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Xxdv7HeHulKDFAeif1/giphy.gif","https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2NrNWV6Z2U0a29pYnM3OWdhZG0yMGdqdHprd2hqdHRwa3B0OGQxMiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3XlEk2RxPS1m8/giphy.gif"]
slap_messages = ["gav en brutal örfil till","smällde till","knockade nästan","slapade skiten ur"]

# Ditt nya kommando ,hej
@bot.command()
async def hej(ctx):
    await ctx.send('Haaaaaallå där din odugliga jävel! Hur kan jag hjälpa dig?(absolut inte)')

# Kommandot ,namn
@bot.command()
async def namn(ctx):
    await ctx.send('Jag heter Piiiiiiiilevick')

# Kommandot ,ping
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

# Kommandot ,sex
@bot.command()
async def sex(ctx):
    await ctx.send('i love sex')

# Kommandot ,hjälp
@bot.command()
async def hjälp(ctx):
    await ctx.send('Ja har: ,hej ,namn ,ping ,sex ,hjälp ,introduktion ,roll ,skämt')

# Kommandot ,introduktion
@bot.command()
async def introduktion(ctx):
    await ctx.send('Jae boten Pillevick, ja skiter i hu du mår, ja vill bara stängas av...')

# Kommandot ,roll
@bot.command()
async def roll(ctx, min = 1, max = 20):
    await ctx.send(f'de bleevvvvvv... {random.randint(int(min), int(max))}')

# Kommandot ,skämt
@bot.command()
async def skämt(ctx):
    await ctx.send (f'Här e ett dåligt jävla skämmt till dej: {random.choice(skämt_list)}')

# Kommandot ,jah
@bot.command()
async def jah(ctx):
    await ctx.send('https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdTFpZ28xc3JzYzU4N2pieG83cDhlNDdmNTdyajZoMXYxY3BwcGdnOSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/7mI0mLnprQCOs/giphy.gif')

# Kommandot ,gif
@bot.command()
async def gifs(ctx):
    await ctx.send(f"{random.choice(gif_list)}")

# kommandod ,slap
@bot.command()
async def slap(ctx, member: discord.Member=None):
    gif = random.choice(slap_gifs_list)
    text = random.choice(slap_messages)
    await ctx.send(f"👋 {ctx.author.mention} {text} {member.mention}!")
    await ctx.send(gif)
   
# Kommandot ,vänd
@bot.command()
async def vänd(ctx, *, sentence):
    reversed_sentence = sentence[::-1]
    await ctx.send(f"Du skrev {reversed_sentence}")

# Kommandot ,räkna
@bot.command()
async def räkna(ctx, x : int, operator : str, y : int):
    if operator == "+":
        await ctx.send(f'{x} + {y} = {x+y}')
    elif operator == "-":
        await ctx.send(f'{x} - {y} = {x-y}')
    elif operator == "*":
        await ctx.send(f'{x} * {y} = {x*y}')
    elif operator == "/":
        await ctx.send(f'{x} / {y} = {x/y}')

@bot.command()
async def statestik(ctx, *, numbers_str):
        numbers = numbers_str.split(" ")
        numbers = list(map(int, numbers))

        mean = statistics.mean(numbers)
        median = statistics.median(numbers)
        mode = statistics.multimode(numbers)

        await ctx.send(
            f"Medelvärde: {round(mean, 2)}\n"
            f"Medianvärde: {median}\n"
            f"Typvärde: {', '.join(map(str, mode))}"
        )

# Kommandot ,mcd
@bot.command()
async def mcd(ctx):
    for i, money in enumerate(donken.inkomster_per_dag, start=1):
        await ctx.send(f"Dag {i}, Tjänade: {money}")
    

bot.run('MTQ4MTYyODk2MTU1NjY2NDQzMA.Gl8m_a.mtRuHNZKh6FKqVyqJ7lBLimyRqkBHO1c6EJ9JU')