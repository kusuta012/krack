import discord
from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        # Get the bot's latency
        latency = round(self.bot.latency * 1000)  # Latency in milliseconds

        # Get the shard ID
        shard_id = ctx.guild.shard_id if ctx.guild else 0  # Default to 0 if not in a guild

        # Create an embed
        embed = discord.Embed(
            title="Pong!",
            description=f"Latency: {latency} ms\nShard ID: {shard_id}",
            color=discord.Color.green()
        )

        # Send the embed
        await ctx.send(embed=embed)

async def setup(bot):
 await bot.add_cog(Example(bot)) 
