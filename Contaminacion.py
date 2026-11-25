import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def contaminacion(ctx):
    await ctx.send(f'Hola,aqui te tengo una lista de objetos que posiblemente tengas en tu casa y puedas reciclar!')

@bot.command()
async def papel(ctx):
    await ctx.send(f'Con el papel pueder hacer origamis,crear nuevo papel y decoraciones!')

@bot.command()
async def tela(ctx):
    await ctx.send(f'Puedes crear peluches o icluso objetos que pueden ayudar en la limpieza!')

@bot.command()
async def carton(ctx):
    await ctx.send(f'Con el carton puedes decorar tu habitacion,puedes crear un rascador para gatos,puesdes crear una caja para guardar fotos de recuerdos y mucho mas!')

@bot.command()
async def vidrio(ctx):
    await ctx.send(f'Con los botes de Vidrio puedes guardas especias,sal,pimienta y etc.Porque el vidrio no modifica las propiedades de los alimentos')

@bot.command()
async def arcilla(ctx):
    await ctx.send(f'con la arcilla puedes molerla hasta volverla polvo y puedes hacer una maza de arcilla como si fuera nueva!')

 
