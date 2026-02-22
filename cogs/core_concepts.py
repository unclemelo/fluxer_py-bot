import fluxer
from fluxer import Cog

class CoreConcepts(Cog):
    def __init__(self, bot):
        super().__init__(bot)

    @Cog.command(name="cogs")
    async def cogs_command(self, ctx):
        embed = fluxer.Embed(
            title="Understanding Cogs",
            description="Cogs are modules that organize your bot's commands and functionality",
            color=0xff6b6b
        )
        embed.add_field(
            name="What is a Cog?",
            value="A cog is a class that inherits from `fluxer.Cog` and contains related commands, events, and functions.",
            inline=False
        )
        embed.add_field(
            name="Basic Structure",
            value="```python\nfrom fluxer import Cog\n\nclass MyCog(Cog):\n    def __init__(self, bot):\n        super().__init__(bot)\n\nasync def setup(bot):\n    await bot.add_cog(MyCog(bot))\n```",
            inline=False
        )
        embed.add_field(
            name="Benefits",
            value="• **Organization** - Keep related commands together\n• **Maintainability** - Easier to update and debug\n• **Modularity** - Load/unload features dynamically\n• **Scalability** - Great for large projects",
            inline=False
        )
        embed.add_field(
            name="File Organization",
            value="Place all your cogs in the `cogs/` folder. The bot automatically loads all cogs on startup!",
            inline=False
        )
        await ctx.send(embed=embed)

    @Cog.command(name="commands")
    async def commands_command(self, ctx):
        embed = fluxer.Embed(
            title="Creating Commands",
            description="Learn how to create powerful commands with fluxer.py",
            color=0x4ecdc4
        )
        embed.add_field(
            name="Command Decorator",
            value="```python\n@Cog.command(name=\"hello\")\nasync def hello_command(self, ctx):\n    await ctx.send(\"Hello!\")\n```",
            inline=False
        )
        embed.add_field(
            name="Command Parameters",
            value="```python\n@Cog.command(name=\"greet\")\nasync def greet(self, ctx, name: str):\n    await ctx.send(f\"Hello {name}!\")\n```\nUsage: `!greet John`",
            inline=False
        )
        embed.add_field(
            name="Key Points",
            value="• Commands are always `async def`\n• Use `ctx` (context) to access message info\n• First parameter is always `self`\n• Parameters come after `ctx`",
            inline=False
        )
        embed.add_field(
            name="Context Object",
            value="The `ctx` object contains:\n• `ctx.send()` - Send a message\n• `ctx.author` - Command user\n• `ctx.channel` - Where command was used\n• `ctx.message` - The message object",
            inline=False
        )
        await ctx.send(embed=embed)

    @Cog.command(name="events")
    async def events_command(self, ctx):
        embed = fluxer.Embed(
            title="📡 Bot Events",
            description="Respond to events that happen on the Fluxer platform",
            color=0xf8b88b
        )
        embed.add_field(
            name="What are Events?",
            value="Events are triggered when something happens (user joins, message sent, etc.)",
            inline=False
        )
        embed.add_field(
            name="Common Events",
            value="• **@bot.event** - Marks an event handler\n• `on_ready()` - Bot connected and ready\n• `on_message()` - Message received\n• `on_member_join()` - New member joins",
            inline=False
        )
        embed.add_field(
            name="Example: on_ready()",
            value="```python\n@bot.event\nasync def on_ready():\n    print(f\"Bot online as {bot.user}\")\n```",
            inline=False
        )
        embed.add_field(
            name="Example: on_message()",
            value="```python\n@bot.event\nasync def on_message(message):\n    if message.author == bot.user:\n        return\n    print(f\"{message.author}: {message.content}\")\n```",
            inline=False
        )
        await ctx.send(embed=embed)

    @Cog.command(name="intents")
    async def intents_command(self, ctx):
        embed = fluxer.Embed(
            title="Understanding Intents",
            description="Intents control what events your bot can receive",
            color=0x95e1d3
        )
        embed.add_field(
            name="What are Intents?",
            value="Intents are permissions that determine which events your bot receives from the Fluxer platform.",
            inline=False
        )
        embed.add_field(
            name="Why Use Intents?",
            value="• **Privacy** - Bots only receive data they need\n• **Performance** - Reduces unnecessary data\n• **Permissions** - Aligns with platform policies",
            inline=False
        )
        embed.add_field(
            name="Default Intents",
            value="```python\nintents = fluxer.Intents.default()\nintents.message_content = True\nbot = fluxer.Bot(intents=intents)\n```",
            inline=False
        )
        embed.add_field(
            name="Common Intent Flags",
            value="• `message_content` - Read message content\n• `members` - Access member information\n• `guilds` - Access guild/server data",
            inline=False
        )
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(CoreConcepts(bot))
