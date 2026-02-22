# Fluxer Python Bot

A Fluxer bot built with [fluxer.py](https://github.com/akarealemil/fluxer.py) that demonstrates the features and capabilities of the fluxer.py library.

## Overview

This is a modular Fluxer bot that leverages the fluxer.py library to provide a flexible and extensible command-based system. The bot implements proper logging, dynamically loads command modules (cogs), and handles async operations efficiently.

## Features

- **Fluxer Bot**: Built on fluxer.py library
- **Modular Architecture**: Cog-based command system for easy extensibility
- **Color-Coded Logging**: Rich console output with timestamps and severity levels
- **Easy Configuration**: Environment variable support via `.env` file
- **Error Handling**: Graceful error handling for startup and command loading
- **Help Command**: Built-in help system to display available commands

## Requirements

- Python 3.8 or higher
- Dependencies listed in `requirements.txt`:
  - `fluxer.py`: Fluxer bot library
  - `python-dotenv`: Environment variable management
  - `colorama`: Cross-platform colored terminal output

## Installation

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/unclemelo/fluxer_py-bot
   cd fluxer_py-bot
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the root directory and add your Fluxer bot token:
   ```
   TOKEN=your_fluxer_bot_token_here
   ```

## Configuration

### Environment Variables

The bot requires the following environment variables in a `.env` file:

| Variable | Description |
|----------|-------------|
| `TOKEN` | Your Fluxer bot token (required) |

### Fluxer Bot Setup

1. Obtain your Fluxer bot token from the Fluxer platform
2. Copy the bot token and add it to your `.env` file
3. Ensure you have the necessary permissions to run the bot

## Usage

### Running the Bot

```bash
python bot.py
```

The bot will:
1. Load environment variables from the `.env` file
2. Initialize with default intents and enable message content
3. Load all cogs from the `cogs/` directory
4. Connect to Fluxer and log in
5. Display status messages in the console

### Available Commands

#### General Commands
| Command | Description |
|---------|-------------|
| `!help` | Displays the main help menu with all available command categories |
| `!repo` | Provides a link to the fluxer.py GitHub repository |
| `!info` | Shows information about the fluxer.py library |

#### Getting Started Commands
| Command | Description |
|---------|-------------|
| `!setup` | Step-by-step guide to set up your first bot |
| `!requirements` | Lists system and Python package requirements |
| `!config` | Configuration guide for `.env`, intents, and tokens |

#### Core Concepts Commands
| Command | Description |
|---------|-------------|
| `!cogs` | Learn about cogs and how to organize your bot with modules |
| `!commands` | How to create and structure bot commands |
| `!events` | Understanding bot events and event listeners |
| `!intents` | What intents are and why they matter for permissions |

#### Features & Techniques Commands
| Command | Description |
|---------|-------------|
| `!embed` | Creating beautiful rich embeds for messages |
| `!async` | Understanding async/await in Python |
| `!context` | The `ctx` object and its properties |
| `!decorators` | Using decorators effectively in your bot |

#### Advanced Topics Commands
| Command | Description |
|---------|-------------|
| `!error-handling` | Error handling best practices and patterns |
| `!logging` | Setting up logging for your bot |
| `!database` | Data persistence with SQLite and JSON |

#### Resources Commands
| Command | Description |
|---------|-------------|
| `!docs` | Links to documentation and learning resources |
| `!examples` | Common code examples and patterns |
| `!tutorial` | Step-by-step tutorials for learning fluxer.py |

### Adding New Commands

1. Create a new Python file in the `cogs/` directory
2. Define a class that inherits from `fluxer.Cog`
3. Add command methods using the `@Cog.command()` decorator
4. Create an async `setup()` function that adds the cog to the bot

Example cog structure:
```python
import fluxer
from fluxer import Cog

class MyCog(Cog):
    def __init__(self, bot):
        super().__init__(bot)

    @Cog.command(name="mycommand")
    async def my_command(self, ctx):
        await ctx.send("Hello!")

async def setup(bot):
    await bot.add_cog(MyCog(bot))
```

## Project Structure

```
fluxer_py-bot/
├── bot.py                      # Main bot entry point
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── LICENSE                     # License file
├── .env                        # Environment variables (not in repo)
├── __pycache__/                # Python cache directory
├── cogs/                       # Command modules (cogs)
│   ├── help.py                # Help and general commands
│   ├── getting_started.py      # Setup and configuration commands
│   ├── core_concepts.py        # Core learning concepts
│   ├── features.py             # Features and techniques
│   ├── advanced.py             # Advanced topics and patterns
│   ├── resources.py            # Resources and tutorials
│   └── __pycache__/            # Cache directory
└── utils/                      # Utility modules
    ├── log.py                  # Custom logging utility
    └── __pycache__/            # Cache directory
```

## Logging

The bot uses a custom logging system with color-coded severity levels:

- **[INFO]** (Cyan): General information messages
- **[SUCCESS]** (Green): Successful operations
- **[WARN]** (Yellow): Warning messages
- **[ERROR]** (Red): Error messages
- **[CRITICAL]** (Magenta): Critical system errors

Each log message includes a timestamp in `HH:MM:SS` format.

## Troubleshooting

### Bot doesn't connect
- Verify your `TOKEN` is correct in the `.env` file
- Ensure the bot has the necessary permissions in Fluxer
- Check your internet connection

### Cogs fail to load
- Check the console output for specific error messages
- Verify all cog files follow the proper structure with `async def setup(bot)`
- Ensure there are no syntax errors in your cog files

### Missing dependencies
- Run `pip install -r requirements.txt` to ensure all packages are installed
- Use a virtual environment to avoid version conflicts

## License

See the [LICENSE](LICENSE) file for more information.

## Contributing

Feel free to fork this repository and submit pull requests for improvements or new features!

## Resources

- [fluxer.py Documentation](https://deepwiki.com/akarealemil/fluxer.py/1-overview)
- [Fluxer Official](https://fluxer.app/) (main platform)
