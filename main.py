import discord
import os
from discord.ext import commands
from discord.ext.commands import CommandNotFound, MissingRequiredArgument

client = commands.Bot(command_prefix="~")
client.remove_command('help')

moderator_role=836095110697451564
staff_role=836101965003358229
FounderAdminRole=836094933785903104
regularAdminRole=836098165210873856
developerRole=853327055394963516

@client.event
async def on_ready():
 await client.change_presence(status=discord.Status.idle, activity=discord.Game(name='discipleship'))
 print("\n\n Bot is Online! \n ------- \n")



@client.command()
@commands.guild_only()
@commands.has_any_role(moderator_role, FounderAdminRole, staff_role, regularAdminRole, developerRole)
async def removerole(ctx, member : discord.Member, role : discord.Role):
    await member.remove_roles(role)
    await ctx.send("**Role Removed!**")

@client.command(aliases=['dl'])
@commands.has_permissions(manage_roles = True)
@commands.guild_only()
async def delrole(ctx, role: discord.Role):
    await client.delete.role(role.server, role)
    await client.say(f"The role {role.name} has been deleted!")
  
@client.command(aliases=['ub'])
@commands.has_permissions(ban_members=True)
@commands.guild_only()
async def unban(ctx, id: int):
    user = await client.fetch.user(id)
    await ctx.guild.unban(user)
    await ctx.send("**Successfully  unbanned!**")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
      await ctx.send(":x: **I couldn't find that command!**")
    if isinstance(error, MissingRequiredArgument):
      await ctx.send("**You forgot to specify your command!**")

@client.command(aliases=['b', 'excommuncate'])
@commands.has_permissions(ban_members=True)
@commands.guild_only()
async def ban(ctx, user: discord.Member, *, reason=None):
  if user == None or user == ctx.message.author:
   return await ctx.channel.send("**You cannot ban yourself!** :rage:")
  await user.ban(reason=reason)
  await ctx.send(f"**{user} has been bannned successfully!**", delete_after=5)
  await ctx.message.delete()

@client.command(aliases=['gr'])
@commands.guild_only()
@commands.has_permissions(manage_roles = True)
async def giverole(ctx, member : discord.Member, role : discord.Role):
    await member.add_roles(role)
    await ctx.send("**Role Added!**")

#Misc

@client.command(aliases=['av'])
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar.url
    embedav = discord.Embed(title="Here is their avatar:", Description="lol", color=0xffffff)
    embedav.set_.image(url=f'{userAvatarUrl}')
    await ctx.send(embed=embedav)

#library

@client.command()
async def library(ctx):
  embedlib = discord.Embed(title="Library", description="This is currently being worked on. Thanks in advance for your patience!")
  embedlib.add_field(name="~trinity", value="***In Development***", inline=False)
  embedlib.set_footer(text="Hope For The Lost ~ Christian Apologetics", icon_url="https://cdn.discordapp.com/avatars/908030197889126481/1d3436efc1bcc8472e54c46f2c10ce64.png?size=1024")
  await ctx.send(embed=embedlib)

@client.command()
async def trinity(ctx):
  embedtri = discord.Embed(title="The Doctrine of the Trinity", description="The Trinitarian doctrine holds that God is one being in three persons. The three persons are co-eternal, co-equal, and co-existent. \n\n The **Holy Spirit** is referred to as a God's breath, and the Holy Spirit has dwelt within Christians since Pentecost. \n\n The Father is who the Son was begotten from. The **Father** has the most authority in the trinity. \n\n The **Son** is the only begotten Son of the Father. The Son is the person who came to earth via the Holy Spirit and Mary to save us from our sins. He is the Ultimate Sacrifice for the sins accrued towards God.", color=0xffffff)
  embedtri.set_footer(text="Hope for the Lost ~ Christian Apologetics", icon_url="https://cdn.discordapp.com/avatars/908030197889126481/1d3436efc1bcc8472e54c46f2c10ce64.png?size=1024")
  embedtri.set_thumbnail(url="https://cdn.discordapp.com/avatars/908030197889126481/1d3436efc1bcc8472e54c46f2c10ce64.png?size=1024")
  await ctx.send(embed=embedtri) 

@client.command()
@commands.guild_only()
async def staff(ctx): 
  embedstaff = discord.Embed(title="Our Staff Team", description="We work hard to share the Gospel and develop a good relationship with our members. If you would like to dm any one of us, feel free to do so! \n\n\n **Admins:** \n\n <@!221495055452471297> \n <@!751556186548994149> \n\n\n **Moderators:** \n\n <@!854173257288777800> \n<@!904780290780717149> \n<@!707530980831002644> \n<@!572560639373869057> \n<@!384309507087663104> \n<@!187552171229839360> \n\n Thanks so much for being a part of this server!")
  embedstaff.set_thumbnail(url="https://cdn.discordapp.com/avatars/908030197889126481/1d3436efc1bcc8472e54c46f2c10ce64.png?size=1024")
  embedstaff.set_footer(text="Hope for the Lost ~ Christian Apologetics", icon_url="https://cdn.discordapp.com/avatars/908030197889126481/1d3436efc1bcc8472e54c46f2c10ce64.png?size=1024")
  await ctx.send(embed=embedstaff)

@client.command()
async def owner(ctx):
  await ctx.send("The Owner is Wing#3678.")

@client.command()
async def jesus(ctx):
  embedjesu = discord.Embed(title="Who is Jesus?", description="Jesus was a man born of a virgin circa 3 A.D. He was raised a young Jewish boy, and he grew up to perform miracles, resurrrect, and ascend to the heavens.")
  embedjesu.set_footer(text="Hope for the Lost ~ Christian Apologetics", icon_url="https://cdn.discordapp.com/avatars/908030197889126481/1d3436efc1bcc8472e54c46f2c10ce64.png?size=1024")
  await ctx.send(embed=embedjesu)

@client.command()
async def salvation(ctx):
  embedsal = discord.Embed(title="", description="")


token = os.environ.get("TOKEN")
client.run(token)