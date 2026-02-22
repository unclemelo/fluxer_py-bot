import fluxer
from fluxer import Cog

class Help(Cog):
    def __init__(self, bot):
        super().__init__(bot)

    @Cog.command(name="help")
    async def help_command(self, ctx):
        embed = fluxer.Embed(
            title="Fluxer.py Educational Bot",
            description="Welcome! This bot is designed to help you learn fluxer.py. Use the commands below to explore different topics."
        )
        
        # General Commands
        embed.add_field(
            name="General Commands",
            value="**!help** - Shows this message\n**!repo** - Fluxer.py GitHub repository\n**!info** - Information about fluxer.py",
            inline=False
        )
        
        # Getting Started
        embed.add_field(
            name="Getting Started",
            value="**!setup** - Setup instructions for your first bot\n**!requirements** - Dependencies you'll need\n**!config** - Configuration guide",
            inline=False
        )
        
        # Core Concepts
        embed.add_field(
            name="Core Concepts",
            value="**!cogs** - Learn about cogs and modules\n**!commands** - How to create commands\n**!events** - Understanding bot events\n**!intents** - What are intents and why they matter",
            inline=False
        )
        
        # Features & Techniques
        embed.add_field(
            name="Features & Techniques",
            value="**!embed** - Creating rich embeds\n**!async** - Async/await in Python\n**!context** - Understanding command context\n**!decorators** - Using decorators effectively",
            inline=False
        )
        
        # Advanced Topics
        embed.add_field(
            name="Advanced Topics",
            value="**!error-handling** - Error handling best practices\n**!logging** - Logging your bot\n**!database** - Storing data persistently",
            inline=False
        )
        
        # Resources
        embed.add_field(
            name="Resources",
            value="**!docs** - Links to documentation\n**!examples** - Code examples\n**!tutorial** - Step-by-step tutorials",
            inline=False
        )

        embed.set_footer(text="Fluxer.py Bot by unclemelo#0001 | Made for learning fluxer.py")

        await ctx.send(embed=embed)

    @Cog.command(name="repo")
    async def repo_command(self, ctx):
        embed = fluxer.Embed(
            title="📦 Fluxer.py Repository",
            description="Check out the official fluxer.py repository on GitHub!",
            color=0x1f1f1f
        )
        embed.add_field(
            name="Repository Link",
            value="[fluxer.py on GitHub](https://github.com/akarealemil/fluxer.py)",
            inline=False
        )
        embed.add_field(
            name="What is fluxer.py?",
            value="A modern, easy-to-use Python library for building bots on the Fluxer platform.",
            inline=False
        )
        await ctx.send(embed=embed)

    @Cog.command(name="info")
    async def info_command(self, ctx):
        embed = fluxer.Embed(
            title="About Fluxer.py",
            description="Fluxer.py is a powerful and user-friendly library for Fluxer bot development.",
            color=0x00a8ff
        )
        embed.add_field(
            name="Key Features",
            value="• Easy-to-use command system\n• Cog-based module architecture\n• Event handling\n• Embed support\n• Error handling\n• Async/await support",
            inline=False
        )
        embed.add_field(
            name="Perfect For",
            value="Building educational bots, custom command systems, and automation tools on the Fluxer platform.",
            inline=False
        )
        embed.add_field(
            name="Get Started",
            value="Use **!setup** to learn how to create your first bot!",
            inline=False
        )
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Help(bot))