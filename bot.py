from typing import Union
import asyncio

import httpx

from message import TelegramMessage
from database import Database

class TelegramBot:
    def __init__(
        self, 
        token: str,
        support_id: Union[str, int] = None,
        database: Database= None
        ):
        self.token = token
        self.support_id = support_id
        self.database = database

    async def __call__(
        self,
        method: str,
        json_data: dict,
        ):
        async with httpx.AsyncClient() as client:
            r = await client.post(
                    f"https://api.telegram.org/bot{self.token}/{method}",
                    json=json_data,
            )
        msg = TelegramMessage(r)
        if self.database and hasattr(msg, 'chat'):
            self.database.add_user(msg)
            self.database.add_messages(msg)
        return msg

    def getMe(self):
        """
                A simple method for testing your bot's auth token. Requires no parameters. Returns basic information about the bot in form of a User object.
        """
        return self("getMe", None)

    def logOut(self):
        """
                Use this method to log out from the cloud Bot API server before launching the bot locally. You must log out the bot before running it locally, otherwise there is no guarantee that the bot will receive updates. After a successful call, you can immediately log in on a local server, but will not be able to log in back to the cloud Bot API server for 10 minutes. Returns True on success. Requires no parameters.
        """
        return self("logOut", None)

    def close(self):
        """
                Use this method to close the bot instance before moving it from one local server to another. You need to delete the webhook before calling this method to ensure that the bot isn't launched again after server restart. The method will return error 429 in the first 10 minutes after the bot is launched. Returns True on success. Requires no parameters.
        """
        return self("close", None)

    def sendMessage(
        self,
        chat_id,
        text,
        parse_mode = None,
        entities = None,
        disable_web_page_preview = None,
        disable_notification = None,
        reply_to_message_id = None,
        allow_sending_without_reply = None,
        reply_markup = None,
        ):
        """
        Use this method to send text messages. On success, the sent Message is returned.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param text (String): Text of the message to be sent, 1-4096 characters after entities parsing
        :param parse_mode (String, Optional): Mode for parsing entities in the message text. See formatting options for more details.
        :param entities (Array of MessageEntity, Optional): List of special entities that appear in message text, which can be specified instead of parse_mode
        :param disable_web_page_preview (Boolean, Optional): Disables link previews for links in this message
        :param disable_notification (Boolean, Optional): Sends the message silently. Users will receive a notification with no sound.
        :param reply_to_message_id (Integer, Optional): If the message is a reply, ID of the original message
        :param allow_sending_without_reply (Boolean, Optional): Pass True, if the message should be sent even if the specified replied-to message is not found
        :param reply_markup (InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, Optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("sendMessage", kwargs)

    def forwardMessage(
        self,
        chat_id,
        from_chat_id,
        message_id,
        disable_notification = None,
        ):
        """
        Use this method to forward messages of any kind. Service messages can't be forwarded. On success, the sent Message is returned.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param from_chat_id (Integer or String): Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)
        :param message_id (Integer): Message identifier in the chat specified in from_chat_id
        :param disable_notification (Boolean, Optional): Sends the message silently. Users will receive a notification with no sound.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("forwardMessage", kwargs)

    def copyMessage(
        self,
        chat_id,
        from_chat_id,
        message_id,
        caption = None,
        parse_mode = None,
        caption_entities = None,
        disable_notification = None,
        reply_to_message_id = None,
        allow_sending_without_reply = None,
        reply_markup = None,
        ):
        """
        Use this method to copy messages of any kind. Service messages and invoice messages can't be copied. The method is analogous to the method forwardMessage, but the copied message doesn't have a link to the original message. Returns the MessageId of the sent message on success.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param from_chat_id (Integer or String): Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)
        :param message_id (Integer): Message identifier in the chat specified in from_chat_id
        :param caption (String, Optional): New caption for media, 0-1024 characters after entities parsing. If not specified, the original caption is kept
        :param parse_mode (String, Optional): Mode for parsing entities in the new caption. See formatting options for more details.
        :param caption_entities (Array of MessageEntity, Optional): List of special entities that appear in the new caption, which can be specified instead of parse_mode
        :param disable_notification (Boolean, Optional): Sends the message silently. Users will receive a notification with no sound.
        :param reply_to_message_id (Integer, Optional): If the message is a reply, ID of the original message
        :param allow_sending_without_reply (Boolean, Optional): Pass True, if the message should be sent even if the specified replied-to message is not found
        :param reply_markup (InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, Optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("copyMessage", kwargs)

    def sendPhoto(
        self,
        chat_id,
        photo,
        caption = None,
        parse_mode = None,
        caption_entities = None,
        disable_notification = None,
        reply_to_message_id = None,
        allow_sending_without_reply = None,
        reply_markup = None,
        ):
        """
        Use this method to send photos. On success, the sent Message is returned.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param photo (InputFile or String): Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data. The photo must be at most 10 MB in size. The photo's width and height must not exceed 10000 in total. Width and height ratio must be at most 20. More info on Sending Files \xc2\xbb
        :param caption (String, Optional): Photo caption (may also be used when resending photos by file_id), 0-1024 characters after entities parsing
        :param parse_mode (String, Optional): Mode for parsing entities in the photo caption. See formatting options for more details.
        :param caption_entities (Array of MessageEntity, Optional): List of special entities that appear in the caption, which can be specified instead of parse_mode
        :param disable_notification (Boolean, Optional): Sends the message silently. Users will receive a notification with no sound.
        :param reply_to_message_id (Integer, Optional): If the message is a reply, ID of the original message
        :param allow_sending_without_reply (Boolean, Optional): Pass True, if the message should be sent even if the specified replied-to message is not found
        :param reply_markup (InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, Optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("sendPhoto", kwargs)

    def sendAudio(
        self,
        chat_id,
        audio,
        caption = None,
        parse_mode = None,
        caption_entities = None,
        duration = None,
        performer = None,
        title = None,
        thumb = None,
        disable_notification = None,
        reply_to_message_id = None,
        allow_sending_without_reply = None,
        reply_markup = None,
        ):
        """
        Use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .MP3 or .M4A format. On success, the sent Message is returned. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future.
        For sending voice messages, use the sendVoice method instead.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param audio (InputFile or String): Audio file to send. Pass a file_id as String to send an audio file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an audio file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files \xc2\xbb
        :param caption (String, Optional): Audio caption, 0-1024 characters after entities parsing
        :param parse_mode (String, Optional): Mode for parsing entities in the audio caption. See formatting options for more details.
        :param caption_entities (Array of MessageEntity, Optional): List of special entities that appear in the caption, which can be specified instead of parse_mode
        :param duration (Integer, Optional): Duration of the audio in seconds
        :param performer (String, Optional): Performer
        :param title (String, Optional): Track name
        :param thumb (InputFile or String, Optional): Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass \xe2\x80\x9cattach://<file_attach_name>\xe2\x80\x9d if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files \xc2\xbb
        :param disable_notification (Boolean, Optional): Sends the message silently. Users will receive a notification with no sound.
        :param reply_to_message_id (Integer, Optional): If the message is a reply, ID of the original message
        :param allow_sending_without_reply (Boolean, Optional): Pass True, if the message should be sent even if the specified replied-to message is not found
        :param reply_markup (InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, Optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("sendAudio", kwargs)

    def sendDocument(
        self,
        chat_id,
        document,
        thumb = None,
        caption = None,
        parse_mode = None,
        caption_entities = None,
        disable_content_type_detection = None,
        disable_notification = None,
        reply_to_message_id = None,
        allow_sending_without_reply = None,
        reply_markup = None,
        ):
        """
        Use this method to send general files. On success, the sent Message is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param document (InputFile or String): File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files \xc2\xbb
        :param thumb (InputFile or String, Optional): Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass \xe2\x80\x9cattach://<file_attach_name>\xe2\x80\x9d if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files \xc2\xbb
        :param caption (String, Optional): Document caption (may also be used when resending documents by file_id), 0-1024 characters after entities parsing
        :param parse_mode (String, Optional): Mode for parsing entities in the document caption. See formatting options for more details.
        :param caption_entities (Array of MessageEntity, Optional): List of special entities that appear in the caption, which can be specified instead of parse_mode
        :param disable_content_type_detection (Boolean, Optional): Disables automatic server-side content type detection for files uploaded using multipart/form-data
        :param disable_notification (Boolean, Optional): Sends the message silently. Users will receive a notification with no sound.
        :param reply_to_message_id (Integer, Optional): If the message is a reply, ID of the original message
        :param allow_sending_without_reply (Boolean, Optional): Pass True, if the message should be sent even if the specified replied-to message is not found
        :param reply_markup (InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, Optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("sendDocument", kwargs)

    def sendVideo(
        self,
        chat_id,
        video,
        duration = None,
        width = None,
        height = None,
        thumb = None,
        caption = None,
        parse_mode = None,
        caption_entities = None,
        supports_streaming = None,
        disable_notification = None,
        reply_to_message_id = None,
        allow_sending_without_reply = None,
        reply_markup = None,
        ):
        """
        Use this method to send video files, Telegram clients support mp4 videos (other formats may be sent as Document). On success, the sent Message is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param video (InputFile or String): Video to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data. More info on Sending Files \xc2\xbb
        :param duration (Integer, Optional): Duration of sent video in seconds
        :param width (Integer, Optional): Video width
        :param height (Integer, Optional): Video height
        :param thumb (InputFile or String, Optional): Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass \xe2\x80\x9cattach://<file_attach_name>\xe2\x80\x9d if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files \xc2\xbb
        :param caption (String, Optional): Video caption (may also be used when resending videos by file_id), 0-1024 characters after entities parsing
        :param parse_mode (String, Optional): Mode for parsing entities in the video caption. See formatting options for more details.
        :param caption_entities (Array of MessageEntity, Optional): List of special entities that appear in the caption, which can be specified instead of parse_mode
        :param supports_streaming (Boolean, Optional): Pass True, if the uploaded video is suitable for streaming
        :param disable_notification (Boolean, Optional): Sends the message silently. Users will receive a notification with no sound.
        :param reply_to_message_id (Integer, Optional): If the message is a reply, ID of the original message
        :param allow_sending_without_reply (Boolean, Optional): Pass True, if the message should be sent even if the specified replied-to message is not found
        :param reply_markup (InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, Optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("sendVideo", kwargs)

    def sendAnimation(
        self,
        chat_id,
        animation,
        duration = None,
        width = None,
        height = None,
        thumb = None,
        caption = None,
        parse_mode = None,
        caption_entities = None,
        disable_notification = None,
        reply_to_message_id = None,
        allow_sending_without_reply = None,
        reply_markup = None,
        ):
        """
        Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound). On success, the sent Message is returned. Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param animation (InputFile or String): Animation to send. Pass a file_id as String to send an animation that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an animation from the Internet, or upload a new animation using multipart/form-data. More info on Sending Files \xc2\xbb
        :param duration (Integer, Optional): Duration of sent animation in seconds
        :param width (Integer, Optional): Animation width
        :param height (Integer, Optional): Animation height
        :param thumb (InputFile or String, Optional): Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass \xe2\x80\x9cattach://<file_attach_name>\xe2\x80\x9d if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files \xc2\xbb
        :param caption (String, Optional): Animation caption (may also be used when resending animation by file_id), 0-1024 characters after entities parsing
        :param parse_mode (String, Optional): Mode for parsing entities in the animation caption. See formatting options for more details.
        :param caption_entities (Array of MessageEntity, Optional): List of special entities that appear in the caption, which can be specified instead of parse_mode
        :param disable_notification (Boolean, Optional): Sends the message silently. Users will receive a notification with no sound.
        :param reply_to_message_id (Integer, Optional): If the message is a reply, ID of the original message
        :param allow_sending_without_reply (Boolean, Optional): Pass True, if the message should be sent even if the specified replied-to message is not found
        :param reply_markup (InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, Optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("sendAnimation", kwargs)

    def sendVoice(
        self,
        chat_id,
        voice,
        caption = None,
        parse_mode = None,
        caption_entities = None,
        duration = None,
        disable_notification = None,
        reply_to_message_id = None,
        allow_sending_without_reply = None,
        reply_markup = None,
        ):
        """
        Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS (other formats may be sent as Audio or Document). On success, the sent Message is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param voice (InputFile or String): Audio file to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files \xc2\xbb
        :param caption (String, Optional): Voice message caption, 0-1024 characters after entities parsing
        :param parse_mode (String, Optional): Mode for parsing entities in the voice message caption. See formatting options for more details.
        :param caption_entities (Array of MessageEntity, Optional): List of special entities that appear in the caption, which can be specified instead of parse_mode
        :param duration (Integer, Optional): Duration of the voice message in seconds
        :param disable_notification (Boolean, Optional): Sends the message silently. Users will receive a notification with no sound.
        :param reply_to_message_id (Integer, Optional): If the message is a reply, ID of the original message
        :param allow_sending_without_reply (Boolean, Optional): Pass True, if the message should be sent even if the specified replied-to message is not found
        :param reply_markup (InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, Optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("sendVoice", kwargs)

    def sendVideoNote(
        self,
        chat_id,
        video_note,
        duration = None,
        length = None,
        thumb = None,
        disable_notification = None,
        reply_to_message_id = None,
        allow_sending_without_reply = None,
        reply_markup = None,
        ):
        """
        As of v.4.0, Telegram clients support rounded square mp4 videos of up to 1 minute long. Use this method to send video messages. On success, the sent Message is returned.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param video_note (InputFile or String): Video note to send. Pass a file_id as String to send a video note that exists on the Telegram servers (recommended) or upload a new video using multipart/form-data. More info on Sending Files \xc2\xbb. Sending video notes by a URL is currently unsupported
        :param duration (Integer, Optional): Duration of sent video in seconds
        :param length (Integer, Optional): Video width and height, i.e. diameter of the video message
        :param thumb (InputFile or String, Optional): Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass \xe2\x80\x9cattach://<file_attach_name>\xe2\x80\x9d if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files \xc2\xbb
        :param disable_notification (Boolean, Optional): Sends the message silently. Users will receive a notification with no sound.
        :param reply_to_message_id (Integer, Optional): If the message is a reply, ID of the original message
        :param allow_sending_without_reply (Boolean, Optional): Pass True, if the message should be sent even if the specified replied-to message is not found
        :param reply_markup (InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, Optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("sendVideoNote", kwargs)

    def sendMediaGroup(
        self,
        chat_id,
        media,
        disable_notification = None,
        reply_to_message_id = None,
        allow_sending_without_reply = None,
        ):
        """
        Use this method to send a group of photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an array of Messages that were sent is returned.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param media (Array of InputMediaAudio, InputMediaDocument, InputMediaPhoto and InputMediaVideo): A JSON-serialized array describing messages to be sent, must include 2-10 items
        :param disable_notification (Boolean, Optional): Sends messages silently. Users will receive a notification with no sound.
        :param reply_to_message_id (Integer, Optional): If the messages are a reply, ID of the original message
        :param allow_sending_without_reply (Boolean, Optional): Pass True, if the message should be sent even if the specified replied-to message is not found
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("sendMediaGroup", kwargs)

    def sendLocation(
        self,
        chat_id,
        latitude,
        longitude,
        horizontal_accuracy = None,
        live_period = None,
        heading = None,
        proximity_alert_radius = None,
        disable_notification = None,
        reply_to_message_id = None,
        allow_sending_without_reply = None,
        reply_markup = None,
        ):
        """
        Use this method to send point on the map. On success, the sent Message is returned.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param latitude (Float number): Latitude of the location
        :param longitude (Float number): Longitude of the location
        :param horizontal_accuracy (Float number, Optional): The radius of uncertainty for the location, measured in meters; 0-1500
        :param live_period (Integer, Optional): Period in seconds for which the location will be updated (see Live Locations, should be between 60 and 86400.
        :param heading (Integer, Optional): For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
        :param proximity_alert_radius (Integer, Optional): For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
        :param disable_notification (Boolean, Optional): Sends the message silently. Users will receive a notification with no sound.
        :param reply_to_message_id (Integer, Optional): If the message is a reply, ID of the original message
        :param allow_sending_without_reply (Boolean, Optional): Pass True, if the message should be sent even if the specified replied-to message is not found
        :param reply_markup (InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, Optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("sendLocation", kwargs)

    def editMessageLiveLocation(
        self,
        latitude,
        longitude,
        chat_id = None,
        message_id = None,
        inline_message_id = None,
        horizontal_accuracy = None,
        heading = None,
        proximity_alert_radius = None,
        reply_markup = None,
        ):
        """
        Use this method to edit live location messages. A location can be edited until its live_period expires or editing is explicitly disabled by a call to stopMessageLiveLocation. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

        Keyword arguments:
        
        :param latitude (Float number): Latitude of new location
        :param longitude (Float number): Longitude of new location
        :param chat_id (Integer or String, Optional): Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param message_id (Integer, Optional): Required if inline_message_id is not specified. Identifier of the message to edit
        :param inline_message_id (String, Optional): Required if chat_id and message_id are not specified. Identifier of the inline message
        :param horizontal_accuracy (Float number, Optional): The radius of uncertainty for the location, measured in meters; 0-1500
        :param heading (Integer, Optional): Direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
        :param proximity_alert_radius (Integer, Optional): Maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
        :param reply_markup (InlineKeyboardMarkup, Optional): A JSON-serialized object for a new inline keyboard.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("editMessageLiveLocation", kwargs)

    def stopMessageLiveLocation(
        self,
        chat_id = None,
        message_id = None,
        inline_message_id = None,
        reply_markup = None,
        ):
        """
        Use this method to stop updating a live location message before live_period expires. On success, if the message was sent by the bot, the sent Message is returned, otherwise True is returned.

        Keyword arguments:
        
        :param chat_id (Integer or String, Optional): Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param message_id (Integer, Optional): Required if inline_message_id is not specified. Identifier of the message with live location to stop
        :param inline_message_id (String, Optional): Required if chat_id and message_id are not specified. Identifier of the inline message
        :param reply_markup (InlineKeyboardMarkup, Optional): A JSON-serialized object for a new inline keyboard.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("stopMessageLiveLocation", kwargs)

    def sendVenue(
        self,
        chat_id,
        latitude,
        longitude,
        title,
        address,
        foursquare_id = None,
        foursquare_type = None,
        google_place_id = None,
        google_place_type = None,
        disable_notification = None,
        reply_to_message_id = None,
        allow_sending_without_reply = None,
        reply_markup = None,
        ):
        """
        Use this method to send information about a venue. On success, the sent Message is returned.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param latitude (Float number): Latitude of the venue
        :param longitude (Float number): Longitude of the venue
        :param title (String): Name of the venue
        :param address (String): Address of the venue
        :param foursquare_id (String, Optional): Foursquare identifier of the venue
        :param foursquare_type (String, Optional): Foursquare type of the venue, if known. (For example, \xe2\x80\x9carts_entertainment/default\xe2\x80\x9d, \xe2\x80\x9carts_entertainment/aquarium\xe2\x80\x9d or \xe2\x80\x9cfood/icecream\xe2\x80\x9d.)
        :param google_place_id (String, Optional): Google Places identifier of the venue
        :param google_place_type (String, Optional): Google Places type of the venue. (See supported types.)
        :param disable_notification (Boolean, Optional): Sends the message silently. Users will receive a notification with no sound.
        :param reply_to_message_id (Integer, Optional): If the message is a reply, ID of the original message
        :param allow_sending_without_reply (Boolean, Optional): Pass True, if the message should be sent even if the specified replied-to message is not found
        :param reply_markup (InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, Optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("sendVenue", kwargs)

    def sendContact(
        self,
        chat_id,
        phone_number,
        first_name,
        last_name = None,
        vcard = None,
        disable_notification = None,
        reply_to_message_id = None,
        allow_sending_without_reply = None,
        reply_markup = None,
        ):
        """
        Use this method to send phone contacts. On success, the sent Message is returned.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param phone_number (String): Contact's phone number
        :param first_name (String): Contact's first name
        :param last_name (String, Optional): Contact's last name
        :param vcard (String, Optional): Additional data about the contact in the form of a vCard, 0-2048 bytes
        :param disable_notification (Boolean, Optional): Sends the message silently. Users will receive a notification with no sound.
        :param reply_to_message_id (Integer, Optional): If the message is a reply, ID of the original message
        :param allow_sending_without_reply (Boolean, Optional): Pass True, if the message should be sent even if the specified replied-to message is not found
        :param reply_markup (InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, Optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove keyboard or to force a reply from the user.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("sendContact", kwargs)

    def sendPoll(
        self,
        chat_id,
        question,
        options,
        is_anonymous = None,
        type = None,
        allows_multiple_answers = None,
        correct_option_id = None,
        explanation = None,
        explanation_parse_mode = None,
        explanation_entities = None,
        open_period = None,
        close_date = None,
        is_closed = None,
        disable_notification = None,
        reply_to_message_id = None,
        allow_sending_without_reply = None,
        reply_markup = None,
        ):
        """
        Use this method to send a native poll. On success, the sent Message is returned.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param question (String): Poll question, 1-300 characters
        :param options (Array of String): A JSON-serialized list of answer options, 2-10 strings 1-100 characters each
        :param is_anonymous (Boolean, Optional): True, if the poll needs to be anonymous, defaults to True
        :param type (String, Optional): Poll type, \xe2\x80\x9cquiz\xe2\x80\x9d or \xe2\x80\x9cregular\xe2\x80\x9d, defaults to \xe2\x80\x9cregular\xe2\x80\x9d
        :param allows_multiple_answers (Boolean, Optional): True, if the poll allows multiple answers, ignored for polls in quiz mode, defaults to False
        :param correct_option_id (Integer, Optional): 0-based identifier of the correct answer option, required for polls in quiz mode
        :param explanation (String, Optional): Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters with at most 2 line feeds after entities parsing
        :param explanation_parse_mode (String, Optional): Mode for parsing entities in the explanation. See formatting options for more details.
        :param explanation_entities (Array of MessageEntity, Optional): List of special entities that appear in the poll explanation, which can be specified instead of parse_mode
        :param open_period (Integer, Optional): Amount of time in seconds the poll will be active after creation, 5-600. Can't be used together with close_date.
        :param close_date (Integer, Optional): Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 600 seconds in the future. Can't be used together with open_period.
        :param is_closed (Boolean, Optional): Pass True, if the poll needs to be immediately closed. This can be useful for poll preview.
        :param disable_notification (Boolean, Optional): Sends the message silently. Users will receive a notification with no sound.
        :param reply_to_message_id (Integer, Optional): If the message is a reply, ID of the original message
        :param allow_sending_without_reply (Boolean, Optional): Pass True, if the message should be sent even if the specified replied-to message is not found
        :param reply_markup (InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, Optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("sendPoll", kwargs)

    def sendDice(
        self,
        chat_id,
        emoji = None,
        disable_notification = None,
        reply_to_message_id = None,
        allow_sending_without_reply = None,
        reply_markup = None,
        ):
        """
        Use this method to send an animated emoji that will display a random value. On success, the sent Message is returned.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param emoji (String, Optional): Emoji on which the dice throw animation is based. Currently, must be one of \xe2\x80\x9c\xe2\x80\x9d, \xe2\x80\x9c\xe2\x80\x9d, \xe2\x80\x9c\xe2\x80\x9d, \xe2\x80\x9c\xe2\x80\x9d, \xe2\x80\x9c\xe2\x80\x9d, or \xe2\x80\x9c\xe2\x80\x9d. Dice can have values 1-6 for \xe2\x80\x9c\xe2\x80\x9d, \xe2\x80\x9c\xe2\x80\x9d and \xe2\x80\x9c\xe2\x80\x9d, values 1-5 for \xe2\x80\x9c\xe2\x80\x9d and \xe2\x80\x9c\xe2\x80\x9d, and values 1-64 for \xe2\x80\x9c\xe2\x80\x9d. Defaults to \xe2\x80\x9c\xe2\x80\x9d
        :param disable_notification (Boolean, Optional): Sends the message silently. Users will receive a notification with no sound.
        :param reply_to_message_id (Integer, Optional): If the message is a reply, ID of the original message
        :param allow_sending_without_reply (Boolean, Optional): Pass True, if the message should be sent even if the specified replied-to message is not found
        :param reply_markup (InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, Optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("sendDice", kwargs)

    def sendChatAction(
        self,
        chat_id,
        action,
        ):
        """
        Use this method when you need to tell the user that something is happening on the bot's side. The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status). Returns True on success.
        Example: The ImageBot needs some time to process a request and upload the image. Instead of sending a text message along the lines of \xe2\x80\x9cRetrieving image, please wait\xe2\x80\xa6\xe2\x80\x9d, the bot may use sendChatAction with action = upload_photo. The user will see a \xe2\x80\x9csending photo\xe2\x80\x9d status for the bot.
        We only recommend using this method when a response from the bot will take a noticeable amount of time to arrive.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param action (String): Type of action to broadcast. Choose one, depending on what the user is about to receive: typing for text messages, upload_photo for photos, record_video or upload_video for videos, record_voice or upload_voice for voice notes, upload_document for general files, find_location for location data, record_video_note or upload_video_note for video notes.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("sendChatAction", kwargs)

    def getUserProfilePhotos(
        self,
        user_id,
        offset = None,
        limit = None,
        ):
        """
        Use this method to get a list of profile pictures for a user. Returns a UserProfilePhotos object.

        Keyword arguments:
        
        :param user_id (Integer): Unique identifier of the target user
        :param offset (Integer, Optional): Sequential number of the first photo to be returned. By default, all photos are returned.
        :param limit (Integer, Optional): Limits the number of photos to be retrieved. Values between 1-100 are accepted. Defaults to 100.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("getUserProfilePhotos", kwargs)

    def getFile(
        self,
        file_id,
        ):
        """
        Use this method to get basic info about a file and prepare it for downloading. For the moment, bots can download files of up to 20MB in size. On success, a File object is returned. The file can then be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>, where <file_path> is taken from the response. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile again.

        Keyword arguments:
        
        :param file_id (String): File identifier to get info about
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("getFile", kwargs)

    def banChatMember(
        self,
        chat_id,
        user_id,
        until_date = None,
        revoke_messages = None,
        ):
        """
        Use this method to ban a user in a group, a supergroup or a channel. In the case of supergroups and channels, the user will not be able to return to the chat on their own using invite links, etc., unless unbanned first. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Returns True on success.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target group or username of the target supergroup or channel (in the format @channelusername)
        :param user_id (Integer): Unique identifier of the target user
        :param until_date (Integer, Optional): Date when the user will be unbanned, unix time. If user is banned for more than 366 days or less than 30 seconds from the current time they are considered to be banned forever. Applied for supergroups and channels only.
        :param revoke_messages (Boolean, Optional): Pass True to delete all messages from the chat for the user that is being removed. If False, the user will be able to see messages in the group that were sent before the user was removed. Always True for supergroups and channels.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("banChatMember", kwargs)

    def unbanChatMember(
        self,
        chat_id,
        user_id,
        only_if_banned = None,
        ):
        """
        Use this method to unban a previously banned user in a supergroup or channel. The user will not return to the group or channel automatically, but will be able to join via link, etc. The bot must be an administrator for this to work. By default, this method guarantees that after the call the user is not a member of the chat, but will be able to join it. So if the user is a member of the chat they will also be removed from the chat. If you don't want this, use the parameter only_if_banned. Returns True on success.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target group or username of the target supergroup or channel (in the format @username)
        :param user_id (Integer): Unique identifier of the target user
        :param only_if_banned (Boolean, Optional): Do nothing if the user is not banned
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("unbanChatMember", kwargs)

    def restrictChatMember(
        self,
        chat_id,
        user_id,
        permissions,
        until_date = None,
        ):
        """
        Use this method to restrict a user in a supergroup. The bot must be an administrator in the supergroup for this to work and must have the appropriate admin rights. Pass True for all permissions to lift restrictions from a user. Returns True on success.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
        :param user_id (Integer): Unique identifier of the target user
        :param permissions (ChatPermissions): A JSON-serialized object for new user permissions
        :param until_date (Integer, Optional): Date when restrictions will be lifted for the user, unix time. If user is restricted for more than 366 days or less than 30 seconds from the current time, they are considered to be restricted forever
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("restrictChatMember", kwargs)

    def promoteChatMember(
        self,
        chat_id,
        user_id,
        is_anonymous = None,
        can_manage_chat = None,
        can_post_messages = None,
        can_edit_messages = None,
        can_delete_messages = None,
        can_manage_voice_chats = None,
        can_restrict_members = None,
        can_promote_members = None,
        can_change_info = None,
        can_invite_users = None,
        can_pin_messages = None,
        ):
        """
        Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Pass False for all boolean parameters to demote a user. Returns True on success.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param user_id (Integer): Unique identifier of the target user
        :param is_anonymous (Boolean, Optional): Pass True, if the administrator's presence in the chat is hidden
        :param can_manage_chat (Boolean, Optional): Pass True, if the administrator can access the chat event log, chat statistics, message statistics in channels, see channel members, see anonymous administrators in supergroups and ignore slow mode. Implied by any other administrator privilege
        :param can_post_messages (Boolean, Optional): Pass True, if the administrator can create channel posts, channels only
        :param can_edit_messages (Boolean, Optional): Pass True, if the administrator can edit messages of other users and can pin messages, channels only
        :param can_delete_messages (Boolean, Optional): Pass True, if the administrator can delete messages of other users
        :param can_manage_voice_chats (Boolean, Optional): Pass True, if the administrator can manage voice chats
        :param can_restrict_members (Boolean, Optional): Pass True, if the administrator can restrict, ban or unban chat members
        :param can_promote_members (Boolean, Optional): Pass True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by him)
        :param can_change_info (Boolean, Optional): Pass True, if the administrator can change chat title, photo and other settings
        :param can_invite_users (Boolean, Optional): Pass True, if the administrator can invite new users to the chat
        :param can_pin_messages (Boolean, Optional): Pass True, if the administrator can pin messages, supergroups only
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("promoteChatMember", kwargs)

    def setChatAdministratorCustomTitle(
        self,
        chat_id,
        user_id,
        custom_title,
        ):
        """
        Use this method to set a custom title for an administrator in a supergroup promoted by the bot. Returns True on success.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
        :param user_id (Integer): Unique identifier of the target user
        :param custom_title (String): New custom title for the administrator; 0-16 characters, emoji are not allowed
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("setChatAdministratorCustomTitle", kwargs)

    def setChatPermissions(
        self,
        chat_id,
        permissions,
        ):
        """
        Use this method to set default chat permissions for all members. The bot must be an administrator in the group or a supergroup for this to work and must have the can_restrict_members admin rights. Returns True on success.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
        :param permissions (ChatPermissions): New default chat permissions
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("setChatPermissions", kwargs)

    def exportChatInviteLink(
        self,
        chat_id,
        ):
        """
        Use this method to generate a new primary invite link for a chat; any previously generated primary link is revoked. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Returns the new invite link as String on success.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("exportChatInviteLink", kwargs)

    def createChatInviteLink(
        self,
        chat_id,
        expire_date = None,
        member_limit = None,
        ):
        """
        Use this method to create an additional invite link for a chat. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. The link can be revoked using the method revokeChatInviteLink. Returns the new invite link as ChatInviteLink object.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param expire_date (Integer, Optional): Point in time (Unix timestamp) when the link will expire
        :param member_limit (Integer, Optional): Maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("createChatInviteLink", kwargs)

    def editChatInviteLink(
        self,
        chat_id,
        invite_link,
        expire_date = None,
        member_limit = None,
        ):
        """
        Use this method to edit a non-primary invite link created by the bot. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Returns the edited invite link as a ChatInviteLink object.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param invite_link (String): The invite link to edit
        :param expire_date (Integer, Optional): Point in time (Unix timestamp) when the link will expire
        :param member_limit (Integer, Optional): Maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("editChatInviteLink", kwargs)

    def revokeChatInviteLink(
        self,
        chat_id,
        invite_link,
        ):
        """
        Use this method to revoke an invite link created by the bot. If the primary link is revoked, a new link is automatically generated. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Returns the revoked invite link as ChatInviteLink object.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier of the target chat or username of the target channel (in the format @channelusername)
        :param invite_link (String): The invite link to revoke
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("revokeChatInviteLink", kwargs)

    def setChatPhoto(
        self,
        chat_id,
        photo,
        ):
        """
        Use this method to set a new profile photo for the chat. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Returns True on success.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param photo (InputFile): New chat photo, uploaded using multipart/form-data
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("setChatPhoto", kwargs)

    def deleteChatPhoto(
        self,
        chat_id,
        ):
        """
        Use this method to delete a chat photo. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Returns True on success.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("deleteChatPhoto", kwargs)

    def setChatTitle(
        self,
        chat_id,
        title,
        ):
        """
        Use this method to change the title of a chat. Titles can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Returns True on success.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param title (String): New chat title, 1-255 characters
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("setChatTitle", kwargs)

    def setChatDescription(
        self,
        chat_id,
        description = None,
        ):
        """
        Use this method to change the description of a group, a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Returns True on success.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param description (String, Optional): New chat description, 0-255 characters
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("setChatDescription", kwargs)

    def pinChatMessage(
        self,
        chat_id,
        message_id,
        disable_notification = None,
        ):
        """
        Use this method to add a message to the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' admin right in a supergroup or 'can_edit_messages' admin right in a channel. Returns True on success.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param message_id (Integer): Identifier of a message to pin
        :param disable_notification (Boolean, Optional): Pass True, if it is not necessary to send a notification to all chat members about the new pinned message. Notifications are always disabled in channels and private chats.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("pinChatMessage", kwargs)

    def unpinChatMessage(
        self,
        chat_id,
        message_id = None,
        ):
        """
        Use this method to remove a message from the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' admin right in a supergroup or 'can_edit_messages' admin right in a channel. Returns True on success.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param message_id (Integer, Optional): Identifier of a message to unpin. If not specified, the most recent pinned message (by sending date) will be unpinned.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("unpinChatMessage", kwargs)

    def unpinAllChatMessages(
        self,
        chat_id,
        ):
        """
        Use this method to clear the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' admin right in a supergroup or 'can_edit_messages' admin right in a channel. Returns True on success.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("unpinAllChatMessages", kwargs)

    def leaveChat(
        self,
        chat_id,
        ):
        """
        Use this method for your bot to leave a group, supergroup or channel. Returns True on success.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("leaveChat", kwargs)

    def getChat(
        self,
        chat_id,
        ):
        """
        Use this method to get up to date information about the chat (current name of the user for one-on-one conversations, current username of a user, group or channel, etc.). Returns a Chat object on success.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("getChat", kwargs)

    def getChatAdministrators(
        self,
        chat_id,
        ):
        """
        Use this method to get a list of administrators in a chat. On success, returns an Array of ChatMember objects that contains information about all chat administrators except other bots. If the chat is a group or a supergroup and no administrators were appointed, only the creator will be returned.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("getChatAdministrators", kwargs)

    def getChatMemberCount(
        self,
        chat_id,
        ):
        """
        Use this method to get the number of members in a chat. Returns Int on success.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("getChatMemberCount", kwargs)

    def getChatMember(
        self,
        chat_id,
        user_id,
        ):
        """
        Use this method to get information about a member of a chat. Returns a ChatMember object on success.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        :param user_id (Integer): Unique identifier of the target user
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("getChatMember", kwargs)

    def setChatStickerSet(
        self,
        chat_id,
        sticker_set_name,
        ):
        """
        Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
        :param sticker_set_name (String): Name of the sticker set to be set as the group sticker set
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("setChatStickerSet", kwargs)

    def deleteChatStickerSet(
        self,
        chat_id,
        ):
        """
        Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate admin rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("deleteChatStickerSet", kwargs)

    def answerCallbackQuery(
        self,
        callback_query_id,
        text = None,
        show_alert = None,
        url = None,
        cache_time = None,
        ):
        """
        Use this method to send answers to callback queries sent from inline keyboards. The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. On success, True is returned.
        Alternatively, the user can be redirected to the specified Game URL. For this option to work, you must first create a game for your bot via @Botfather and accept the terms. Otherwise, you may use links like t.me/your_bot?start=XXXX that open your bot with a parameter.

        Keyword arguments:
        
        :param callback_query_id (String): Unique identifier for the query to be answered
        :param text (String, Optional): Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters
        :param show_alert (Boolean, Optional): If true, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to false.
        :param url (String, Optional): URL that will be opened by the user's client. If you have created a Game and accepted the conditions via @Botfather, specify the URL that opens your game \xe2\x80\x94 note that this will only work if the query comes from a callback_game button.Otherwise, you may use links like t.me/your_bot?start=XXXX that open your bot with a parameter.
        :param cache_time (Integer, Optional): The maximum amount of time in seconds that the result of the callback query may be cached client-side. Telegram apps will support caching starting in version 3.14. Defaults to 0.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("answerCallbackQuery", kwargs)

    def setMyCommands(
        self,
        commands,
        scope = None,
        language_code = None,
        ):
        """
        Use this method to change the list of the bot's commands. See https://core.telegram.org/bots#commands for more details about bot commands. Returns True on success.

        Keyword arguments:
        
        :param commands (Array of BotCommand): A JSON-serialized list of bot commands to be set as the list of the bot's commands. At most 100 commands can be specified.
        :param scope (BotCommandScope, Optional): A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to BotCommandScopeDefault.
        :param language_code (String, Optional): A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("setMyCommands", kwargs)

    def deleteMyCommands(
        self,
        scope = None,
        language_code = None,
        ):
        """
        Use this method to delete the list of the bot's commands for the given scope and user language. After deletion, higher level commands will be shown to affected users. Returns True on success.

        Keyword arguments:
        
        :param scope (BotCommandScope, Optional): A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to BotCommandScopeDefault.
        :param language_code (String, Optional): A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("deleteMyCommands", kwargs)

    def getMyCommands(
        self,
        scope = None,
        language_code = None,
        ):
        """
        Use this method to get the current list of the bot's commands for the given scope and user language. Returns Array of BotCommand on success. If commands aren't set, an empty list is returned.

        Keyword arguments:
        
        :param scope (BotCommandScope, Optional): A JSON-serialized object, describing scope of users. Defaults to BotCommandScopeDefault.
        :param language_code (String, Optional): A two-letter ISO 639-1 language code or an empty string
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("getMyCommands", kwargs)

    def editMessageText(
        self,
        text,
        chat_id = None,
        message_id = None,
        inline_message_id = None,
        parse_mode = None,
        entities = None,
        disable_web_page_preview = None,
        reply_markup = None,
        ):
        """
        Use this method to edit text and game messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

        Keyword arguments:
        
        :param text (String): New text of the message, 1-4096 characters after entities parsing
        :param chat_id (Integer or String, Optional): Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param message_id (Integer, Optional): Required if inline_message_id is not specified. Identifier of the message to edit
        :param inline_message_id (String, Optional): Required if chat_id and message_id are not specified. Identifier of the inline message
        :param parse_mode (String, Optional): Mode for parsing entities in the message text. See formatting options for more details.
        :param entities (Array of MessageEntity, Optional): List of special entities that appear in message text, which can be specified instead of parse_mode
        :param disable_web_page_preview (Boolean, Optional): Disables link previews for links in this message
        :param reply_markup (InlineKeyboardMarkup, Optional): A JSON-serialized object for an inline keyboard.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("editMessageText", kwargs)

    def editMessageCaption(
        self,
        chat_id = None,
        message_id = None,
        inline_message_id = None,
        caption = None,
        parse_mode = None,
        caption_entities = None,
        reply_markup = None,
        ):
        """
        Use this method to edit captions of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

        Keyword arguments:
        
        :param chat_id (Integer or String, Optional): Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param message_id (Integer, Optional): Required if inline_message_id is not specified. Identifier of the message to edit
        :param inline_message_id (String, Optional): Required if chat_id and message_id are not specified. Identifier of the inline message
        :param caption (String, Optional): New caption of the message, 0-1024 characters after entities parsing
        :param parse_mode (String, Optional): Mode for parsing entities in the message caption. See formatting options for more details.
        :param caption_entities (Array of MessageEntity, Optional): List of special entities that appear in the caption, which can be specified instead of parse_mode
        :param reply_markup (InlineKeyboardMarkup, Optional): A JSON-serialized object for an inline keyboard.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("editMessageCaption", kwargs)

    def editMessageMedia(
        self,
        media,
        chat_id = None,
        message_id = None,
        inline_message_id = None,
        reply_markup = None,
        ):
        """
        Use this method to edit animation, audio, document, photo, or video messages. If a message is part of a message album, then it can be edited only to an audio for audio albums, only to a document for document albums and to a photo or a video otherwise. When an inline message is edited, a new file can't be uploaded. Use a previously uploaded file via its file_id or specify a URL. On success, if the edited message was sent by the bot, the edited Message is returned, otherwise True is returned.

        Keyword arguments:
        
        :param media (InputMedia): A JSON-serialized object for a new media content of the message
        :param chat_id (Integer or String, Optional): Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param message_id (Integer, Optional): Required if inline_message_id is not specified. Identifier of the message to edit
        :param inline_message_id (String, Optional): Required if chat_id and message_id are not specified. Identifier of the inline message
        :param reply_markup (InlineKeyboardMarkup, Optional): A JSON-serialized object for a new inline keyboard.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("editMessageMedia", kwargs)

    def editMessageReplyMarkup(
        self,
        chat_id = None,
        message_id = None,
        inline_message_id = None,
        reply_markup = None,
        ):
        """
        Use this method to edit only the reply markup of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

        Keyword arguments:
        
        :param chat_id (Integer or String, Optional): Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param message_id (Integer, Optional): Required if inline_message_id is not specified. Identifier of the message to edit
        :param inline_message_id (String, Optional): Required if chat_id and message_id are not specified. Identifier of the inline message
        :param reply_markup (InlineKeyboardMarkup, Optional): A JSON-serialized object for an inline keyboard.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("editMessageReplyMarkup", kwargs)

    def stopPoll(
        self,
        chat_id,
        message_id,
        reply_markup = None,
        ):
        """
        Use this method to stop a poll which was sent by the bot. On success, the stopped Poll with the final results is returned.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param message_id (Integer): Identifier of the original message with the poll
        :param reply_markup (InlineKeyboardMarkup, Optional): A JSON-serialized object for a new message inline keyboard.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("stopPoll", kwargs)

    def deleteMessage(
        self,
        chat_id,
        message_id,
        ):
        """
        Use this method to delete a message, including service messages, with the following limitations:- A message can only be deleted if it was sent less than 48 hours ago.- A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.- Bots can delete outgoing messages in private chats, groups, and supergroups.- Bots can delete incoming messages in private chats.- Bots granted can_post_messages permissions can delete outgoing messages in channels.- If the bot is an administrator of a group, it can delete any message there.- If the bot has can_delete_messages permission in a supergroup or a channel, it can delete any message there.Returns True on success.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param message_id (Integer): Identifier of the message to delete
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("deleteMessage", kwargs)


async def main():
    bot = TelegramBot(r'1743689155:AAHeSu4jYeIgYMN5yOBVcb6RcHEXNV7-iJY')
    msg = await bot.sendMessage(455572260, 'This message will be deleted :)')
    await asyncio.sleep(2)
    await bot.deleteMessage(msg.chat_id, msg.message_id)
    

if __name__ == '__main__':
    asyncio.run(main())