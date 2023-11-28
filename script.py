import disnake
import telebot
from disnake.ext import commands

print("bot activated(y4qu1m3)")
telegram_bot_token = "your token"
discord_bot_token = "your token"
telegram_chat_id = "your id"

bot = commands.Bot(command_prefix="*", intents=disnake.Intents.all())

@bot.slash_command()
async def say_to_telegram(interaction: disnake.AppCmdInter, message: str):
    try:
        await interaction.response.defer()
        telegram_bot = telebot.TeleBot(telegram_bot_token)
        telegram_bot.send_message(telegram_chat_id, message)
        await interaction.edit_original_response(content="send")
    except Exception as e:
        await interaction.edit_original_response(content=f"error: {str(e)}")

bot.run(discord_bot_token)