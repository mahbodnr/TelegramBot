from typing import Union, List

import httpx
import requests
from fastapi import FastAPI,Request
import uvicorn
from dacite import from_dict

from .database import Database
from .types import *

class TelegramBot:
    def __init__(
        self, 
        token: str,
        webhook: str = None,
        support_id: Union[str, int] = None,
        database: Database= None
        ):
        self.token = token
        self.support_id = support_id
        self.database = database

        if webhook:
            r = requests.get(
                f'https://api.telegram.org/bot{self.token}'
                f'/setWebhook?url={webhook}')
            assert r.status_code == 200, f"Couldn't set the webhook. {r.content}"

        self.app = FastAPI()
        

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


    def getUpdates(
        self,
        offset: int = None,
        limit: int = None,
        timeout: int = None,
        allowed_updates: List[str] = None,
        ):
        """
        Use this method to receive incoming updates using long polling (wiki). An Array of Update objects is returned.

        Keyword arguments:
        
        :param offset (Integer, Optional): Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates. By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as getUpdates is called with an offset higher than its update_id. The negative offset can be specified to retrieve updates starting from -offset update from the end of the updates queue. All previous updates will forgotten.
        :param limit (Integer, Optional): Limits the number of updates to be retrieved. Values between 1-100 are accepted. Defaults to 100.
        :param timeout (Integer, Optional): Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling. Should be positive, short polling should be used for testing purposes only.
        :param allowed_updates (Array of String, Optional): A JSON-serialized list of the update types you want your bot to receive. For example, specify [\xe2\x80\x9cmessage\xe2\x80\x9d, \xe2\x80\x9cedited_channel_post\xe2\x80\x9d, \xe2\x80\x9ccallback_query\xe2\x80\x9d] to only receive updates of these types. See Update for a complete list of available update types. Specify an empty list to receive all update types except chat_member (default). If not specified, the previous setting will be used.Please note that this parameter doesn't affect updates created before the call to the getUpdates, so unwanted updates may be received for a short period of time.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("getUpdates", kwargs)

    def setWebhook(
        self,
        url: str,
        certificate: InputFile = None,
        ip_address: str = None,
        max_connections: int = None,
        allowed_updates: List[str] = None,
        drop_pending_updates: bool = None,
        ):
        """
        Use this method to specify a url and receive incoming updates via an outgoing webhook. Whenever there is an update for the bot, we will send an HTTPS POST request to the specified url, containing a JSON-serialized Update. In case of an unsuccessful request, we will give up after a reasonable amount of attempts. Returns True on success.
        If you'd like to make sure that the Webhook request comes from Telegram, we recommend using a secret path in the URL, e.g. https://www.example.com/<token>. Since nobody else knows your bot's token, you can be pretty sure it's us.

        Keyword arguments:
        
        :param url (String): HTTPS url to send updates to. Use an empty string to remove webhook integration
        :param certificate (InputFile, Optional): Upload your public key certificate so that the root certificate in use can be checked. See our self-signed guide for details.
        :param ip_address (String, Optional): The fixed IP address which will be used to send webhook requests instead of the IP address resolved through DNS
        :param max_connections (Integer, Optional): Maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery, 1-100. Defaults to 40. Use lower values to limit the load on your bot's server, and higher values to increase your bot's throughput.
        :param allowed_updates (Array of String, Optional): A JSON-serialized list of the update types you want your bot to receive. For example, specify [\xe2\x80\x9cmessage\xe2\x80\x9d, \xe2\x80\x9cedited_channel_post\xe2\x80\x9d, \xe2\x80\x9ccallback_query\xe2\x80\x9d] to only receive updates of these types. See Update for a complete list of available update types. Specify an empty list to receive all update types except chat_member (default). If not specified, the previous setting will be used.Please note that this parameter doesn't affect updates created before the call to the setWebhook, so unwanted updates may be received for a short period of time.
        :param drop_pending_updates (Boolean, Optional): Pass True to drop all pending updates
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("setWebhook", kwargs)

    def deleteWebhook(
        self,
        drop_pending_updates: bool = None,
        ):
        """
        Use this method to remove webhook integration if you decide to switch back to getUpdates. Returns True on success.

        Keyword arguments:
        
        :param drop_pending_updates (Boolean, Optional): Pass True to drop all pending updates
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("deleteWebhook", kwargs)

    def getWebhookInfo(self):
        """
        Use this method to get current webhook status. Requires no parameters. On success, returns a WebhookInfo object. If the bot is using getUpdates, will return an object with the url field empty.
        """
        return self("getWebhookInfo", None)


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
        chat_id: Union[int, str],
        text: str,
        parse_mode: str = None,
        entities: List[MessageEntity] = None,
        disable_web_page_preview: bool = None,
        disable_notification: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None,
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
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_id: int,
        disable_notification: bool = None,
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
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_id: int,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        disable_notification: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None,
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
        chat_id: Union[int, str],
        photo: Union[InputFile, str],
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        disable_notification: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None,
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
        chat_id: Union[int, str],
        audio: Union[InputFile, str],
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        duration: int = None,
        performer: str = None,
        title: str = None,
        thumb: Union[InputFile, str] = None,
        disable_notification: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None,
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
        chat_id: Union[int, str],
        document: Union[InputFile, str],
        thumb: Union[InputFile, str] = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        disable_content_type_detection: bool = None,
        disable_notification: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None,
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
        chat_id: Union[int, str],
        video: Union[InputFile, str],
        duration: int = None,
        width: int = None,
        height: int = None,
        thumb: Union[InputFile, str] = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        supports_streaming: bool = None,
        disable_notification: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None,
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
        chat_id: Union[int, str],
        animation: Union[InputFile, str],
        duration: int = None,
        width: int = None,
        height: int = None,
        thumb: Union[InputFile, str] = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        disable_notification: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None,
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
        chat_id: Union[int, str],
        voice: Union[InputFile, str],
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        duration: int = None,
        disable_notification: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None,
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
        chat_id: Union[int, str],
        video_note: Union[InputFile, str],
        duration: int = None,
        length: int = None,
        thumb: Union[InputFile, str] = None,
        disable_notification: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None,
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
        chat_id: Union[int, str],
        media: List[Union[InputMediaAudio, InputMediaDocument, InputMediaPhoto, InputMediaVideo]],
        disable_notification: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
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
        chat_id: Union[int, str],
        latitude: float,
        longitude: float,
        horizontal_accuracy: float = None,
        live_period: int = None,
        heading: int = None,
        proximity_alert_radius: int = None,
        disable_notification: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None,
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
        latitude: float,
        longitude: float,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        horizontal_accuracy: float = None,
        heading: int = None,
        proximity_alert_radius: int = None,
        reply_markup: InlineKeyboardMarkup = None,
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
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        reply_markup: InlineKeyboardMarkup = None,
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
        chat_id: Union[int, str],
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        foursquare_id: str = None,
        foursquare_type: str = None,
        google_place_id: str = None,
        google_place_type: str = None,
        disable_notification: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None,
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
        chat_id: Union[int, str],
        phone_number: str,
        first_name: str,
        last_name: str = None,
        vcard: str = None,
        disable_notification: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None,
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
        chat_id: Union[int, str],
        question: str,
        options: List[str],
        is_anonymous: bool = None,
        type: str = None,
        allows_multiple_answers: bool = None,
        correct_option_id: int = None,
        explanation: str = None,
        explanation_parse_mode: str = None,
        explanation_entities: List[MessageEntity] = None,
        open_period: int = None,
        close_date: int = None,
        is_closed: bool = None,
        disable_notification: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None,
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
        chat_id: Union[int, str],
        emoji: str = None,
        disable_notification: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None,
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
        chat_id: Union[int, str],
        action: str,
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
        user_id: int,
        offset: int = None,
        limit: int = None,
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
        file_id: str,
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
        chat_id: Union[int, str],
        user_id: int,
        until_date: int = None,
        revoke_messages: bool = None,
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
        chat_id: Union[int, str],
        user_id: int,
        only_if_banned: bool = None,
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
        chat_id: Union[int, str],
        user_id: int,
        permissions: ChatPermissions,
        until_date: int = None,
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
        chat_id: Union[int, str],
        user_id: int,
        is_anonymous: bool = None,
        can_manage_chat: bool = None,
        can_post_messages: bool = None,
        can_edit_messages: bool = None,
        can_delete_messages: bool = None,
        can_manage_voice_chats: bool = None,
        can_restrict_members: bool = None,
        can_promote_members: bool = None,
        can_change_info: bool = None,
        can_invite_users: bool = None,
        can_pin_messages: bool = None,
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
        chat_id: Union[int, str],
        user_id: int,
        custom_title: str,
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
        chat_id: Union[int, str],
        permissions: ChatPermissions,
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
        chat_id: Union[int, str],
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
        chat_id: Union[int, str],
        expire_date: int = None,
        member_limit: int = None,
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
        chat_id: Union[int, str],
        invite_link: str,
        expire_date: int = None,
        member_limit: int = None,
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
        chat_id: Union[int, str],
        invite_link: str,
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
        chat_id: Union[int, str],
        photo: InputFile,
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
        chat_id: Union[int, str],
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
        chat_id: Union[int, str],
        title: str,
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
        chat_id: Union[int, str],
        description: str = None,
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
        chat_id: Union[int, str],
        message_id: int,
        disable_notification: bool = None,
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
        chat_id: Union[int, str],
        message_id: int = None,
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
        chat_id: Union[int, str],
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
        chat_id: Union[int, str],
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
        chat_id: Union[int, str],
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
        chat_id: Union[int, str],
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
        chat_id: Union[int, str],
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
        chat_id: Union[int, str],
        user_id: int,
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
        chat_id: Union[int, str],
        sticker_set_name: str,
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
        chat_id: Union[int, str],
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
        callback_query_id: str,
        text: str = None,
        show_alert: bool = None,
        url: str = None,
        cache_time: int = None,
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
        commands: List[BotCommand],
        scope: BotCommandScope = None,
        language_code: str = None,
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
        scope: BotCommandScope = None,
        language_code: str = None,
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
        scope: BotCommandScope = None,
        language_code: str = None,
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
        text: str,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        parse_mode: str = None,
        entities: List[MessageEntity] = None,
        disable_web_page_preview: bool = None,
        reply_markup: InlineKeyboardMarkup = None,
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
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: List[MessageEntity] = None,
        reply_markup: InlineKeyboardMarkup = None,
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
        media: InputMedia,
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        reply_markup: InlineKeyboardMarkup = None,
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
        chat_id: Union[int, str] = None,
        message_id: int = None,
        inline_message_id: str = None,
        reply_markup: InlineKeyboardMarkup = None,
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
        chat_id: Union[int, str],
        message_id: int,
        reply_markup: InlineKeyboardMarkup = None,
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
        chat_id: Union[int, str],
        message_id: int,
        ):
        """
        Use this method to delete a message, including service messages, with the following limitations:- A message can only be deleted if it was sent less than 48 hours ago.- A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.- Bots can delete outgoing messages in private chats, groups, and supergroups.- Bots can delete incoming messages in private chats.- Bots granted can_post_messages permissions can delete outgoing messages in channels.- If the bot is an administrator of a group, it can delete any message there.- If the bot has can_delete_messages permission in a supergroup or a channel, it can delete any message there.Returns True on success.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param message_id (Integer): Identifier of the message to delete
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("deleteMessage", kwargs)

    def sendSticker(
        self,
        chat_id: Union[int, str],
        sticker: Union[InputFile, str],
        disable_notification: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply] = None,
        ):
        """
        Use this method to send static .WEBP or animated .TGS stickers. On success, the sent Message is returned.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param sticker (InputFile or String): Sticker to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a .WEBP file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files \xc2\xbb
        :param disable_notification (Boolean, Optional): Sends the message silently. Users will receive a notification with no sound.
        :param reply_to_message_id (Integer, Optional): If the message is a reply, ID of the original message
        :param allow_sending_without_reply (Boolean, Optional): Pass True, if the message should be sent even if the specified replied-to message is not found
        :param reply_markup (InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply, Optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("sendSticker", kwargs)

    def getStickerSet(
        self,
        name: str,
        ):
        """
        Use this method to get a sticker set. On success, a StickerSet object is returned.

        Keyword arguments:
        
        :param name (String): Name of the sticker set
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("getStickerSet", kwargs)

    def uploadStickerFile(
        self,
        user_id: int,
        png_sticker: InputFile,
        ):
        """
        Use this method to upload a .PNG file with a sticker for later use in createNewStickerSet and addStickerToSet methods (can be used multiple times). Returns the uploaded File on success.

        Keyword arguments:
        
        :param user_id (Integer): User identifier of sticker file owner
        :param png_sticker (InputFile): PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either width or height must be exactly 512px. More info on Sending Files \xc2\xbb
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("uploadStickerFile", kwargs)

    def createNewStickerSet(
        self,
        user_id: int,
        name: str,
        title: str,
        emojis: str,
        png_sticker: Union[InputFile, str] = None,
        tgs_sticker: InputFile = None,
        contains_masks: bool = None,
        mask_position: MaskPosition = None,
        ):
        """
        Use this method to create a new sticker set owned by a user. The bot will be able to edit the sticker set thus created. You must use exactly one of the fields png_sticker or tgs_sticker. Returns True on success.

        Keyword arguments:
        
        :param user_id (Integer): User identifier of created sticker set owner
        :param name (String): Short name of sticker set, to be used in t.me/addstickers/ URLs (e.g., animals). Can contain only english letters, digits and underscores. Must begin with a letter, can't contain consecutive underscores and must end in \xe2\x80\x9c_by_<bot username>\xe2\x80\x9d. <bot_username> is case insensitive. 1-64 characters.
        :param title (String): Sticker set title, 1-64 characters
        :param emojis (String): One or more emoji corresponding to the sticker
        :param png_sticker (InputFile or String, Optional): PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either width or height must be exactly 512px. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files \xc2\xbb
        :param tgs_sticker (InputFile, Optional): TGS animation with the sticker, uploaded using multipart/form-data. See https://core.telegram.org/animated_stickers#technical-requirements for technical requirements
        :param contains_masks (Boolean, Optional): Pass True, if a set of mask stickers should be created
        :param mask_position (MaskPosition, Optional): A JSON-serialized object for position where the mask should be placed on faces
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("createNewStickerSet", kwargs)

    def addStickerToSet(
        self,
        user_id: int,
        name: str,
        emojis: str,
        png_sticker: Union[InputFile, str] = None,
        tgs_sticker: InputFile = None,
        mask_position: MaskPosition = None,
        ):
        """
        Use this method to add a new sticker to a set created by the bot. You must use exactly one of the fields png_sticker or tgs_sticker. Animated stickers can be added to animated sticker sets and only to them. Animated sticker sets can have up to 50 stickers. Static sticker sets can have up to 120 stickers. Returns True on success.

        Keyword arguments:
        
        :param user_id (Integer): User identifier of sticker set owner
        :param name (String): Sticker set name
        :param emojis (String): One or more emoji corresponding to the sticker
        :param png_sticker (InputFile or String, Optional): PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either width or height must be exactly 512px. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files \xc2\xbb
        :param tgs_sticker (InputFile, Optional): TGS animation with the sticker, uploaded using multipart/form-data. See https://core.telegram.org/animated_stickers#technical-requirements for technical requirements
        :param mask_position (MaskPosition, Optional): A JSON-serialized object for position where the mask should be placed on faces
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("addStickerToSet", kwargs)

    def setStickerPositionInSet(
        self,
        sticker: str,
        position: int,
        ):
        """
        Use this method to move a sticker in a set created by the bot to a specific position. Returns True on success.

        Keyword arguments:
        
        :param sticker (String): File identifier of the sticker
        :param position (Integer): New sticker position in the set, zero-based
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("setStickerPositionInSet", kwargs)

    def deleteStickerFromSet(
        self,
        sticker: str,
        ):
        """
        Use this method to delete a sticker from a set created by the bot. Returns True on success.

        Keyword arguments:
        
        :param sticker (String): File identifier of the sticker
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("deleteStickerFromSet", kwargs)

    def setStickerSetThumb(
        self,
        name: str,
        user_id: int,
        thumb: Union[InputFile, str] = None,
        ):
        """
        Use this method to set the thumbnail of a sticker set. Animated thumbnails can be set for animated sticker sets only. Returns True on success.

        Keyword arguments:
        
        :param name (String): Sticker set name
        :param user_id (Integer): User identifier of the sticker set owner
        :param thumb (InputFile or String, Optional): A PNG image with the thumbnail, must be up to 128 kilobytes in size and have width and height exactly 100px, or a TGS animation with the thumbnail up to 32 kilobytes in size; see https://core.telegram.org/animated_stickers#technical-requirements for animated sticker technical requirements. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files \xc2\xbb. Animated sticker set thumbnail can't be uploaded via HTTP URL.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("setStickerSetThumb", kwargs)

    def answerInlineQuery(
        self,
        inline_query_id: str,
        results: List[InlineQueryResult],
        cache_time: int = None,
        is_personal: bool = None,
        next_offset: str = None,
        switch_pm_text: str = None,
        switch_pm_parameter: str = None,
        ):
        """
        Use this method to send answers to an inline query. On success, True is returned.No more than 50 results per query are allowed.

        Keyword arguments:
        
        :param inline_query_id (String): Unique identifier for the answered query
        :param results (Array of InlineQueryResult): A JSON-serialized array of results for the inline query
        :param cache_time (Integer, Optional): The maximum amount of time in seconds that the result of the inline query may be cached on the server. Defaults to 300.
        :param is_personal (Boolean, Optional): Pass True, if results may be cached on the server side only for the user that sent the query. By default, results may be returned to any user who sends the same query
        :param next_offset (String, Optional): Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don't support pagination. Offset length can't exceed 64 bytes.
        :param switch_pm_text (String, Optional): If passed, clients will display a button with specified text that switches the user to a private chat with the bot and sends the bot a start message with the parameter switch_pm_parameter
        :param switch_pm_parameter (String, Optional): Deep-linking parameter for the /start message sent to the bot when user presses the switch button. 1-64 characters, only A-Z, a-z, 0-9, _ and - are allowed.Example: An inline bot that sends YouTube videos can ask the user to connect the bot to their YouTube account to adapt search results accordingly. To do this, it displays a 'Connect your YouTube account' button above the results, or even before showing any. The user presses the button, switches to a private chat with the bot and, in doing so, passes a start parameter that instructs the bot to return an oauth link. Once done, the bot can offer a switch_inline button so that the user can easily return to the chat where they wanted to use the bot's inline capabilities.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("answerInlineQuery", kwargs)

    def sendInvoice(
        self,
        chat_id: Union[int, str],
        title: str,
        description: str,
        payload: str,
        provider_token: str,
        currency: str,
        prices: List[LabeledPrice],
        max_tip_amount: int = None,
        suggested_tip_amounts: List[int] = None,
        start_parameter: str = None,
        provider_data: str = None,
        photo_url: str = None,
        photo_size: int = None,
        photo_width: int = None,
        photo_height: int = None,
        need_name: bool = None,
        need_phone_number: bool = None,
        need_email: bool = None,
        need_shipping_address: bool = None,
        send_phone_number_to_provider: bool = None,
        send_email_to_provider: bool = None,
        is_flexible: bool = None,
        disable_notification: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: InlineKeyboardMarkup = None,
        ):
        """
        Use this method to send invoices. On success, the sent Message is returned.

        Keyword arguments:
        
        :param chat_id (Integer or String): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param title (String): Product name, 1-32 characters
        :param description (String): Product description, 1-255 characters
        :param payload (String): Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.
        :param provider_token (String): Payments provider token, obtained via Botfather
        :param currency (String): Three-letter ISO 4217 currency code, see more on currencies
        :param prices (Array of LabeledPrice): Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)
        :param max_tip_amount (Integer, Optional): The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0
        :param suggested_tip_amounts (Array of Integer, Optional): A JSON-serialized array of suggested amounts of tips in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.
        :param start_parameter (String, Optional): Unique deep-linking parameter. If left empty, forwarded copies of the sent message will have a Pay button, allowing multiple users to pay directly from the forwarded message, using the same invoice. If non-empty, forwarded copies of the sent message will have a URL button with a deep link to the bot (instead of a Pay button), with the value used as the start parameter
        :param provider_data (String, Optional): A JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider.
        :param photo_url (String, Optional): URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.
        :param photo_size (Integer, Optional): Photo size
        :param photo_width (Integer, Optional): Photo width
        :param photo_height (Integer, Optional): Photo height
        :param need_name (Boolean, Optional): Pass True, if you require the user's full name to complete the order
        :param need_phone_number (Boolean, Optional): Pass True, if you require the user's phone number to complete the order
        :param need_email (Boolean, Optional): Pass True, if you require the user's email address to complete the order
        :param need_shipping_address (Boolean, Optional): Pass True, if you require the user's shipping address to complete the order
        :param send_phone_number_to_provider (Boolean, Optional): Pass True, if user's phone number should be sent to provider
        :param send_email_to_provider (Boolean, Optional): Pass True, if user's email address should be sent to provider
        :param is_flexible (Boolean, Optional): Pass True, if the final price depends on the shipping method
        :param disable_notification (Boolean, Optional): Sends the message silently. Users will receive a notification with no sound.
        :param reply_to_message_id (Integer, Optional): If the message is a reply, ID of the original message
        :param allow_sending_without_reply (Boolean, Optional): Pass True, if the message should be sent even if the specified replied-to message is not found
        :param reply_markup (InlineKeyboardMarkup, Optional): A JSON-serialized object for an inline keyboard. If empty, one 'Pay total price' button will be shown. If not empty, the first button must be a Pay button.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("sendInvoice", kwargs)

    def answerShippingQuery(
        self,
        shipping_query_id: str,
        ok: bool,
        shipping_options: List[ShippingOption] = None,
        error_message: str = None,
        ):
        """
        If you sent an invoice requesting a shipping address and the parameter is_flexible was specified, the Bot API will send an Update with a shipping_query field to the bot. Use this method to reply to shipping queries. On success, True is returned.

        Keyword arguments:
        
        :param shipping_query_id (String): Unique identifier for the query to be answered
        :param ok (Boolean): Specify True if delivery to the specified address is possible and False if there are any problems (for example, if delivery to the specified address is not possible)
        :param shipping_options (Array of ShippingOption, Optional): Required if ok is True. A JSON-serialized array of available shipping options.
        :param error_message (String, Optional): Required if ok is False. Error message in human readable form that explains why it is impossible to complete the order (e.g. "Sorry, delivery to your desired address is unavailable'). Telegram will display this message to the user.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("answerShippingQuery", kwargs)

    def answerPreCheckoutQuery(
        self,
        pre_checkout_query_id: str,
        ok: bool,
        error_message: str = None,
        ):
        """
        Once the user has confirmed their payment and shipping details, the Bot API sends the final confirmation in the form of an Update with the field pre_checkout_query. Use this method to respond to such pre-checkout queries. On success, True is returned. Note: The Bot API must receive an answer within 10 seconds after the pre-checkout query was sent.

        Keyword arguments:
        
        :param pre_checkout_query_id (String): Unique identifier for the query to be answered
        :param ok (Boolean): Specify True if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order. Use False if there are any problems.
        :param error_message (String, Optional): Required if ok is False. Error message in human readable form that explains the reason for failure to proceed with the checkout (e.g. "Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different color or garment!"). Telegram will display this message to the user.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("answerPreCheckoutQuery", kwargs)

    def setPassportDataErrors(
        self,
        user_id: int,
        errors: List[PassportElementError],
        ):
        """
        Informs a user that some of the Telegram Passport elements they provided contains errors. The user will not be able to re-submit their Passport to you until the errors are fixed (the contents of the field for which you returned the error must change). Returns True on success.
        Use this if the data submitted by the user doesn't satisfy the standards your service requires for any reason. For example, if a birthday date seems invalid, a submitted document is blurry, a scan shows evidence of tampering, etc. Supply some details in the error message to make sure the user knows how to correct the issues.

        Keyword arguments:
        
        :param user_id (Integer): User identifier
        :param errors (Array of PassportElementError): A JSON-serialized array describing the errors
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("setPassportDataErrors", kwargs)

    def sendGame(
        self,
        chat_id: int,
        game_short_name: str,
        disable_notification: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: InlineKeyboardMarkup = None,
        ):
        """
        Use this method to send a game. On success, the sent Message is returned.

        Keyword arguments:
        
        :param chat_id (Integer): Unique identifier for the target chat
        :param game_short_name (String): Short name of the game, serves as the unique identifier for the game. Set up your games via Botfather.
        :param disable_notification (Boolean, Optional): Sends the message silently. Users will receive a notification with no sound.
        :param reply_to_message_id (Integer, Optional): If the message is a reply, ID of the original message
        :param allow_sending_without_reply (Boolean, Optional): Pass True, if the message should be sent even if the specified replied-to message is not found
        :param reply_markup (InlineKeyboardMarkup, Optional): A JSON-serialized object for an inline keyboard. If empty, one 'Play game_title' button will be shown. If not empty, the first button must launch the game.
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("sendGame", kwargs)

    def setGameScore(
        self,
        user_id: int,
        score: int,
        force: bool = None,
        disable_edit_message: bool = None,
        chat_id: int = None,
        message_id: int = None,
        inline_message_id: str = None,
        ):
        """
        Use this method to set the score of the specified user in a game. On success, if the message was sent by the bot, returns the edited Message, otherwise returns True. Returns an error, if the new score is not greater than the user's current score in the chat and force is False.

        Keyword arguments:
        
        :param user_id (Integer): User identifier
        :param score (Integer): New score, must be non-negative
        :param force (Boolean, Optional): Pass True, if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters
        :param disable_edit_message (Boolean, Optional): Pass True, if the game message should not be automatically edited to include the current scoreboard
        :param chat_id (Integer, Optional): Required if inline_message_id is not specified. Unique identifier for the target chat
        :param message_id (Integer, Optional): Required if inline_message_id is not specified. Identifier of the sent message
        :param inline_message_id (String, Optional): Required if chat_id and message_id are not specified. Identifier of the inline message
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("setGameScore", kwargs)

    def getGameHighScores(
        self,
        user_id: int,
        chat_id: int = None,
        message_id: int = None,
        inline_message_id: str = None,
        ):
        """
        Use this method to get data for high score tables. Will return the score of the specified user and several of their neighbors in a game. On success, returns an Array of GameHighScore objects.
        This method will currently return scores for the target user, plus two of their closest neighbors on each side. Will also return the top three users if the user and his neighbors are not among them. Please note that this behavior is subject to change.

        Keyword arguments:
        
        :param user_id (Integer): Target user id
        :param chat_id (Integer, Optional): Required if inline_message_id is not specified. Unique identifier for the target chat
        :param message_id (Integer, Optional): Required if inline_message_id is not specified. Identifier of the sent message
        :param inline_message_id (String, Optional): Required if chat_id and message_id are not specified. Identifier of the inline message
        """
        kwargs = {k:v for k,v in locals().items() if k!='self' and v!=None}
        return self("getGameHighScores", kwargs)


    def _make_instance(self, telegramType: object, req: dict) -> object:
        req_data= eval(str(req).replace('"from"', '"_from"').replace("'from'", "'_from'"))
        return from_dict(telegramType, req_data)


    def onUpdate(
        self,
        path: str = "/",
        filters: Union[str, List[str]] = None,
        ):
        def get_update(handle):
            @self.app.post(path)
            async def recWebHook(req: Request):
                r = await req.json()
                # read update
                update = self._make_instance(Update, r)
                # filter update
                passed_filter = False
                if type(filters) == str:
                    if getattr(update, filters):
                        passed_filter = True
                elif type(filters) == list:
                    for filter in filters:
                        if getattr(update, filter):
                            passed_filter = True
                            break
                else:
                    raise TypeError(
                        "'filters' must be either a list or a string." 
                        f" got {type(filters)}"
                        )
                if not passed_filter:
                    return
                # write on database
                if self.database:
                    self.database.add_update(update)
                    if update.message and update.message._from:
                        self.database.add_user(update.message._from)
                #handle
                return await handle(update)
        return get_update