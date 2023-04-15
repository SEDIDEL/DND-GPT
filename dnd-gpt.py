import os
import openai
import discord
from discord.ext import commands

# Configurar las claves API y tokens usando variables de entorno
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]

# Configurar OpenAI API
openai.api_key = OPENAI_API_KEY

# Configurar el bot de Discord
intents = discord.Intents.all()
intents.typing = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def obtener_respuesta(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text.strip()
    return message

@bot.event
async def on_ready():
    print(f"{bot.user.name} ha iniciado sesión.")

@bot.command(name="dnd")
async def dnd(ctx, *, pregunta):
    prompt = f"Por favor, responde la siguiente pregunta sobre Dungeons & Dragons: {pregunta}"
    respuesta = await obtener_respuesta(prompt)
    await ctx.send(respuesta)

bot.run(DISCORD_TOKEN)
