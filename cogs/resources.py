import fluxer
from fluxer import Cog

class Resources(Cog):
    def __init__(self, bot):
        super().__init__(bot)

    @Cog.command(name="docs")
    async def docs_command(self, ctx):
        embed = fluxer.Embed(
            title="Documentation & Resources",
            description="Links to helpful documentation and learning materials",
            color=0x6666ff
        )
        embed.add_field(
            name="Official Resources",
            value="• [fluxer.py GitHub](https://github.com/akarealemil/fluxer.py) - Source code and issues\n• [Fluxer Platform](https://fluxer.app/) - Official Fluxer website",
            inline=False
        )
        embed.add_field(
            name="Python Learning",
            value="• [Python.org Documentation](https://docs.python.org/3/) - Official Python docs\n• [Real Python](https://realpython.com/) - Great tutorials\n• [W3Schools Python](https://www.w3schools.com/python/) - Interactive learning",
            inline=False
        )
        embed.add_field(
            name="Async/Await",
            value="• [Python asyncio docs](https://docs.python.org/3/library/asyncio.html) - Official async documentation\n• [Real Python asyncio](https://realpython.com/async-io-python/) - Beginner-friendly guide",
            inline=False
        )
        embed.add_field(
            name="Community Help",
            value="• GitHub Issues - Report bugs or ask questions\n• Discord Communities - Connect with other bot developers\n• Stack Overflow - Search for solutions",
            inline=False
        )
        await ctx.send(embed=embed)

    @Cog.command(name="examples")
    async def examples_command(self, ctx):
        embed = fluxer.Embed(
            title="Code Examples",
            description="Common code patterns and examples for fluxer.py",
            color=0x00ff66
        )
        embed.add_field(
            name="Simple Command",
            value="```python\n@Cog.command(name=\"ping\")\nasync def ping(self, ctx):\n    await ctx.send(\"Pong!\")\n```",
            inline=False
        )
        embed.add_field(
            name="Command with Arguments",
            value="```python\n@Cog.command(name=\"greet\")\nasync def greet(self, ctx, name: str):\n    await ctx.send(f\"Hello {name}!\")\n```\nUsage: `!greet Alice`",
            inline=False
        )
        embed.add_field(
            name="Event Listener",
            value="```python\n@bot.event\nasync def on_ready():\n    logger.info(f\"Bot logged in as {bot.user}\")\n```",
            inline=False
        )
        embed.add_field(
            name="Send Embed",
            value="```python\nembed = fluxer.Embed(title=\"Hello\", color=0xFF5733)\nawait ctx.send(embed=embed)\n```",
            inline=False
        )
        embed.add_field(
            name="Error Handling",
            value="```python\ntry:\n    data = await get_data()\nexcept Exception as e:\n    await ctx.send(f\"Error: {e}\")\n```",
            inline=False
        )
        await ctx.send(embed=embed)

    @Cog.command(name="tutorial")
    async def tutorial_command(self, ctx):
        embed = fluxer.Embed(
            title="Step-by-Step Tutorials",
            description="Guided tutorials to help you learn fluxer.py development",
            color=0xff9900
        )
        embed.add_field(
            name="Tutorial 1: Your First Bot",
            value="Steps:\n1. Use **!setup** to set up your environment\n2. Use **!requirements** to install dependencies\n3. Create a new bot.py file\n4. Add the startup code from **!examples**\n5. Run your bot!",
            inline=False
        )
        embed.add_field(
            name="Tutorial 2: Creating Commands",
            value="Steps:\n1. Create a new cog file in the `cogs/` folder\n2. Use **!commands** to learn the structure\n3. Define your command using @Cog.command()\n4. Implement your command logic\n5. The bot auto-loads it on startup!",
            inline=False
        )
        embed.add_field(
            name="Tutorial 3: Working with Data",
            value="Steps:\n1. Learn about **!database** options\n2. Choose SQLite or JSON for storage\n3. Create a cog to handle data operations\n4. Save/load user information\n5. Test your data persistence!",
            inline=False
        )
        embed.add_field(
            name="Tutorial 4: Error Handling",
            value="Steps:\n1. Study **!error-handling** techniques\n2. Add try-except blocks to commands\n3. Create a global error handler\n4. Test with invalid inputs\n5. Log errors for debugging!",
            inline=False
        )
        embed.add_field(
            name="Next Steps",
            value="• Build your own custom bot\n• Explore the GitHub repository\n• Join the community\n• Share what you've learned!",
            inline=False
        )
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Resources(bot))
