from re import compile


# chat setting regex
GET_ALL_CHATS = compile(r"^(getchats|چت ?ها)$")
ADD_NEW_CHAT = compile(r"^(setchat|تنظیم ?چت)$")
