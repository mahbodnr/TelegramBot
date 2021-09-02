class AdminPanel:
    def __init__(
        self,
        bot,
    ):
        assert bot.database, "A database must be set to use the AdminPanel"
        self.bot = bot

    async def __call__(self, update):
        if update.message:
            msg_text = update.message.text
            chat_id = update.message.chat.id

            # Search for user
            if msg_text.startswith('/search'):
                return await self.bot.sendMessage(
                chat_id, "Not Implemented Yet!"
                )
            
            # view user
            else:
                try:
                    user_id = int(msg_text[1:])
                except:
                    return await self.bot.sendMessage(
                    chat_id, 
                    "User id Must be a Number!", 
                    reply_to_message_id = update.message.message_id,
                    )
                user_info = self.bot.database.users.find_one({"id": user_id})
                if not user_info:
                    return await self.bot.sendMessage(
                    chat_id, 
                    "No user found with this chat id!", 
                    reply_to_message_id = update.message.message_id,
                    )
                
                return await self.bot.sendMessage(
                    chat_id,
                    (
                        f"* {user_info['first_name']}"
                        f" {user_info['last_name'] if user_info['last_name'] else None}"
                        f" {({user_info['id']})}"
                        f" @{user_info['username']}" if  user_info['username'] else ''
                    ),
                    reply_to_message_id = update.message.message_id,
                )
