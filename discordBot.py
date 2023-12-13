import utils
import discord
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = "?", intents = intents)

@bot.event
async def on_ready():
    print(f'acordei!\nconectado como: {bot.user}')
    # remenber.start()	

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)


@bot.command(name = 'notas') 
async def get_grade(ctx, site, login, password):
    
    # ainda tem coisas para arrumar aqui, muitas coisas
    try:
        notas = utils.get_grades(site, login, password, toStr=False)
        utils.drawText(notas)
        
        embed = discord.Embed(
            title = "Tabela de notas",
            description= "Podem haver erros ou mudanças nas notas",
            color = 0x0000FF)
        file = discord.File('notas.png', filename = 'image.png')
        embed.set_image(url='attachment://image.png')
        
        await ctx.author.send(f'aqui estão suas notas até o momento:\n\n')
        await ctx.send(file=file, embed=embed)
                           
    except discord.errors.Forbidden:
        if notas == False:
            await ctx.send('não encontrei nenhuma nota')
            await ctx.author.send('mas não se preocupe, os professores podem simplesmente não ter postado ainda, pesquise outra vez mais tarte, ou fale diretamente com algum professor')
        else:
            await ctx.send('Não posso enviar menssagens no seu privrado!\ncaso queira receber habilite a opção para receber mensagens de qualquer pessoa.')
    

# ainda não tenho o porque usar algo assim, mas tá aqui no caso de algum dia precisar
@tasks.loop(seconds = 5) 
async def remenber():
    channel = bot.get_channel(1055487703472406538)
    
    await channel.send('eu ainda estou aqui!')

bot.run('MTA1NTQ3ODk5NjM1NzM2MTcyNg.G_c4JD.lATe-AEUyPbL7Q1uPHhD755KM2gPIhnlZbJ46w')
