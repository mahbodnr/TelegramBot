from .utils import mention_by_id
from .types import InlineKeyboardMarkup, InlineKeyboardButton

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
                        f" {user_info['last_name'] if user_info['last_name'] else ''}"
                        f" ({mention_by_id(user_info['id'], user_info['id'], 'HTML')})"
                        + (f" @{user_info['username']}" if  user_info['username'] else '')
                    ),
                    reply_to_message_id = update.message.message_id,
                    parse_mode = 'HTML',
                    reply_markup = InlineKeyboardMarkup(
                        inline_keyboard = [[
                            InlineKeyboardButton(
                                text= "View Messages",
                                callback_data= f"getMessages {user_id}",
                            )
                        ]]
                    ),
                )
        
        if update.callback_query:
            chat_id = update.callback_query.from_.id
            return await self.bot.sendMessage(
                chat_id, "callback_query"
                )
