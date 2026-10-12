import random
import discord
from bot_logic import gen_pass
sayings = ["A caballo regalado no se le miran los dientes", "A quien madruga, Dios le ayuda", 
"A mal tiempo, buena cara", "A palabras necias, oídos sordos", "A río revuelto, ganancia de pescadores", 
"Agua que no has de beber, déjala correr", "Al mal paso darle prisa", 
"Al que a buen árbol se arrima, buena sombra le cobija",
"Amor con amor se paga", "Ande yo caliente y ríase la gente", 
"Barriga llena, corazón contento", "Camarón que se duerme se lo lleva la corriente",
 "Cada loco con su tema", "Cada oveja con su pareja", "Cuando el río suena, agua lleva",
 "Dime con quién andas y te diré quién eres", "Donde hay patrón, no manda marinero", 
 "El hábito no hace al monje", "El que mucho abarca, poco aprieta"]

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$password'):
        respuesta = gen_pass(10)
        await message.channel.send(respuesta)
    elif message.content.startswith('$saying'):
        respuestas = random.choice(sayings)
        await message.channel.send(respuestas)
    else:
        await message.channel.send(message.content)

client.run("")
