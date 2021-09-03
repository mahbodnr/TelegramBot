
def mention_by_id(
    content,
    chat_id, 
    parse_mode = "HTML"):
        if parse_mode == "HTML":
            return f'<a href="tg://user?id={chat_id}">{content}</a>'
        elif parse_mode == "Markdown":
            return '[{content}](tg://user?id={chat_id})'

        else:
            raise ValueError("parse_mode not valid: %s" % parse_mode)

def glance(update):
    for message_type in { 
            "message",
            "edited_message",
            "channel_post",
            "edited_channel_post",
            "inline_query",
            "chosen_inline_result",
            "callback_query",
            "shipping_query",
            "pre_checkout_query",
            "poll",
            "poll_answer",
            "my_chat_member",
            "chat_member",
        }:
            if (getattr(update, message_type)):
                pass # TODO