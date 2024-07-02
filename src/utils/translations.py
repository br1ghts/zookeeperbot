import discord
from translate import Translator
from discord import Message
from config.config import role_to_language

async def translate_message(message: str, target_language: str) -> str:
    translator = Translator(to_lang=target_language)
    translation = translator.translate(message)
    return translation

async def handle_message_translation(message: Message, bot) -> None:
    translation_role = discord.utils.get(message.guild.roles, name="Translation")
    author_language = None
    for role in message.author.roles:
        if role.name in role_to_language:
            author_language = role_to_language[role.name]
            break

    if translation_role in message.author.roles and author_language:
        if message.mentions:
            for user in message.mentions:
                if translation_role in user.roles:
                    target_lang = None
                    for role in user.roles:
                        if role.name in role_to_language:
                            target_lang = role_to_language[role.name]
                            break
                    if target_lang:
                        translator = Translator(from_lang=author_language, to_lang=target_lang)
                        translation = translator.translate(message.content)
                        custom_message = (
                            f"**{message.author.display_name}** mentioned **{user.display_name}**:\n\n"
                            f"> {message.content}\n\n"
                            f"**Translated to {target_lang.upper()}**:\n"
                            f"> {translation}"
                        )
                        await message.channel.send(custom_message)