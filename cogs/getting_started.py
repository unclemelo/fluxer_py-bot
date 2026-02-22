import fluxer
from fluxer import Cog

class GettingStarted(Cog):
    def __init__(self, bot):
        super().__init__(bot)

    @Cog.command(name="setup")
    async def setup_command(self, ctx):
        embed = fluxer.Embed(
            title="Setting Up Your First Bot",
            description="Follow these steps to create your first fluxer.py bot!",
            color=0x00ff00
        )
        embed.add_field(
            name="Step 1: Install Python",
            value="Ensure you have Python 3.8 or higher installed on your system.",
            inline=False
        )
        embed.add_field(
            name="Step 2: Create a Project Folder",
            value="```mkdir my_first_bot\ncd my_first_bot```",
            inline=False
        )
        embed.add_field(
            name="Step 3: Create Virtual Environment",
            value="```python -m venv venv\nvenv\\Scripts\\activate```",
            inline=False
        )
        embed.add_field(
            name="Step 4: Install fluxer.py",
            value="```pip install fluxer.py python-dotenv```",
            inline=False
        )
        embed.add_field(
            name="Step 5: Create Your Bot",
            value="Create a `bot.py` file and start coding! Use **!examples** to see sample code.",
            inline=False
        )
        await ctx.send(embed=embed)

    @Cog.command(name="requirements")
    async def requirements_command(self, ctx):
        embed = fluxer.Embed(
            title="Bot Requirements",
            description="Here's what you need to get started with fluxer.py",
            color=0xffa500
        )
        embed.add_field(
            name="System Requirements",
            value="• Python 3.8 or higher\n• pip (Python package manager)\n• A text editor or IDE (VS Code, PyCharm, etc.)",
            inline=False
        )
        embed.add_field(
            name="Python Packages",
            value="• **fluxer.py** - The main library\n• **python-dotenv** - For environment variables\n• **requests** - For HTTP requests (optional)\n• **colorama** - For colored output (optional)",
            inline=False
        )
        embed.add_field(
            name="Install All Requirements",
            value="```bash\npip install -r requirements.txt\n```",
            inline=False
        )
        embed.add_field(
            name="Basic requirements.txt",
            value="```\nfluxer.py\npython-dotenv\nrequests\ncolorama\n```",
            inline=False
        )
        await ctx.send(embed=embed)

    @Cog.command(name="config")
    async def config_command(self, ctx):
        embed = fluxer.Embed(
            title="Configuration Guide",
            description="How to configure your fluxer.py bot",
            color=0x9500ff
        )
        embed.add_field(
            name="Create a .env File",
            value="In your project root, create a `.env` file and add:\n```\nTOKEN=your_fluxer_bot_token_here\n```",
            inline=False
        )
        embed.add_field(
            name="Load Environment Variables",
            value="```python\nfrom dotenv import load_dotenv\nimport os\n\nload_dotenv()\nTOKEN = os.getenv(\"TOKEN\")\n```",
            inline=False
        )
        embed.add_field(
            name="Initialize Your Bot",
            value="```python\nimport fluxer\n\nintents = fluxer.Intents.default()\nintents.message_content = True\n\nbot = fluxer.Bot(intents=intents, command_prefix=\"!\")\n```",
            inline=False
        )
        embed.add_field(
            name="Tips",
            value="• Never commit your `.env` file to version control\n• Add `.env` to your `.gitignore`\n• Keep your token secret and secure",
            inline=False
        )
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(GettingStarted(bot))
