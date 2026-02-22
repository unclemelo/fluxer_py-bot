import fluxer
from fluxer import Cog

class Features(Cog):
    def __init__(self, bot):
        super().__init__(bot)

    @Cog.command(name="embed")
    async def embed_command(self, ctx):
        embed = fluxer.Embed(
            title="Creating Rich Embeds",
            description="Embeds allow you to create beautifully formatted messages",
            color=0xffd700
        )
        embed.add_field(
            name="Basic Embed",
            value="```python\nembed = fluxer.Embed(\n    title=\"My Embed\",\n    description=\"Hello world!\",\n    color=0xFF5733\n)\nawait ctx.send(embed=embed)\n```",
            inline=False
        )
        embed.add_field(
            name="Adding Fields",
            value="```python\nembed.add_field(\n    name=\"Field Name\",\n    value=\"Field Value\",\n    inline=True\n)\n```",
            inline=False
        )
        embed.add_field(
            name="Adding Footer & Author",
            value="```python\nembed.set_footer(text=\"Footer text\")\nembed.set_author(name=\"Author Name\")\nembed.set_thumbnail(url=\"image_url\")\n```",
            inline=False
        )
        embed.add_field(
            name="Embed Properties",
            value="• `title` - Embed title\n• `description` - Main text\n• `color` - Hex color code (0xFF5733)\n• `url` - Link when title is clicked",
            inline=False
        )
        
        # Send example embed
        example = fluxer.Embed(
            title="Example Embed",
            description="This is what an embed looks like!",
            color=0x00ff00
        )
        example.add_field(name="Field 1", value="Value 1", inline=True)
        example.add_field(name="Field 2", value="Value 2", inline=True)
        
        await ctx.send(embed=embed)
        await ctx.send("Here's an example:", embed=example)

    @Cog.command(name="async")
    async def async_command(self, ctx):
        embed = fluxer.Embed(
            title="Async/Await in Python",
            description="Understanding asynchronous programming with fluxer.py",
            color=0x00bfff
        )
        embed.add_field(
            name="What is Async?",
            value="Async allows your bot to do multiple things at once without blocking. This keeps your bot responsive!",
            inline=False
        )
        embed.add_field(
            name="async/await Keywords",
            value="```python\n# Define async function\nasync def my_function():\n    # Do something\n    await some_async_operation()\n    # Continue\n```",
            inline=False
        )
        embed.add_field(
            name="Why Use Async?",
            value="• **Non-blocking** - Bot doesn't freeze while waiting\n• **Efficient** - Handle multiple commands at once\n• **Responsive** - Better user experience",
            inline=False
        )
        embed.add_field(
            name="Common Async Operations",
            value="• `await ctx.send()` - Send a message\n• `await asyncio.sleep(seconds)` - Wait\n• `await some_api.fetch_data()` - Get data",
            inline=False
        )
        embed.add_field(
            name="Remember",
            value="All command functions in fluxer.py are `async def`! You must use `await` to call other async functions.",
            inline=False
        )
        await ctx.send(embed=embed)

    @Cog.command(name="context")
    async def context_command(self, ctx):
        embed = fluxer.Embed(
            title="Understanding Context",
            description="The `ctx` object contains all command execution information",
            color=0xff69b4
        )
        embed.add_field(
            name="What is Context?",
            value="The `ctx` (context) parameter in commands contains information about how and where the command was invoked.",
            inline=False
        )
        embed.add_field(
            name="Essential ctx Properties",
            value="• `ctx.author` - The user who ran the command\n• `ctx.channel` - The channel where command was used\n• `ctx.message` - The message object\n• `ctx.bot` - Reference to the bot",
            inline=False
        )
        embed.add_field(
            name="Useful ctx Methods",
            value="• `await ctx.send(message)` - Send text\n• `await ctx.send(embed=embed)` - Send embed\n• `await ctx.reply(message)` - Reply to message",
            inline=False
        )
        embed.add_field(
            name="Example Usage",
            value="```python\n@Cog.command(name=\"userinfo\")\nasync def userinfo(self, ctx):\n    user = ctx.author\n    await ctx.send(f\"Username: {user}\")\n```",
            inline=False
        )
        await ctx.send(embed=embed)

    @Cog.command(name="decorators")
    async def decorators_command(self, ctx):
        embed = fluxer.Embed(
            title="Using Decorators",
            description="Decorators are powerful tools for adding functionality to functions",
            color=0xda70d6
        )
        embed.add_field(
            name="What is a Decorator?",
            value="A decorator is a function that wraps another function and modifies its behavior without changing the original function.",
            inline=False
        )
        embed.add_field(
            name="Common Decorators in fluxer.py",
            value="• `@Cog.command()` - Makes a function a command\n• `@bot.event` - Marks an event handler\n• `@Cog.listener()` - Alternative event syntax",
            inline=False
        )
        embed.add_field(
            name="Command Decorator Options",
            value="```python\n@Cog.command(name=\"hello\", help=\"Says hello\")\nasync def hello(self, ctx):\n    await ctx.send(\"Hello!\")\n```",
            inline=False
        )
        embed.add_field(
            name="Creating Custom Decorators",
            value="```python\ndef admin_only(func):\n    async def wrapper(self, ctx, *args):\n        if ctx.author.is_admin:\n            return await func(self, ctx, *args)\n    return wrapper\n```",
            inline=False
        )
        embed.add_field(
            name="Key Points",
            value="• Decorators start with `@`\n• They go directly above a function\n• They modify function behavior\n• Very useful for permissions and checks",
            inline=False
        )
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Features(bot))
