import fluxer
from fluxer import Cog
import subprocess
import os
import sys
import asyncio
import traceback
from datetime import datetime

GITHUB_REPO = "https://github.com/unclemelo/fluxer_py-bot"
DEV_USER_ID = 1473700908232945809

class Updater(Cog):
    def __init__(self, bot):
        super().__init__(bot)

    # -------------------------------------------------
    # Helper: Check for developer role
    # -------------------------------------------------
    async def _is_dev(self, ctx):
        if DEV_USER_ID == 0:
            return True
        return ctx.author.id == DEV_USER_ID

    # -------------------------------------------------
    # Helper: Send error embed
    # -------------------------------------------------
    async def send_error_embed(self, ctx, error: Exception, command_name: str):
        """Sends an informative error message when a command fails."""
        tb = "".join(traceback.format_exception(type(error), error, error.__traceback__))
        embed = fluxer.Embed(
            title=f"⚠️ Error in `{command_name}`",
            description=f"An error occurred while running the `{command_name}` command.",
            color=0xff0000
        )
        embed.add_field(name="Error Type", value=f"`{type(error).__name__}`", inline=True)
        embed.add_field(name="Error Message", value=f"```{str(error)[:500]}```", inline=False)
        embed.set_footer(text="Check console for traceback details.")
        await ctx.send(embed=embed)
        print(f"[Updater Error] {command_name} failed:\n{tb}")

    # -------------------------------------------------
    # !update - main update + restart
    # -------------------------------------------------
    @Cog.command(name="update")
    async def update_bot(self, ctx):
        if not await self._is_dev(ctx):
            return await ctx.send("You are not authorized to run this command.")

        try:
            process = subprocess.run(["git", "pull"], capture_output=True, text=True)
            output = process.stdout.strip() or process.stderr.strip()

            if "Already up to date" in output:
                return await ctx.send("✅ No updates available. The bot is already up to date.")

            embed = fluxer.Embed(
                title="🔁 Bot Updated",
                description="Successfully pulled updates from GitHub and restarting...",
                color=0x00ff00
            )
            embed.add_field(name="GitHub Status", value=f"Updates applied successfully.\n[View on GitHub]({GITHUB_REPO})", inline=False)

            try:
                commits = subprocess.run(["git", "log", "-5", "--pretty=format:• %s (%an)"], capture_output=True, text=True)
                commit_list = commits.stdout.strip()
                embed.add_field(name="Recent Commits", value=f"```\n{commit_list}\n```", inline=False)
            except Exception as e:
                embed.add_field(name="Recent Commits", value=f"Could not retrieve commit log.\nError: {e}", inline=False)

            embed.set_footer(text=f"Updated at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            await ctx.send(embed=embed)

            await asyncio.sleep(3)
            os.execv(sys.executable, ["python3"] + sys.argv)

        except Exception as e:
            await self.send_error_embed(ctx, e, "update")

    # -------------------------------------------------
    # !updatecommits - View recent commits
    # -------------------------------------------------
    @Cog.command(name="updatecommits")
    async def recent_commits(self, ctx):
        if not await self._is_dev(ctx):
            return await ctx.send("You are not authorized to run this command.")

        try:
            process = subprocess.run(["git", "log", "-5", "--pretty=format:• %s (%an)"], capture_output=True, text=True)
            commits = process.stdout.strip() or "No commits found."
            embed = fluxer.Embed(title="📝 Recent Commits", description=f"```\n{commits}\n```", color=0x5865f2)
            await ctx.send(embed=embed)
        except Exception as e:
            await self.send_error_embed(ctx, e, "updatecommits")

    # -------------------------------------------------
    # !updatetest - Simulate update without restart
    # -------------------------------------------------
    @Cog.command(name="updatetest")
    async def test_update(self, ctx):
        if not await self._is_dev(ctx):
            return await ctx.send("You are not authorized to run this command.")

        try:
            process = subprocess.run(["git", "fetch"], capture_output=True, text=True)
            ahead_check = subprocess.run(["git", "status", "-uno"], capture_output=True, text=True)
            embed = fluxer.Embed(title="🧪 Update Test", color=0xffa500)
            embed.add_field(name="Git Fetch Output", value=f"```\n{process.stdout.strip()[:500]}\n```", inline=False)
            embed.add_field(name="Status", value=f"```\n{ahead_check.stdout.strip()[:500]}\n```", inline=False)
            await ctx.send(embed=embed)
        except Exception as e:
            await self.send_error_embed(ctx, e, "updatetest")

    # -------------------------------------------------
    # !updatereload - Reload cogs
    # -------------------------------------------------
    @Cog.command(name="updatereload")
    async def reload_cogs(self, ctx):
        if not await self._is_dev(ctx):
            return await ctx.send("You are not authorized to run this command.")

        try:
            reloaded = []
            failed = []
            for ext in list(self.bot.extensions.keys()):
                try:
                    await self.bot.reload_extension(ext)
                    reloaded.append(ext)
                except Exception as e:
                    failed.append(f"{ext}: {e}")
                    print(f"Failed to reload {ext}: {e}")

            embed = fluxer.Embed(title="♻️ Reloaded Cogs", color=0x00ff00)
            embed.add_field(name="Reloaded", value=f"```\n{chr(10).join(reloaded) or 'None'}\n```", inline=False)
            if failed:
                embed.add_field(name="Failed", value=f"```\n{chr(10).join(failed)[:1000]}\n```", inline=False)
            await ctx.send(embed=embed)
        except Exception as e:
            await self.send_error_embed(ctx, e, "updatereload")

    # -------------------------------------------------
    # !updatestatus - Show version and branch
    # -------------------------------------------------
    @Cog.command(name="updatestatus")
    async def update_status(self, ctx):
        try:
            branch = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True).stdout.strip()
            commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()

            embed = fluxer.Embed(title="📊 Bot Status", color=0x0066ff)
            embed.add_field(name="Branch", value=branch or "Unknown", inline=True)
            embed.add_field(name="Commit", value=commit or "Unknown", inline=True)
            embed.add_field(name="GitHub", value=f"[View Repository]({GITHUB_REPO})", inline=False)
            await ctx.send(embed=embed)
        except Exception as e:
            await self.send_error_embed(ctx, e, "updatestatus")

    # -------------------------------------------------
    # !updateinfo - Display info
    # -------------------------------------------------
    @Cog.command(name="updateinfo")
    async def update_info(self, ctx):
        try:
            process = subprocess.run(["git", "log", "-3", "--pretty=format:• %s (%an)"], capture_output=True, text=True)
            current_commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
            
            embed = fluxer.Embed(
                title="ℹ️ Bot Update Info",
                description="Quick summary of recent updates and version info.",
                color=0x9500ff
            )
            embed.add_field(name="Current Commit", value=current_commit or "Unknown", inline=False)
            embed.add_field(name="Recent Commits", value=f"```\n{process.stdout.strip()}\n```", inline=False)
            embed.add_field(name="GitHub Repo", value=f"[View Repository]({GITHUB_REPO})", inline=False)
            await ctx.send(embed=embed)
        except Exception as e:
            await self.send_error_embed(ctx, e, "updateinfo")


async def setup(bot):
    await bot.add_cog(Updater(bot))
