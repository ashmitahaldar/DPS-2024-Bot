
botcmdsId = 829361180802940938
spamId = 829242559980896266
shitpostId = 844180316326330428

kek_words = ["lol", "lmao", "LOL", "LMAO", "kek", "kekw", "lolf", "KEK", "XD", "xd", "lmfao"]

starter_kek_replies = ["You're SO funny haha", 
"kek owo", 
"haha that do be funny", 
"hehe", 
"lololololol",
"xD funny"]

def update_kek_replies(reply_list, reply_message):
  reply_list.append(reply_message)
  # if "kekreplies" in db.keys():
  #   kekreplies = db["kekreplies"]
  #   kekreplies.append(reply_message)
  #   db["kekreplies"] = kekreplies
  # else:
  #   db["kekreplies"] = [reply_message]

# def delete_kek_replies(index):
#   kekreplies = db["kekreplies"]
#   if len(kekreplies) > index:
#     del kekreplies[index]
#     db["kekreplies"] = kekreplies

# if msg.startswith("$delKekReply"):
    #   kekreplies = []
    # if "kekreplies" in db.keys():
    #   index = int(msg.split("$delKekReply ",1)[1])
    #   delete_kek_replies(index)
    #   kekreplies = db["kekreplies"]
    #   await message.channel.send(kekreplies)

# kekreply_options = starter_kek_replies
    # if "kekreplies" in db.keys():
    #   kekreply_options += db["kekreplies"]