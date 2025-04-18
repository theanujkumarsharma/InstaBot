from instabot import Bot

bot = Bot()
bot.login(username="your_username", password="your_password")

# Follow a user
bot.follow("username")

# Like and comment on a user's most recent post
user_id = bot.get_user_id_from_username("username")
media_ids = bot.get_user_medias(user_id, filtration=False)

if media_ids:
    bot.like(media_ids[0])
    bot.comment(media_ids[0], "Great post!")

# Try sending a DM
bot.send_message("Hello from my Python bot!", ["username"])
