from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def shingekin(ctx):
    await ctx.send('はい、なります！w')
@bot.command()
async def dolick(ctx):
    await ctx.send('( ˙꒳˙  )')
    
@bot.command()
async def syobon(ctx):
    await ctx.send('Terraria1.4まだかな～')
    
@bot.command()
async def kantoku(ctx):
    await ctx.send('クラスの分散会の時\n\n運営「時間余ったし、マジカルバナナしよ」\n\n前「ハイジといったらスイス」\n俺「スイスと言ったらロマンシュ語」\n次「＼(^o^)／」\n\n～別の周～\n前「フランクフルトといったらドイツ」\n俺「ドイツといったらヴュルテンベルク」\n次「＼(^o^)／」\n次の人ごめんね()')
   
@bot.command()
async def sirosuke(ctx):
    await ctx.send('ヽ(ﾟ∀｡)ﾉｳｪ')
@bot.command()
async def sirosuke2(ctx):
    await ctx.send('(ﾟ∀ﾟ)ｱﾋｬ')
    
bot.run(token)
