import discord
from discord.ext import commands
import requests
import re

class IPInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # Check if the message is from the desired channel
        if message.channel.id == 1218597076728811640:
            # Extract IP address from message content
            ip_address = self.extract_ip_address(message.content)
            if ip_address:
                # Make a request to get IP info and send the result
                await self.get_ip_info(message.channel, ip_address)

    def extract_ip_address(self, message_content):
        # Define a regex pattern to match IP addresses
        ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
        
        # Search for IP addresses in the message content
        match = re.search(ip_pattern, message_content)
        
        if match:
            return match.group()  # Return the first matched IP address
        else:
            return None  # Return None if no IP address is found

    async def get_ip_info(self, channel, ip_address):
        # Make a GET request to the IP geolocation API
        response = requests.get(f"https://ipinfo.io/{ip_address}?token=dde603e0e1892b")
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Extract relevant information from the response
            ip = data.get('ip', 'Unknown')
            loc = data.get('loc', 'Unknown')
            country = data.get('country', 'Unknown')
            region = data.get('region', 'Unknown')
            city = data.get('city', 'Unknown')
            isp = data.get('org', 'Unknown')
            
            # Construct an embed with the retrieved information
            embed = discord.Embed(title="IP Information", color=discord.Color.blue())
            embed.add_field(name="IP Address", value=ip, inline=False)
            embed.add_field(name="Loc", value=loc, inline=False)
            embed.add_field(name="Country", value=country, inline=True)
            embed.add_field(name="Region", value=region, inline=True)
            embed.add_field(name="City", value=city, inline=True)
            embed.add_field(name="ISP", value=isp, inline=False)
            
            # Send the embed as a message
            await channel.send(embed=embed)
        else:
            await channel.send("Failed to retrieve information for the provided IP address.")


async def setup(bot):
    await bot.add_cog(IPInfo(bot))
