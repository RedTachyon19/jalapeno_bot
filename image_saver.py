#This is not activle used, but just a possibility to inegrated

'''
This can save photos and files sent. Snipe for photos.
Requires a deleted_files.txt
'''

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
