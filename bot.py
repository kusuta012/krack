import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Discord intents
intents = discord.Intents.default()
intents.message_content = True  # Enable message related events
intents.guilds = True  # Enable guild related events

# Create bot instance with command prefix and intents
bot = commands.Bot(command_prefix='k!', intents=intents)


# Event handler for bot ready event
@bot.event
async def on_ready():
    logging.info(f'{bot.user} has connected to Discord!')
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            cog_name = filename[:-3]
            try:
                extension = await bot.load_extension(f'commands.{cog_name}')
                logging.info(f'Loaded extension: {cog_name}, return value: {extension}')
            except Exception as e:
                logging.error(f'Failed to load extension {cog_name}: {e}')

# Start the bot
bot.run(os.getenv('DISCORD_BOT_TOKEN'))
