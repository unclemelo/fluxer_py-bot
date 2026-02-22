import fluxer
from fluxer import Cog

class Advanced(Cog):
    def __init__(self, bot):
        super().__init__(bot)

    @Cog.command(name="error-handling")
    async def error_handling_command(self, ctx):
        embed = fluxer.Embed(
            title="🛡️ Error Handling Best Practices",
            description="Learn how to handle errors gracefully in your bot",
            color=0xff4444
        )
        embed.add_field(
            name="Try-Except Blocks",
            value="```python\ntry:\n    # Code that might error\n    result = 10 / 0\nexcept ZeroDivisionError:\n    await ctx.send(\"Cannot divide by zero!\")\nexcept Exception as e:\n    await ctx.send(f\"Error: {e}\")\n```",
            inline=False
        )
        embed.add_field(
            name="Global Error Handler",
            value="```python\n@bot.event\nasync def on_command_error(ctx, error):\n    if isinstance(error, commands.CommandNotFound):\n        return\n    await ctx.send(f\"Error: {error}\")\n```",
            inline=False
        )
        embed.add_field(
            name="Types of Errors",
            value="• **ValueError** - Invalid value\n• **TypeError** - Wrong type\n• **KeyError** - Missing dictionary key\n• **IndexError** - Index out of range\n• **ZeroDivisionError** - Division by zero",
            inline=False
        )
        embed.add_field(
            name="Best Practices",
            value="• Always wrap API calls in try-except\n• Log errors for debugging\n• Give users helpful error messages\n• Never crash silently\n• Handle specific exceptions first",
            inline=False
        )
        await ctx.send(embed=embed)

    @Cog.command(name="logging")
    async def logging_command(self, ctx):
        embed = fluxer.Embed(
            title="📝 Logging Your Bot",
            description="Set up logging to track your bot's activity",
            color=0x00cccc
        )
        embed.add_field(
            name="Why Log?",
            value="• Track bot activity and performance\n• Debug issues when they occur\n• Monitor command usage\n• Identify problems quickly",
            inline=False
        )
        embed.add_field(
            name="Basic Logging",
            value="```python\nimport logging\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format='%(asctime)s - %(levelname)s - %(message)s'\n)\nlogger = logging.getLogger(__name__)\n\nlogger.info(\"Bot started\")\nlogger.error(\"Something went wrong\")\n```",
            inline=False
        )
        embed.add_field(
            name="Log Levels",
            value="• **DEBUG** (10) - Detailed info\n• **INFO** (20) - General info\n• **WARNING** (30) - Warning messages\n• **ERROR** (40) - Error messages\n• **CRITICAL** (50) - Critical issues",
            inline=False
        )
        embed.add_field(
            name="Logging to File",
            value="```python\nhandler = logging.FileHandler('bot.log')\nformatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')\nhandler.setFormatter(formatter)\nlogger.addHandler(handler)\n```",
            inline=False
        )
        embed.add_field(
            name="Pro Tips",
            value="• Log important events (startup, shutdown)\n• Log errors with full tracebacks\n• Use appropriate log levels\n• Rotate log files to prevent bloat",
            inline=False
        )
        await ctx.send(embed=embed)

    @Cog.command(name="database")
    async def database_command(self, ctx):
        embed = fluxer.Embed(
            title="🗄️ Storing Data Persistently",
            description="Learn how to save data that persists between bot restarts",
            color=0x00aa44
        )
        embed.add_field(
            name="Why Use a Database?",
            value="• Save user data\n• Track statistics\n• Remember preferences\n• Persist data between restarts",
            inline=False
        )
        embed.add_field(
            name="Simple JSON Storage",
            value="```python\nimport json\n\n# Save data\ndata = {'users': ['alice', 'bob']}\nwith open('data.json', 'w') as f:\n    json.dump(data, f)\n\n# Load data\nwith open('data.json', 'r') as f:\n    data = json.load(f)\n```",
            inline=False
        )
        embed.add_field(
            name="SQLite Database",
            value="```python\nimport sqlite3\n\nconn = sqlite3.connect('bot.db')\ncursor = conn.cursor()\ncursor.execute('CREATE TABLE users (id INTEGER, name TEXT)')\ncursor.execute('INSERT INTO users VALUES (1, \"Alice\")')\nconn.commit()\nconn.close()\n```",
            inline=False
        )
        embed.add_field(
            name="Popular Database Libraries",
            value="• **sqlite3** - Built-in, lightweight\n• **psycopg2** - PostgreSQL\n• **motor** - Async MongoDB\n• **sqlalchemy** - Advanced SQL toolkit",
            inline=False
        )
        embed.add_field(
            name="Best Practices",
            value="• Use async database operations\n• Validate data before storing\n• Implement data backups\n• Use parameterized queries to prevent SQL injection",
            inline=False
        )
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Advanced(bot))
