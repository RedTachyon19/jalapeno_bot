# jalapeno_bot
This is the code for the japaleno bot. Version control is done on GitHub, and the bot is run on Replit. This is a moderation discord bot that has a variety of commands such as purge, snipe, ping, whois (gives information about a member in the server), invites, ban, and giverole. It can be found in my personal discord server Hot Chili:

https://discord.gg/VkF3z8WmEN

## file snipe add-on
This is an additional add on to replace the current snipe code under the event message deleted. This saves deleted files with the suffix listed below.
In order to use this add on, must have a "deleted_files.txt"

``` python
image_types = ["png", "jpeg", "gif", "jpg"]
@bot.event
async def on_message_delete(message):
  for attachment in message.attachments:
      if any(attachment.filename.lower().endswith(image) for image in image_types):
          await attachment.save(attachment.filename)
          
file = open("deleted_files.txt", "r")
file_len = 0
for line in file:
    if line != "\n":
        file_len += 1
file.close()
```

## additional information
I use the free version of replit and as a result programs close after an hour on inactivity. To keep this bot online all the time, I used uptimerobot which sends requests to the bot in 5 minute intervals to keep the bot online. If you use an IDE without this limitation, delete "keep_alive.py" and the function "keep_alive()" in "main.py" can be deleted.

## Author
This bot is proudly created by Ishan Vemireddy aka RedTachyon19
