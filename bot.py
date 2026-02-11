import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


def gamble():
    # Usamos randint para números aleatórios
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    n3 = random.randint(0, 9)
    
    emoji_format = f"{n1} | {n2} | {n3}"
    
    if n1 == n2 == n3:
        return f"{emoji_format}\nJACKPOT!!! 🎰"
    else:
        return f"{emoji_format}"


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('/lista de comandos'):
        await message.channel.send("X = algum número. palavra = qualquer palavra")
        await message.channel.send("aura, gamble, skibidi, senha, /slap @member, /hello, /roll XnX, /add X X, /test (palavra), /heh X")
    if message.content.startswith('oi cleiton'):
        await message.channel.send("Oi amigo!! Bem-vindo!")
    elif message.content.startswith('tchau cleiton'):
        await message.channel.send("Tchau amigo!! Volte sempre!")
    elif message.content.startswith('cleiton, sanduíche de atum é bom?'):
        await message.channel.send("não")
    elif message.content.startswith('boa cleiton'):
        await message.channel.send("disponha, estou aqui pra ajudar!")
    elif message.content.startswith('cleiton como vai a sua mãe?'):
        await message.channel.send("incrivelmente CASADA")
    elif message.content.startswith('cleiton bobão'):
        await message.channel.send("REPETE *cara de bravo*")
    elif message.content.startswith('cleiton'):
        await message.channel.send("O que foi?? :D")
    elif message.content.startswith('senha'):
        await message.channel.send(gen_pass(10))
        await message.channel.send("NÃO PODE!")
    elif message.content.startswith('skibidi'):
        await message.channel.send("dop dop dop yes yes, skibidi dap dip dip")
    elif message.content.startswith('gamble'):
        resultado = gamble() # Chama a função e guarda o que ela retornar
        await message.channel.send(resultado)
    elif message.content.startswith('aura'):
        await message.channel.send("Tche Tche 67, 1000+ de aura")
    elif message.content.startswith('te amo cleiton'):
        await message.channel.send('Também te amo amigo!')
    else:
        await message.channel.send("")

client.run("Seu Token")
