from instabot import Bot

bot = Bot()
bot.login(username="astra.sha01", password="Sharma#12564")

# Follow a user
bot.follow("the_a_k_sharma")

# Like and comment on a user's most recent post
user_id = bot.get_user_id_from_username("the_a_k_sharma")
media_ids = bot.get_user_medias(user_id, filtration=False)

if media_ids:
    bot.like(media_ids[0])
    bot.comment(media_ids[0], "Great post!")

# Try sending a DM
bot.send_message("Hello from my Python bot!", ["the_a_k_sharma"])
