# jalapeno_bot
This is the code for the japaleno bot. Version control is done on GitHub, and the bot is run on Replit. This is a moderation discord bot that has a variety of commands such as purge, snipe, ping, whois (gives information about a member in the server), invites, ban, and giverole. It can be found in my personal discord server Hot Chili:

https://discord.gg/VkF3z8WmEN

### Add-On File Snipe
This is an additional add-on to replace the current snipe code under the event message deleted. This saves deleted files with the suffix listed below.
In order to use this add-on, must have a "deleted_files.txt"

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
### Add-On Censoring
This is an additional moderation add on function to delete messages with certain words like the North Korean government.

```python
censored_words = ['karam', 'caliente', 'hot']

#message should not be scanned if sent by a bot
@bot.event
async def on_message(message):
  
  for word in censored_words:
    if word in message.content:
      await message.delete()
      break 
      
    await bot.process_commands(message)
```
### Requirements
* discord.py 2.2.3
* discord-py-slash-command 4.2.1 
* Flask 2.3.2
* datetime v3.11.3

### Additional Information
I use the free version of replit and as a result programs close after an hour on inactivity. To keep this bot online all the time, I used uptimerobot which sends requests to the bot in 5 minute intervals to keep the bot online. If you use an IDE without this limitation, delete "keep_alive.py" and the function "keep_alive()" in "main.py" can be deleted.

### Author
This bot is proudly created by Ishan Vemireddy aka RedTachyon19
