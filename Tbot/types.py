from dataclasses import dataclass
from typing import Union, List


@dataclass
class VoiceChatStarted:
    """
    This object represents a service message about a voice chat started in the chat. Currently holds no information.

    """
    pass


@dataclass
class ChatMember:
    """
    This object contains information about one member of a chat. Currently, the following 6 types of chat members are supported:
    
    ChatMemberOwner
    ChatMemberAdministrator
    ChatMemberMember
    ChatMemberRestricted
    ChatMemberLeft
    ChatMemberBanned
    

    """
    pass


@dataclass
class BotCommandScope:
    """
    This object represents the scope to which bot commands are applied. Currently, the following 7 scopes are supported:
    
    BotCommandScopeDefault
    BotCommandScopeAllPrivateChats
    BotCommandScopeAllGroupChats
    BotCommandScopeAllChatAdministrators
    BotCommandScopeChat
    BotCommandScopeChatAdministrators
    BotCommandScopeChatMember
    

    """
    pass


@dataclass
class InputMedia:
    """
    This object represents the content of a media message to be sent. It should be one of
    
    InputMediaAnimation
    InputMediaDocument
    InputMediaAudio
    InputMediaPhoto
    InputMediaVideo
    

    """
    pass


@dataclass
class InputFile:
    """
    This object represents the contents of a file to be uploaded. Must be posted using multipart/form-data in the usual way that files are uploaded via the browser.

    """
    pass


@dataclass
class InlineQueryResult:
    """
    This object represents one result of an inline query. Telegram clients currently support results of the following 20 types:
    
    InlineQueryResultCachedAudio
    InlineQueryResultCachedDocument
    InlineQueryResultCachedGif
    InlineQueryResultCachedMpeg4Gif
    InlineQueryResultCachedPhoto
    InlineQueryResultCachedSticker
    InlineQueryResultCachedVideo
    InlineQueryResultCachedVoice
    InlineQueryResultArticle
    InlineQueryResultAudio
    InlineQueryResultContact
    InlineQueryResultGame
    InlineQueryResultDocument
    InlineQueryResultGif
    InlineQueryResultLocation
    InlineQueryResultMpeg4Gif
    InlineQueryResultPhoto
    InlineQueryResultVenue
    InlineQueryResultVideo
    InlineQueryResultVoice
    
    Note: All URLs passed in inline query results will be available to end users and therefore must be assumed to be public.

    """
    pass


@dataclass
class InputMessageContent:
    """
    This object represents the content of a message to be sent as a result of an inline query. Telegram clients currently support the following 5 types:
    
    InputTextMessageContent
    InputLocationMessageContent
    InputVenueMessageContent
    InputContactMessageContent
    InputInvoiceMessageContent
    

    """
    pass


@dataclass
class PassportElementError:
    """
    This object represents an error in the Telegram Passport element which was submitted that should be resolved by the user. It should be one of:
    
    PassportElementErrorDataField
    PassportElementErrorFrontSide
    PassportElementErrorReverseSide
    PassportElementErrorSelfie
    PassportElementErrorFile
    PassportElementErrorFiles
    PassportElementErrorTranslationFile
    PassportElementErrorTranslationFiles
    PassportElementErrorUnspecified
    

    """
    pass


@dataclass
class CallbackGame:
    """
    A placeholder, currently holds no information. Use BotFather to set up your game.

    """
    pass


@dataclass
class User:
    """
    This object represents a Telegram user or bot.

    Keyword arguments:

    :param id (Integer): Unique identifier for this user or bot. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
    :param is_bot (Boolean): True, if this user is a bot
    :param first_name (String): User's or bot's first name
    :param last_name (String): Optional. User's or bot's last name
    :param username (String): Optional. User's or bot's username
    :param language_code (String): Optional. IETF language tag of the user's language
    :param can_join_groups (Boolean): Optional. True, if the bot can be invited to groups. Returned only in getMe.
    :param can_read_all_group_messages (Boolean): Optional. True, if privacy mode is disabled for the bot. Returned only in getMe.
    :param supports_inline_queries (Boolean): Optional. True, if the bot supports inline queries. Returned only in getMe.
    """
    id: int
    is_bot: bool
    first_name: str
    last_name: str
    username: str
    language_code: str
    can_join_groups: bool
    can_read_all_group_messages: bool
    supports_inline_queries: bool

@dataclass
class MessageId:
    """
    This object represents a unique message identifier.

    Keyword arguments:

    :param message_id (Integer): Unique message identifier
    """
    message_id: int


@dataclass
class MessageEntity:
    """
    This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.

    Keyword arguments:

    :param type (String): Type of the entity. Can be \xe2\x80\x9cmention\xe2\x80\x9d (@username), \xe2\x80\x9chashtag\xe2\x80\x9d (#hashtag), \xe2\x80\x9ccashtag\xe2\x80\x9d ($USD), \xe2\x80\x9cbot_command\xe2\x80\x9d (/start@jobs_bot), \xe2\x80\x9curl\xe2\x80\x9d (https://telegram.org), \xe2\x80\x9cemail\xe2\x80\x9d (do-not-reply@telegram.org), \xe2\x80\x9cphone_number\xe2\x80\x9d (+1-212-555-0123), \xe2\x80\x9cbold\xe2\x80\x9d (bold text), \xe2\x80\x9citalic\xe2\x80\x9d (italic text), \xe2\x80\x9cunderline\xe2\x80\x9d (underlined text), \xe2\x80\x9cstrikethrough\xe2\x80\x9d (strikethrough text), \xe2\x80\x9ccode\xe2\x80\x9d (monowidth string), \xe2\x80\x9cpre\xe2\x80\x9d (monowidth block), \xe2\x80\x9ctext_link\xe2\x80\x9d (for clickable text URLs), \xe2\x80\x9ctext_mention\xe2\x80\x9d (for users without usernames)
    :param offset (Integer): Offset in UTF-16 code units to the start of the entity
    :param length (Integer): Length of the entity in UTF-16 code units
    :param url (String): Optional. For \xe2\x80\x9ctext_link\xe2\x80\x9d only, url that will be opened after user taps on the text
    :param user (User): Optional. For \xe2\x80\x9ctext_mention\xe2\x80\x9d only, the mentioned user
    :param language (String): Optional. For \xe2\x80\x9cpre\xe2\x80\x9d only, the programming language of the entity text
    """
    type: str
    offset: int
    length: int
    url: str
    user: User
    language: str


@dataclass
class PhotoSize:
    """
    This object represents one size of a photo or a file / sticker thumbnail.

    Keyword arguments:

    :param file_id (String): Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id (String): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :param width (Integer): Photo width
    :param height (Integer): Photo height
    :param file_size (Integer): Optional. File size
    """
    file_id: str
    file_unique_id: str
    width: int
    height: int
    file_size: int


@dataclass
class Animation:
    """
    This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).

    Keyword arguments:

    :param file_id (String): Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id (String): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :param width (Integer): Video width as defined by sender
    :param height (Integer): Video height as defined by sender
    :param duration (Integer): Duration of the video in seconds as defined by sender
    :param thumb (PhotoSize): Optional. Animation thumbnail as defined by sender
    :param file_name (String): Optional. Original animation filename as defined by sender
    :param mime_type (String): Optional. MIME type of the file as defined by sender
    :param file_size (Integer): Optional. File size
    """
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumb: PhotoSize
    file_name: str
    mime_type: str
    file_size: int


@dataclass
class Audio:
    """
    This object represents an audio file to be treated as music by the Telegram clients.

    Keyword arguments:

    :param file_id (String): Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id (String): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :param duration (Integer): Duration of the audio in seconds as defined by sender
    :param performer (String): Optional. Performer of the audio as defined by sender or by audio tags
    :param title (String): Optional. Title of the audio as defined by sender or by audio tags
    :param file_name (String): Optional. Original filename as defined by sender
    :param mime_type (String): Optional. MIME type of the file as defined by sender
    :param file_size (Integer): Optional. File size
    :param thumb (PhotoSize): Optional. Thumbnail of the album cover to which the music file belongs
    """
    file_id: str
    file_unique_id: str
    duration: int
    performer: str
    title: str
    file_name: str
    mime_type: str
    file_size: int
    thumb: PhotoSize


@dataclass
class Document:
    """
    This object represents a general file (as opposed to photos, voice messages and audio files).

    Keyword arguments:

    :param file_id (String): Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id (String): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :param thumb (PhotoSize): Optional. Document thumbnail as defined by sender
    :param file_name (String): Optional. Original filename as defined by sender
    :param mime_type (String): Optional. MIME type of the file as defined by sender
    :param file_size (Integer): Optional. File size
    """
    file_id: str
    file_unique_id: str
    thumb: PhotoSize
    file_name: str
    mime_type: str
    file_size: int


@dataclass
class Video:
    """
    This object represents a video file.

    Keyword arguments:

    :param file_id (String): Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id (String): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :param width (Integer): Video width as defined by sender
    :param height (Integer): Video height as defined by sender
    :param duration (Integer): Duration of the video in seconds as defined by sender
    :param thumb (PhotoSize): Optional. Video thumbnail
    :param file_name (String): Optional. Original filename as defined by sender
    :param mime_type (String): Optional. Mime type of a file as defined by sender
    :param file_size (Integer): Optional. File size
    """
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumb: PhotoSize
    file_name: str
    mime_type: str
    file_size: int


@dataclass
class VideoNote:
    """
    This object represents a video message (available in Telegram apps as of v.4.0).

    Keyword arguments:

    :param file_id (String): Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id (String): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :param length (Integer): Video width and height (diameter of the video message) as defined by sender
    :param duration (Integer): Duration of the video in seconds as defined by sender
    :param thumb (PhotoSize): Optional. Video thumbnail
    :param file_size (Integer): Optional. File size
    """
    file_id: str
    file_unique_id: str
    length: int
    duration: int
    thumb: PhotoSize
    file_size: int


@dataclass
class Voice:
    """
    This object represents a voice note.

    Keyword arguments:

    :param file_id (String): Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id (String): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :param duration (Integer): Duration of the audio in seconds as defined by sender
    :param mime_type (String): Optional. MIME type of the file as defined by sender
    :param file_size (Integer): Optional. File size
    """
    file_id: str
    file_unique_id: str
    duration: int
    mime_type: str
    file_size: int


@dataclass
class Contact:
    """
    This object represents a phone contact.

    Keyword arguments:

    :param phone_number (String): Contact's phone number
    :param first_name (String): Contact's first name
    :param last_name (String): Optional. Contact's last name
    :param user_id (Integer): Optional. Contact's user identifier in Telegram. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
    :param vcard (String): Optional. Additional data about the contact in the form of a vCard
    """
    phone_number: str
    first_name: str
    last_name: str
    user_id: int
    vcard: str


@dataclass
class Dice:
    """
    This object represents an animated emoji that displays a random value.

    Keyword arguments:

    :param emoji (String): Emoji on which the dice throw animation is based
    :param value (Integer): Value of the dice, 1-6 for \xe2\x80\x9c\xe2\x80\x9d, \xe2\x80\x9c\xe2\x80\x9d and \xe2\x80\x9c\xe2\x80\x9d base emoji, 1-5 for \xe2\x80\x9c\xe2\x80\x9d and \xe2\x80\x9c\xe2\x80\x9d base emoji, 1-64 for \xe2\x80\x9c\xe2\x80\x9d base emoji
    """
    emoji: str
    value: int


@dataclass
class PollOption:
    """
    This object contains information about one answer option in a poll.

    Keyword arguments:

    :param text (String): Option text, 1-100 characters
    :param voter_count (Integer): Number of users that voted for this option
    """
    text: str
    voter_count: int


@dataclass
class PollAnswer:
    """
    This object represents an answer of a user in a non-anonymous poll.

    Keyword arguments:

    :param poll_id (String): Unique poll identifier
    :param user (User): The user, who changed the answer to the poll
    :param option_ids (Array of Integer): 0-based identifiers of answer options, chosen by the user. May be empty if the user retracted their vote.
    """
    poll_id: str
    user: User
    option_ids: List[int]


@dataclass
class Poll:
    """
    This object contains information about a poll.

    Keyword arguments:

    :param id (String): Unique poll identifier
    :param question (String): Poll question, 1-300 characters
    :param options (Array of PollOption): List of poll options
    :param total_voter_count (Integer): Total number of users that voted in the poll
    :param is_closed (Boolean): True, if the poll is closed
    :param is_anonymous (Boolean): True, if the poll is anonymous
    :param type (String): Poll type, currently can be \xe2\x80\x9cregular\xe2\x80\x9d or \xe2\x80\x9cquiz\xe2\x80\x9d
    :param allows_multiple_answers (Boolean): True, if the poll allows multiple answers
    :param correct_option_id (Integer): Optional. 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot.
    :param explanation (String): Optional. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters
    :param explanation_entities (Array of MessageEntity): Optional. Special entities like usernames, URLs, bot commands, etc. that appear in the explanation
    :param open_period (Integer): Optional. Amount of time in seconds the poll will be active after creation
    :param close_date (Integer): Optional. Point in time (Unix timestamp) when the poll will be automatically closed
    """
    id: str
    question: str
    options: List[PollOption]
    total_voter_count: int
    is_closed: bool
    is_anonymous: bool
    type: str
    allows_multiple_answers: bool
    correct_option_id: int
    explanation: str
    explanation_entities: List[MessageEntity]
    open_period: int
    close_date: int


@dataclass
class Location:
    """
    This object represents a point on the map.

    Keyword arguments:

    :param longitude (Float): Longitude as defined by sender
    :param latitude (Float): Latitude as defined by sender
    :param horizontal_accuracy (Float number): Optional. The radius of uncertainty for the location, measured in meters; 0-1500
    :param live_period (Integer): Optional. Time relative to the message sending date, during which the location can be updated, in seconds. For active live locations only.
    :param heading (Integer): Optional. The direction in which user is moving, in degrees; 1-360. For active live locations only.
    :param proximity_alert_radius (Integer): Optional. Maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only.
    """
    longitude: float
    latitude: float
    horizontal_accuracy: float
    live_period: int
    heading: int
    proximity_alert_radius: int


@dataclass
class Venue:
    """
    This object represents a venue.

    Keyword arguments:

    :param location (Location): Venue location. Can't be a live location
    :param title (String): Name of the venue
    :param address (String): Address of the venue
    :param foursquare_id (String): Optional. Foursquare identifier of the venue
    :param foursquare_type (String): Optional. Foursquare type of the venue. (For example, \xe2\x80\x9carts_entertainment/default\xe2\x80\x9d, \xe2\x80\x9carts_entertainment/aquarium\xe2\x80\x9d or \xe2\x80\x9cfood/icecream\xe2\x80\x9d.)
    :param google_place_id (String): Optional. Google Places identifier of the venue
    :param google_place_type (String): Optional. Google Places type of the venue. (See supported types.)
    """
    location: Location
    title: str
    address: str
    foursquare_id: str
    foursquare_type: str
    google_place_id: str
    google_place_type: str


@dataclass
class ProximityAlertTriggered:
    """
    This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user.

    Keyword arguments:

    :param traveler (User): User that triggered the alert
    :param watcher (User): User that set the alert
    :param distance (Integer): The distance between the users
    """
    traveler: User
    watcher: User
    distance: int


@dataclass
class MessageAutoDeleteTimerChanged:
    """
    This object represents a service message about a change in auto-delete timer settings.

    Keyword arguments:

    :param message_auto_delete_time (Integer): New auto-delete time for messages in the chat
    """
    message_auto_delete_time: int


@dataclass
class VoiceChatScheduled:
    """
    This object represents a service message about a voice chat scheduled in the chat.

    Keyword arguments:

    :param start_date (Integer): Point in time (Unix timestamp) when the voice chat is supposed to be started by a chat administrator
    """
    start_date: int


@dataclass
class VoiceChatEnded:
    """
    This object represents a service message about a voice chat ended in the chat.

    Keyword arguments:

    :param duration (Integer): Voice chat duration; in seconds
    """
    duration: int


@dataclass
class VoiceChatParticipantsInvited:
    """
    This object represents a service message about new members invited to a voice chat.

    Keyword arguments:

    :param users (Array of User): Optional. New members that were invited to the voice chat
    """
    users: List[User]


@dataclass
class UserProfilePhotos:
    """
    This object represent a user's profile pictures.

    Keyword arguments:

    :param total_count (Integer): Total number of profile pictures the target user has
    :param photos (Array of Array of PhotoSize): Requested profile pictures (in up to 4 sizes each)
    """
    total_count: int
    photos: List[List[PhotoSize]]


@dataclass
class File:
    """
    This object represents a file ready to be downloaded. The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile.
    Maximum file size to download is 20 MB

    Keyword arguments:

    :param file_id (String): Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id (String): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :param file_size (Integer): Optional. File size, if known
    :param file_path (String): Optional. File path. Use https://api.telegram.org/file/bot<token>/<file_path> to get the file.
    """
    file_id: str
    file_unique_id: str
    file_size: int
    file_path: str


@dataclass
class KeyboardButtonPollType:
    """
    This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed.

    Keyword arguments:

    :param type (String): Optional. If quiz is passed, the user will be allowed to create only polls in the quiz mode. If regular is passed, only regular polls will be allowed. Otherwise, the user will be allowed to create a poll of any type.
    """
    type: str


@dataclass
class KeyboardButton:
    """
    This object represents one button of the reply keyboard. For simple text buttons String can be used instead of this object to specify text of the button. Optional fields request_contact, request_location, and request_poll are mutually exclusive.

    Keyword arguments:

    :param text (String): Text of the button. If none of the optional fields are used, it will be sent as a message when the button is pressed
    :param request_contact (Boolean): Optional. If True, the user's phone number will be sent as a contact when the button is pressed. Available in private chats only
    :param request_location (Boolean): Optional. If True, the user's current location will be sent when the button is pressed. Available in private chats only
    :param request_poll (KeyboardButtonPollType): Optional. If specified, the user will be asked to create a poll and send it to the bot when the button is pressed. Available in private chats only
    """
    text: str
    request_contact: bool
    request_location: bool
    request_poll: KeyboardButtonPollType


@dataclass
class ReplyKeyboardMarkup:
    """
    This object represents a custom keyboard with reply options (see Introduction to bots for details and examples).

    Keyword arguments:

    :param keyboard (Array of Array of KeyboardButton): Array of button rows, each represented by an Array of KeyboardButton objects
    :param resize_keyboard (Boolean): Optional. Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons). Defaults to false, in which case the custom keyboard is always of the same height as the app's standard keyboard.
    :param one_time_keyboard (Boolean): Optional. Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available, but clients will automatically display the usual letter-keyboard in the chat \xe2\x80\x93 the user can press a special button in the input field to see the custom keyboard again. Defaults to false.
    :param input_field_placeholder (String): Optional. The placeholder to be shown in the input field when the keyboard is active; 1-64 characters
    :param selective (Boolean): Optional. Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.Example: A user requests to change the bot's language, bot replies to the request with a keyboard to select the new language. Other users in the group don't see the keyboard.
    """
    keyboard: List[List[KeyboardButton]]
    resize_keyboard: bool
    one_time_keyboard: bool
    input_field_placeholder: str
    selective: bool


@dataclass
class ReplyKeyboardRemove:
    """
    Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup).

    Keyword arguments:

    :param remove_keyboard (True): Requests clients to remove the custom keyboard (user will not be able to summon this keyboard; if you want to hide the keyboard from sight but keep it accessible, use one_time_keyboard in ReplyKeyboardMarkup)
    :param selective (Boolean): Optional. Use this parameter if you want to remove the keyboard for specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.Example: A user votes in a poll, bot returns confirmation message in reply to the vote and removes the keyboard for that user, while still showing the keyboard with poll options to users who haven't voted yet.
    """
    remove_keyboard: True
    selective: bool


@dataclass
class LoginUrl:
    """
    This object represents a parameter of the inline keyboard button used to automatically authorize a user. Serves as a great replacement for the Telegram Login Widget when the user is coming from Telegram. All the user needs to do is tap/click a button and confirm that they want to log in:
    Telegram apps support these buttons as of version 5.7.
    Sample bot: @discussbot

    Keyword arguments:

    :param url (String): An HTTP URL to be opened with user authorization data added to the query string when the button is pressed. If the user refuses to provide authorization data, the original URL without information about the user will be opened. The data added is the same as described in Receiving authorization data.NOTE: You must always check the hash of the received data to verify the authentication and the integrity of the data as described in Checking authorization.
    :param forward_text (String): Optional. New text of the button in forwarded messages.
    :param bot_username (String): Optional. Username of a bot, which will be used for user authorization. See Setting up a bot for more details. If not specified, the current bot's username will be assumed. The url's domain must be the same as the domain linked with the bot. See Linking your domain to the bot for more details.
    :param request_write_access (Boolean): Optional. Pass True to request the permission for your bot to send messages to the user.
    """
    url: str
    forward_text: str
    bot_username: str
    request_write_access: bool


@dataclass
class InlineKeyboardButton:
    """
    This object represents one button of an inline keyboard. You must use exactly one of the optional fields.

    Keyword arguments:

    :param text (String): Label text on the button
    :param url (String): Optional. HTTP or tg:// url to be opened when button is pressed
    :param login_url (LoginUrl): Optional. An HTTP URL used to automatically authorize the user. Can be used as a replacement for the Telegram Login Widget.
    :param callback_data (String): Optional. Data to be sent in a callback query to the bot when button is pressed, 1-64 bytes
    :param switch_inline_query (String): Optional. If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field. Can be empty, in which case just the bot's username will be inserted.Note: This offers an easy way for users to start using your bot in inline mode when they are currently in a private chat with it. Especially useful when combined with switch_pm\xe2\x80\xa6 actions \xe2\x80\x93 in this case the user will be automatically returned to the chat they switched from, skipping the chat selection screen.
    :param switch_inline_query_current_chat (String): Optional. If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field. Can be empty, in which case only the bot's username will be inserted.This offers a quick way for the user to open your bot in inline mode in the same chat \xe2\x80\x93 good for selecting something from multiple options.
    :param callback_game (CallbackGame): Optional. Description of the game that will be launched when the user presses the button.NOTE: This type of button must always be the first button in the first row.
    :param pay (Boolean): Optional. Specify True, to send a Pay button.NOTE: This type of button must always be the first button in the first row.
    """
    text: str
    url: str
    login_url: LoginUrl
    callback_data: str
    switch_inline_query: str
    switch_inline_query_current_chat: str
    callback_game: CallbackGame
    pay: bool


@dataclass
class InlineKeyboardMarkup:
    """
    This object represents an inline keyboard that appears right next to the message it belongs to.

    Keyword arguments:

    :param inline_keyboard (Array of Array of InlineKeyboardButton): Array of button rows, each represented by an Array of InlineKeyboardButton objects
    """
    inline_keyboard: List[List[InlineKeyboardButton]]


@dataclass
class CallbackQuery:
    """
    This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present.

    Keyword arguments:

    :param id (String): Unique identifier for this query
    :param _from (User): Sender
    :param message (Message): Optional. Message with the callback button that originated the query. Note that message content and message date will not be available if the message is too old
    :param inline_message_id (String): Optional. Identifier of the message sent via the bot in inline mode, that originated the query.
    :param chat_instance (String): Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games.
    :param data (String): Optional. Data associated with the callback button. Be aware that a bad client can send arbitrary data in this field.
    :param game_short_name (String): Optional. Short name of a Game to be returned, serves as the unique identifier for the game
    """
    id: str
    _from: User
    message: "Message"
    inline_message_id: str
    chat_instance: str
    data: str
    game_short_name: str


@dataclass
class ForceReply:
    """
    Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode.

    Keyword arguments:

    :param force_reply (True): Shows reply interface to the user, as if they manually selected the bot's message and tapped 'Reply'
    :param input_field_placeholder (String): Optional. The placeholder to be shown in the input field when the reply is active; 1-64 characters
    :param selective (Boolean): Optional. Use this parameter if you want to force reply from specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.
    """
    force_reply: True
    input_field_placeholder: str
    selective: bool


@dataclass
class ChatPhoto:
    """
    This object represents a chat photo.

    Keyword arguments:

    :param small_file_id (String): File identifier of small (160x160) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.
    :param small_file_unique_id (String): Unique file identifier of small (160x160) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :param big_file_id (String): File identifier of big (640x640) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.
    :param big_file_unique_id (String): Unique file identifier of big (640x640) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    """
    small_file_id: str
    small_file_unique_id: str
    big_file_id: str
    big_file_unique_id: str


@dataclass
class ChatInviteLink:
    """
    Represents an invite link for a chat.

    Keyword arguments:

    :param invite_link (String): The invite link. If the link was created by another chat administrator, then the second part of the link will be replaced with \xe2\x80\x9c\xe2\x80\xa6\xe2\x80\x9d.
    :param creator (User): Creator of the link
    :param is_primary (Boolean): True, if the link is primary
    :param is_revoked (Boolean): True, if the link is revoked
    :param expire_date (Integer): Optional. Point in time (Unix timestamp) when the link will expire or has been expired
    :param member_limit (Integer): Optional. Maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999
    """
    invite_link: str
    creator: User
    is_primary: bool
    is_revoked: bool
    expire_date: int
    member_limit: int


@dataclass
class ChatMemberOwner:
    """
    Represents a chat member that owns the chat and has all administrator privileges.

    Keyword arguments:

    :param status (String): The member's status in the chat, always \xe2\x80\x9ccreator\xe2\x80\x9d
    :param user (User): Information about the user
    :param is_anonymous (Boolean): True, if the user's presence in the chat is hidden
    :param custom_title (String): Optional. Custom title for this user
    """
    status: str
    user: User
    is_anonymous: bool
    custom_title: str


@dataclass
class ChatMemberAdministrator:
    """
    Represents a chat member that has some additional privileges.

    Keyword arguments:

    :param status (String): The member's status in the chat, always \xe2\x80\x9cadministrator\xe2\x80\x9d
    :param user (User): Information about the user
    :param can_be_edited (Boolean): True, if the bot is allowed to edit administrator privileges of that user
    :param is_anonymous (Boolean): True, if the user's presence in the chat is hidden
    :param can_manage_chat (Boolean): True, if the administrator can access the chat event log, chat statistics, message statistics in channels, see channel members, see anonymous administrators in supergroups and ignore slow mode. Implied by any other administrator privilege
    :param can_delete_messages (Boolean): True, if the administrator can delete messages of other users
    :param can_manage_voice_chats (Boolean): True, if the administrator can manage voice chats
    :param can_restrict_members (Boolean): True, if the administrator can restrict, ban or unban chat members
    :param can_promote_members (Boolean): True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user)
    :param can_change_info (Boolean): True, if the user is allowed to change the chat title, photo and other settings
    :param can_invite_users (Boolean): True, if the user is allowed to invite new users to the chat
    :param can_post_messages (Boolean): Optional. True, if the administrator can post in the channel; channels only
    :param can_edit_messages (Boolean): Optional. True, if the administrator can edit messages of other users and can pin messages; channels only
    :param can_pin_messages (Boolean): Optional. True, if the user is allowed to pin messages; groups and supergroups only
    :param custom_title (String): Optional. Custom title for this user
    """
    status: str
    user: User
    can_be_edited: bool
    is_anonymous: bool
    can_manage_chat: bool
    can_delete_messages: bool
    can_manage_voice_chats: bool
    can_restrict_members: bool
    can_promote_members: bool
    can_change_info: bool
    can_invite_users: bool
    can_post_messages: bool
    can_edit_messages: bool
    can_pin_messages: bool
    custom_title: str


@dataclass
class ChatMemberMember:
    """
    Represents a chat member that has no additional privileges or restrictions.

    Keyword arguments:

    :param status (String): The member's status in the chat, always \xe2\x80\x9cmember\xe2\x80\x9d
    :param user (User): Information about the user
    """
    status: str
    user: User


@dataclass
class ChatMemberRestricted:
    """
    Represents a chat member that is under certain restrictions in the chat. Supergroups only.

    Keyword arguments:

    :param status (String): The member's status in the chat, always \xe2\x80\x9crestricted\xe2\x80\x9d
    :param user (User): Information about the user
    :param is_member (Boolean): True, if the user is a member of the chat at the moment of the request
    :param can_change_info (Boolean): True, if the user is allowed to change the chat title, photo and other settings
    :param can_invite_users (Boolean): True, if the user is allowed to invite new users to the chat
    :param can_pin_messages (Boolean): True, if the user is allowed to pin messages
    :param can_send_messages (Boolean): True, if the user is allowed to send text messages, contacts, locations and venues
    :param can_send_media_messages (Boolean): True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes
    :param can_send_polls (Boolean): True, if the user is allowed to send polls
    :param can_send_other_messages (Boolean): True, if the user is allowed to send animations, games, stickers and use inline bots
    :param can_add_web_page_previews (Boolean): True, if the user is allowed to add web page previews to their messages
    :param until_date (Integer): Date when restrictions will be lifted for this user; unix time. If 0, then the user is restricted forever
    """
    status: str
    user: User
    is_member: bool
    can_change_info: bool
    can_invite_users: bool
    can_pin_messages: bool
    can_send_messages: bool
    can_send_media_messages: bool
    can_send_polls: bool
    can_send_other_messages: bool
    can_add_web_page_previews: bool
    until_date: int


@dataclass
class ChatMemberLeft:
    """
    Represents a chat member that isn't currently a member of the chat, but may join it themselves.

    Keyword arguments:

    :param status (String): The member's status in the chat, always \xe2\x80\x9cleft\xe2\x80\x9d
    :param user (User): Information about the user
    """
    status: str
    user: User


@dataclass
class ChatMemberBanned:
    """
    Represents a chat member that was banned in the chat and can't return to the chat or view chat messages.

    Keyword arguments:

    :param status (String): The member's status in the chat, always \xe2\x80\x9ckicked\xe2\x80\x9d
    :param user (User): Information about the user
    :param until_date (Integer): Date when restrictions will be lifted for this user; unix time. If 0, then the user is banned forever
    """
    status: str
    user: User
    until_date: int


@dataclass
class ChatPermissions:
    """
    Describes actions that a non-administrator user is allowed to take in a chat.

    Keyword arguments:

    :param can_send_messages (Boolean): Optional. True, if the user is allowed to send text messages, contacts, locations and venues
    :param can_send_media_messages (Boolean): Optional. True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes, implies can_send_messages
    :param can_send_polls (Boolean): Optional. True, if the user is allowed to send polls, implies can_send_messages
    :param can_send_other_messages (Boolean): Optional. True, if the user is allowed to send animations, games, stickers and use inline bots, implies can_send_media_messages
    :param can_add_web_page_previews (Boolean): Optional. True, if the user is allowed to add web page previews to their messages, implies can_send_media_messages
    :param can_change_info (Boolean): Optional. True, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups
    :param can_invite_users (Boolean): Optional. True, if the user is allowed to invite new users to the chat
    :param can_pin_messages (Boolean): Optional. True, if the user is allowed to pin messages. Ignored in public supergroups
    """
    can_send_messages: bool
    can_send_media_messages: bool
    can_send_polls: bool
    can_send_other_messages: bool
    can_add_web_page_previews: bool
    can_change_info: bool
    can_invite_users: bool
    can_pin_messages: bool


@dataclass
class ChatLocation:
    """
    Represents a location to which a chat is connected.

    Keyword arguments:

    :param location (Location): The location to which the supergroup is connected. Can't be a live location.
    :param address (String): Location address; 1-64 characters, as defined by the chat owner
    """
    location: Location
    address: str


@dataclass
class BotCommand:
    """
    This object represents a bot command.

    Keyword arguments:

    :param command (String): Text of the command, 1-32 characters. Can contain only lowercase English letters, digits and underscores.
    :param description (String): Description of the command, 3-256 characters.
    """
    command: str
    description: str


@dataclass
class BotCommandScopeDefault:
    """
    Represents the default scope of bot commands. Default commands are used if no commands with a narrower scope are specified for the user.

    Keyword arguments:

    :param type (String): Scope type, must be default
    """
    type: str


@dataclass
class BotCommandScopeAllPrivateChats:
    """
    Represents the scope of bot commands, covering all private chats.

    Keyword arguments:

    :param type (String): Scope type, must be all_private_chats
    """
    type: str


@dataclass
class BotCommandScopeAllGroupChats:
    """
    Represents the scope of bot commands, covering all group and supergroup chats.

    Keyword arguments:

    :param type (String): Scope type, must be all_group_chats
    """
    type: str


@dataclass
class BotCommandScopeAllChatAdministrators:
    """
    Represents the scope of bot commands, covering all group and supergroup chat administrators.

    Keyword arguments:

    :param type (String): Scope type, must be all_chat_administrators
    """
    type: str


@dataclass
class BotCommandScopeChat:
    """
    Represents the scope of bot commands, covering a specific chat.

    Keyword arguments:

    :param type (String): Scope type, must be chat
    :param chat_id (Integer or String): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
    """
    type: str
    chat_id: Union[int, str]


@dataclass
class BotCommandScopeChatAdministrators:
    """
    Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat.

    Keyword arguments:

    :param type (String): Scope type, must be chat_administrators
    :param chat_id (Integer or String): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
    """
    type: str
    chat_id: Union[int, str]


@dataclass
class BotCommandScopeChatMember:
    """
    Represents the scope of bot commands, covering a specific member of a group or supergroup chat.

    Keyword arguments:

    :param type (String): Scope type, must be chat_member
    :param chat_id (Integer or String): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
    :param user_id (Integer): Unique identifier of the target user
    """
    type: str
    chat_id: Union[int, str]
    user_id: int


@dataclass
class ResponseParameters:
    """
    Contains information about why a request was unsuccessful.

    Keyword arguments:

    :param migrate_to_chat_id (Integer): Optional. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    :param retry_after (Integer): Optional. In case of exceeding flood control, the number of seconds left to wait before the request can be repeated
    """
    migrate_to_chat_id: int
    retry_after: int


@dataclass
class InputMediaPhoto:
    """
    Represents a photo to be sent.

    Keyword arguments:

    :param type (String): Type of the result, must be photo
    :param media (String): File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass \xe2\x80\x9cattach://<file_attach_name>\xe2\x80\x9d to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files \xc2\xbb
    :param caption (String): Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
    :param parse_mode (String): Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
    :param caption_entities (Array of MessageEntity): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    """
    type: str
    media: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]


@dataclass
class InputMediaVideo:
    """
    Represents a video to be sent.

    Keyword arguments:

    :param type (String): Type of the result, must be video
    :param media (String): File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass \xe2\x80\x9cattach://<file_attach_name>\xe2\x80\x9d to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files \xc2\xbb
    :param thumb (InputFile or String): Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass \xe2\x80\x9cattach://<file_attach_name>\xe2\x80\x9d if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files \xc2\xbb
    :param caption (String): Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
    :param parse_mode (String): Optional. Mode for parsing entities in the video caption. See formatting options for more details.
    :param caption_entities (Array of MessageEntity): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :param width (Integer): Optional. Video width
    :param height (Integer): Optional. Video height
    :param duration (Integer): Optional. Video duration
    :param supports_streaming (Boolean): Optional. Pass True, if the uploaded video is suitable for streaming
    """
    type: str
    media: str
    thumb: Union[InputFile, str]
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    width: int
    height: int
    duration: int
    supports_streaming: bool


@dataclass
class InputMediaAnimation:
    """
    Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.

    Keyword arguments:

    :param type (String): Type of the result, must be animation
    :param media (String): File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass \xe2\x80\x9cattach://<file_attach_name>\xe2\x80\x9d to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files \xc2\xbb
    :param thumb (InputFile or String): Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass \xe2\x80\x9cattach://<file_attach_name>\xe2\x80\x9d if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files \xc2\xbb
    :param caption (String): Optional. Caption of the animation to be sent, 0-1024 characters after entities parsing
    :param parse_mode (String): Optional. Mode for parsing entities in the animation caption. See formatting options for more details.
    :param caption_entities (Array of MessageEntity): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :param width (Integer): Optional. Animation width
    :param height (Integer): Optional. Animation height
    :param duration (Integer): Optional. Animation duration
    """
    type: str
    media: str
    thumb: Union[InputFile, str]
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    width: int
    height: int
    duration: int


@dataclass
class InputMediaAudio:
    """
    Represents an audio file to be treated as music to be sent.

    Keyword arguments:

    :param type (String): Type of the result, must be audio
    :param media (String): File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass \xe2\x80\x9cattach://<file_attach_name>\xe2\x80\x9d to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files \xc2\xbb
    :param thumb (InputFile or String): Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass \xe2\x80\x9cattach://<file_attach_name>\xe2\x80\x9d if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files \xc2\xbb
    :param caption (String): Optional. Caption of the audio to be sent, 0-1024 characters after entities parsing
    :param parse_mode (String): Optional. Mode for parsing entities in the audio caption. See formatting options for more details.
    :param caption_entities (Array of MessageEntity): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :param duration (Integer): Optional. Duration of the audio in seconds
    :param performer (String): Optional. Performer of the audio
    :param title (String): Optional. Title of the audio
    """
    type: str
    media: str
    thumb: Union[InputFile, str]
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    duration: int
    performer: str
    title: str


@dataclass
class InputMediaDocument:
    """
    Represents a general file to be sent.

    Keyword arguments:

    :param type (String): Type of the result, must be document
    :param media (String): File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass \xe2\x80\x9cattach://<file_attach_name>\xe2\x80\x9d to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files \xc2\xbb
    :param thumb (InputFile or String): Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass \xe2\x80\x9cattach://<file_attach_name>\xe2\x80\x9d if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files \xc2\xbb
    :param caption (String): Optional. Caption of the document to be sent, 0-1024 characters after entities parsing
    :param parse_mode (String): Optional. Mode for parsing entities in the document caption. See formatting options for more details.
    :param caption_entities (Array of MessageEntity): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :param disable_content_type_detection (Boolean): Optional. Disables automatic server-side content type detection for files uploaded using multipart/form-data. Always true, if the document is sent as part of an album.
    """
    type: str
    media: str
    thumb: Union[InputFile, str]
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    disable_content_type_detection: bool


@dataclass
class MaskPosition:
    """
    This object describes the position on faces where a mask should be placed by default.

    Keyword arguments:

    :param point (String): The part of the face relative to which the mask should be placed. One of \xe2\x80\x9cforehead\xe2\x80\x9d, \xe2\x80\x9ceyes\xe2\x80\x9d, \xe2\x80\x9cmouth\xe2\x80\x9d, or \xe2\x80\x9cchin\xe2\x80\x9d.
    :param x_shift (Float number): Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. For example, choosing -1.0 will place mask just to the left of the default mask position.
    :param y_shift (Float number): Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. For example, 1.0 will place the mask just below the default mask position.
    :param scale (Float number): Mask scaling coefficient. For example, 2.0 means double size.
    """
    point: str
    x_shift: float
    y_shift: float
    scale: float


@dataclass
class Sticker:
    """
    This object represents a sticker.

    Keyword arguments:

    :param file_id (String): Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id (String): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :param width (Integer): Sticker width
    :param height (Integer): Sticker height
    :param is_animated (Boolean): True, if the sticker is animated
    :param thumb (PhotoSize): Optional. Sticker thumbnail in the .WEBP or .JPG format
    :param emoji (String): Optional. Emoji associated with the sticker
    :param set_name (String): Optional. Name of the sticker set to which the sticker belongs
    :param mask_position (MaskPosition): Optional. For mask stickers, the position where the mask should be placed
    :param file_size (Integer): Optional. File size
    """
    file_id: str
    file_unique_id: str
    width: int
    height: int
    is_animated: bool
    thumb: PhotoSize
    emoji: str
    set_name: str
    mask_position: MaskPosition
    file_size: int


@dataclass
class StickerSet:
    """
    This object represents a sticker set.

    Keyword arguments:

    :param name (String): Sticker set name
    :param title (String): Sticker set title
    :param is_animated (Boolean): True, if the sticker set contains animated stickers
    :param contains_masks (Boolean): True, if the sticker set contains masks
    :param stickers (Array of Sticker): List of all set stickers
    :param thumb (PhotoSize): Optional. Sticker set thumbnail in the .WEBP or .TGS format
    """
    name: str
    title: str
    is_animated: bool
    contains_masks: bool
    stickers: List[Sticker]
    thumb: PhotoSize


@dataclass
class InlineQuery:
    """
    This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.

    Keyword arguments:

    :param id (String): Unique identifier for this query
    :param _from (User): Sender
    :param query (String): Text of the query (up to 256 characters)
    :param offset (String): Offset of the results to be returned, can be controlled by the bot
    :param chat_type (String): Optional. Type of the chat, from which the inline query was sent. Can be either \xe2\x80\x9csender\xe2\x80\x9d for a private chat with the inline query sender, \xe2\x80\x9cprivate\xe2\x80\x9d, \xe2\x80\x9cgroup\xe2\x80\x9d, \xe2\x80\x9csupergroup\xe2\x80\x9d, or \xe2\x80\x9cchannel\xe2\x80\x9d. The chat type should be always known for requests sent from official clients and most third-party clients, unless the request was sent from a secret chat
    :param location (Location): Optional. Sender location, only for bots that request user location
    """
    id: str
    _from: User
    query: str
    offset: str
    chat_type: str
    location: Location


@dataclass
class InlineQueryResultArticle:
    """
    Represents a link to an article or web page.

    Keyword arguments:

    :param type (String): Type of the result, must be article
    :param id (String): Unique identifier for this result, 1-64 Bytes
    :param title (String): Title of the result
    :param input_message_content (InputMessageContent): Content of the message to be sent
    :param reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
    :param url (String): Optional. URL of the result
    :param hide_url (Boolean): Optional. Pass True, if you don't want the URL to be shown in the message
    :param description (String): Optional. Short description of the result
    :param thumb_url (String): Optional. Url of the thumbnail for the result
    :param thumb_width (Integer): Optional. Thumbnail width
    :param thumb_height (Integer): Optional. Thumbnail height
    """
    type: str
    id: str
    title: str
    input_message_content: InputMessageContent
    reply_markup: InlineKeyboardMarkup
    url: str
    hide_url: bool
    description: str
    thumb_url: str
    thumb_width: int
    thumb_height: int


@dataclass
class InlineQueryResultPhoto:
    """
    Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

    Keyword arguments:

    :param type (String): Type of the result, must be photo
    :param id (String): Unique identifier for this result, 1-64 bytes
    :param photo_url (String): A valid URL of the photo. Photo must be in jpeg format. Photo size must not exceed 5MB
    :param thumb_url (String): URL of the thumbnail for the photo
    :param photo_width (Integer): Optional. Width of the photo
    :param photo_height (Integer): Optional. Height of the photo
    :param title (String): Optional. Title for the result
    :param description (String): Optional. Short description of the result
    :param caption (String): Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
    :param parse_mode (String): Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
    :param caption_entities (Array of MessageEntity): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :param reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
    :param input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the photo
    """
    type: str
    id: str
    photo_url: str
    thumb_url: str
    photo_width: int
    photo_height: int
    title: str
    description: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


@dataclass
class InlineQueryResultGif:
    """
    Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    Keyword arguments:

    :param type (String): Type of the result, must be gif
    :param id (String): Unique identifier for this result, 1-64 bytes
    :param gif_url (String): A valid URL for the GIF file. File size must not exceed 1MB
    :param gif_width (Integer): Optional. Width of the GIF
    :param gif_height (Integer): Optional. Height of the GIF
    :param gif_duration (Integer): Optional. Duration of the GIF
    :param thumb_url (String): URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
    :param thumb_mime_type (String): Optional. MIME type of the thumbnail, must be one of \xe2\x80\x9cimage/jpeg\xe2\x80\x9d, \xe2\x80\x9cimage/gif\xe2\x80\x9d, or \xe2\x80\x9cvideo/mp4\xe2\x80\x9d. Defaults to \xe2\x80\x9cimage/jpeg\xe2\x80\x9d
    :param title (String): Optional. Title for the result
    :param caption (String): Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing
    :param parse_mode (String): Optional. Mode for parsing entities in the caption. See formatting options for more details.
    :param caption_entities (Array of MessageEntity): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :param reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
    :param input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the GIF animation
    """
    type: str
    id: str
    gif_url: str
    gif_width: int
    gif_height: int
    gif_duration: int
    thumb_url: str
    thumb_mime_type: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


@dataclass
class InlineQueryResultMpeg4Gif:
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    Keyword arguments:

    :param type (String): Type of the result, must be mpeg4_gif
    :param id (String): Unique identifier for this result, 1-64 bytes
    :param mpeg4_url (String): A valid URL for the MP4 file. File size must not exceed 1MB
    :param mpeg4_width (Integer): Optional. Video width
    :param mpeg4_height (Integer): Optional. Video height
    :param mpeg4_duration (Integer): Optional. Video duration
    :param thumb_url (String): URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
    :param thumb_mime_type (String): Optional. MIME type of the thumbnail, must be one of \xe2\x80\x9cimage/jpeg\xe2\x80\x9d, \xe2\x80\x9cimage/gif\xe2\x80\x9d, or \xe2\x80\x9cvideo/mp4\xe2\x80\x9d. Defaults to \xe2\x80\x9cimage/jpeg\xe2\x80\x9d
    :param title (String): Optional. Title for the result
    :param caption (String): Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing
    :param parse_mode (String): Optional. Mode for parsing entities in the caption. See formatting options for more details.
    :param caption_entities (Array of MessageEntity): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :param reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
    :param input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the video animation
    """
    type: str
    id: str
    mpeg4_url: str
    mpeg4_width: int
    mpeg4_height: int
    mpeg4_duration: int
    thumb_url: str
    thumb_mime_type: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


@dataclass
class InlineQueryResultVideo:
    """
    Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.
    If an InlineQueryResultVideo message contains an embedded video (e.g., YouTube), you must replace its content using input_message_content.

    Keyword arguments:

    :param type (String): Type of the result, must be video
    :param id (String): Unique identifier for this result, 1-64 bytes
    :param video_url (String): A valid URL for the embedded video player or video file
    :param mime_type (String): Mime type of the content of video url, \xe2\x80\x9ctext/html\xe2\x80\x9d or \xe2\x80\x9cvideo/mp4\xe2\x80\x9d
    :param thumb_url (String): URL of the thumbnail (jpeg only) for the video
    :param title (String): Title for the result
    :param caption (String): Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
    :param parse_mode (String): Optional. Mode for parsing entities in the video caption. See formatting options for more details.
    :param caption_entities (Array of MessageEntity): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :param video_width (Integer): Optional. Video width
    :param video_height (Integer): Optional. Video height
    :param video_duration (Integer): Optional. Video duration in seconds
    :param description (String): Optional. Short description of the result
    :param reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
    :param input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the video. This field is required if InlineQueryResultVideo is used to send an HTML-page as a result (e.g., a YouTube video).
    """
    type: str
    id: str
    video_url: str
    mime_type: str
    thumb_url: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    video_width: int
    video_height: int
    video_duration: int
    description: str
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


@dataclass
class InlineQueryResultAudio:
    """
    Represents a link to an MP3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.

    Keyword arguments:

    :param type (String): Type of the result, must be audio
    :param id (String): Unique identifier for this result, 1-64 bytes
    :param audio_url (String): A valid URL for the audio file
    :param title (String): Title
    :param caption (String): Optional. Caption, 0-1024 characters after entities parsing
    :param parse_mode (String): Optional. Mode for parsing entities in the audio caption. See formatting options for more details.
    :param caption_entities (Array of MessageEntity): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :param performer (String): Optional. Performer
    :param audio_duration (Integer): Optional. Audio duration in seconds
    :param reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
    :param input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the audio
    """
    type: str
    id: str
    audio_url: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    performer: str
    audio_duration: int
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


@dataclass
class InlineQueryResultVoice:
    """
    Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message.

    Keyword arguments:

    :param type (String): Type of the result, must be voice
    :param id (String): Unique identifier for this result, 1-64 bytes
    :param voice_url (String): A valid URL for the voice recording
    :param title (String): Recording title
    :param caption (String): Optional. Caption, 0-1024 characters after entities parsing
    :param parse_mode (String): Optional. Mode for parsing entities in the voice message caption. See formatting options for more details.
    :param caption_entities (Array of MessageEntity): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :param voice_duration (Integer): Optional. Recording duration in seconds
    :param reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
    :param input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the voice recording
    """
    type: str
    id: str
    voice_url: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    voice_duration: int
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


@dataclass
class InlineQueryResultDocument:
    """
    Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.

    Keyword arguments:

    :param type (String): Type of the result, must be document
    :param id (String): Unique identifier for this result, 1-64 bytes
    :param title (String): Title for the result
    :param caption (String): Optional. Caption of the document to be sent, 0-1024 characters after entities parsing
    :param parse_mode (String): Optional. Mode for parsing entities in the document caption. See formatting options for more details.
    :param caption_entities (Array of MessageEntity): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :param document_url (String): A valid URL for the file
    :param mime_type (String): Mime type of the content of the file, either \xe2\x80\x9capplication/pdf\xe2\x80\x9d or \xe2\x80\x9capplication/zip\xe2\x80\x9d
    :param description (String): Optional. Short description of the result
    :param reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
    :param input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the file
    :param thumb_url (String): Optional. URL of the thumbnail (jpeg only) for the file
    :param thumb_width (Integer): Optional. Thumbnail width
    :param thumb_height (Integer): Optional. Thumbnail height
    """
    type: str
    id: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    document_url: str
    mime_type: str
    description: str
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
    thumb_url: str
    thumb_width: int
    thumb_height: int


@dataclass
class InlineQueryResultLocation:
    """
    Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.

    Keyword arguments:

    :param type (String): Type of the result, must be location
    :param id (String): Unique identifier for this result, 1-64 Bytes
    :param latitude (Float number): Location latitude in degrees
    :param longitude (Float number): Location longitude in degrees
    :param title (String): Location title
    :param horizontal_accuracy (Float number): Optional. The radius of uncertainty for the location, measured in meters; 0-1500
    :param live_period (Integer): Optional. Period in seconds for which the location can be updated, should be between 60 and 86400.
    :param heading (Integer): Optional. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
    :param proximity_alert_radius (Integer): Optional. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
    :param reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
    :param input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the location
    :param thumb_url (String): Optional. Url of the thumbnail for the result
    :param thumb_width (Integer): Optional. Thumbnail width
    :param thumb_height (Integer): Optional. Thumbnail height
    """
    type: str
    id: str
    latitude: float
    longitude: float
    title: str
    horizontal_accuracy: float
    live_period: int
    heading: int
    proximity_alert_radius: int
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
    thumb_url: str
    thumb_width: int
    thumb_height: int


@dataclass
class InlineQueryResultVenue:
    """
    Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.

    Keyword arguments:

    :param type (String): Type of the result, must be venue
    :param id (String): Unique identifier for this result, 1-64 Bytes
    :param latitude (Float): Latitude of the venue location in degrees
    :param longitude (Float): Longitude of the venue location in degrees
    :param title (String): Title of the venue
    :param address (String): Address of the venue
    :param foursquare_id (String): Optional. Foursquare identifier of the venue if known
    :param foursquare_type (String): Optional. Foursquare type of the venue, if known. (For example, \xe2\x80\x9carts_entertainment/default\xe2\x80\x9d, \xe2\x80\x9carts_entertainment/aquarium\xe2\x80\x9d or \xe2\x80\x9cfood/icecream\xe2\x80\x9d.)
    :param google_place_id (String): Optional. Google Places identifier of the venue
    :param google_place_type (String): Optional. Google Places type of the venue. (See supported types.)
    :param reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
    :param input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the venue
    :param thumb_url (String): Optional. Url of the thumbnail for the result
    :param thumb_width (Integer): Optional. Thumbnail width
    :param thumb_height (Integer): Optional. Thumbnail height
    """
    type: str
    id: str
    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: str
    foursquare_type: str
    google_place_id: str
    google_place_type: str
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
    thumb_url: str
    thumb_width: int
    thumb_height: int


@dataclass
class InlineQueryResultContact:
    """
    Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.

    Keyword arguments:

    :param type (String): Type of the result, must be contact
    :param id (String): Unique identifier for this result, 1-64 Bytes
    :param phone_number (String): Contact's phone number
    :param first_name (String): Contact's first name
    :param last_name (String): Optional. Contact's last name
    :param vcard (String): Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes
    :param reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
    :param input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the contact
    :param thumb_url (String): Optional. Url of the thumbnail for the result
    :param thumb_width (Integer): Optional. Thumbnail width
    :param thumb_height (Integer): Optional. Thumbnail height
    """
    type: str
    id: str
    phone_number: str
    first_name: str
    last_name: str
    vcard: str
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
    thumb_url: str
    thumb_width: int
    thumb_height: int


@dataclass
class InlineQueryResultGame:
    """
    Represents a Game.

    Keyword arguments:

    :param type (String): Type of the result, must be game
    :param id (String): Unique identifier for this result, 1-64 bytes
    :param game_short_name (String): Short name of the game
    :param reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
    """
    type: str
    id: str
    game_short_name: str
    reply_markup: InlineKeyboardMarkup


@dataclass
class InlineQueryResultCachedPhoto:
    """
    Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

    Keyword arguments:

    :param type (String): Type of the result, must be photo
    :param id (String): Unique identifier for this result, 1-64 bytes
    :param photo_file_id (String): A valid file identifier of the photo
    :param title (String): Optional. Title for the result
    :param description (String): Optional. Short description of the result
    :param caption (String): Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
    :param parse_mode (String): Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
    :param caption_entities (Array of MessageEntity): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :param reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
    :param input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the photo
    """
    type: str
    id: str
    photo_file_id: str
    title: str
    description: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


@dataclass
class InlineQueryResultCachedGif:
    """
    Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation.

    Keyword arguments:

    :param type (String): Type of the result, must be gif
    :param id (String): Unique identifier for this result, 1-64 bytes
    :param gif_file_id (String): A valid file identifier for the GIF file
    :param title (String): Optional. Title for the result
    :param caption (String): Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing
    :param parse_mode (String): Optional. Mode for parsing entities in the caption. See formatting options for more details.
    :param caption_entities (Array of MessageEntity): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :param reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
    :param input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the GIF animation
    """
    type: str
    id: str
    gif_file_id: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


@dataclass
class InlineQueryResultCachedMpeg4Gif:
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    Keyword arguments:

    :param type (String): Type of the result, must be mpeg4_gif
    :param id (String): Unique identifier for this result, 1-64 bytes
    :param mpeg4_file_id (String): A valid file identifier for the MP4 file
    :param title (String): Optional. Title for the result
    :param caption (String): Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing
    :param parse_mode (String): Optional. Mode for parsing entities in the caption. See formatting options for more details.
    :param caption_entities (Array of MessageEntity): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :param reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
    :param input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the video animation
    """
    type: str
    id: str
    mpeg4_file_id: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


@dataclass
class InlineQueryResultCachedSticker:
    """
    Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker.

    Keyword arguments:

    :param type (String): Type of the result, must be sticker
    :param id (String): Unique identifier for this result, 1-64 bytes
    :param sticker_file_id (String): A valid file identifier of the sticker
    :param reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
    :param input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the sticker
    """
    type: str
    id: str
    sticker_file_id: str
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


@dataclass
class InlineQueryResultCachedDocument:
    """
    Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file.

    Keyword arguments:

    :param type (String): Type of the result, must be document
    :param id (String): Unique identifier for this result, 1-64 bytes
    :param title (String): Title for the result
    :param document_file_id (String): A valid file identifier for the file
    :param description (String): Optional. Short description of the result
    :param caption (String): Optional. Caption of the document to be sent, 0-1024 characters after entities parsing
    :param parse_mode (String): Optional. Mode for parsing entities in the document caption. See formatting options for more details.
    :param caption_entities (Array of MessageEntity): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :param reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
    :param input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the file
    """
    type: str
    id: str
    title: str
    document_file_id: str
    description: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


@dataclass
class InlineQueryResultCachedVideo:
    """
    Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

    Keyword arguments:

    :param type (String): Type of the result, must be video
    :param id (String): Unique identifier for this result, 1-64 bytes
    :param video_file_id (String): A valid file identifier for the video file
    :param title (String): Title for the result
    :param description (String): Optional. Short description of the result
    :param caption (String): Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
    :param parse_mode (String): Optional. Mode for parsing entities in the video caption. See formatting options for more details.
    :param caption_entities (Array of MessageEntity): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :param reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
    :param input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the video
    """
    type: str
    id: str
    video_file_id: str
    title: str
    description: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


@dataclass
class InlineQueryResultCachedVoice:
    """
    Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message.

    Keyword arguments:

    :param type (String): Type of the result, must be voice
    :param id (String): Unique identifier for this result, 1-64 bytes
    :param voice_file_id (String): A valid file identifier for the voice message
    :param title (String): Voice message title
    :param caption (String): Optional. Caption, 0-1024 characters after entities parsing
    :param parse_mode (String): Optional. Mode for parsing entities in the voice message caption. See formatting options for more details.
    :param caption_entities (Array of MessageEntity): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :param reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
    :param input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the voice message
    """
    type: str
    id: str
    voice_file_id: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


@dataclass
class InlineQueryResultCachedAudio:
    """
    Represents a link to an MP3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.

    Keyword arguments:

    :param type (String): Type of the result, must be audio
    :param id (String): Unique identifier for this result, 1-64 bytes
    :param audio_file_id (String): A valid file identifier for the audio file
    :param caption (String): Optional. Caption, 0-1024 characters after entities parsing
    :param parse_mode (String): Optional. Mode for parsing entities in the audio caption. See formatting options for more details.
    :param caption_entities (Array of MessageEntity): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :param reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
    :param input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the audio
    """
    type: str
    id: str
    audio_file_id: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent


@dataclass
class InputTextMessageContent:
    """
    Represents the content of a text message to be sent as the result of an inline query.

    Keyword arguments:

    :param message_text (String): Text of the message to be sent, 1-4096 characters
    :param parse_mode (String): Optional. Mode for parsing entities in the message text. See formatting options for more details.
    :param entities (Array of MessageEntity): Optional. List of special entities that appear in message text, which can be specified instead of parse_mode
    :param disable_web_page_preview (Boolean): Optional. Disables link previews for links in the sent message
    """
    message_text: str
    parse_mode: str
    entities: List[MessageEntity]
    disable_web_page_preview: bool


@dataclass
class InputLocationMessageContent:
    """
    Represents the content of a location message to be sent as the result of an inline query.

    Keyword arguments:

    :param latitude (Float): Latitude of the location in degrees
    :param longitude (Float): Longitude of the location in degrees
    :param horizontal_accuracy (Float number): Optional. The radius of uncertainty for the location, measured in meters; 0-1500
    :param live_period (Integer): Optional. Period in seconds for which the location can be updated, should be between 60 and 86400.
    :param heading (Integer): Optional. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
    :param proximity_alert_radius (Integer): Optional. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
    """
    latitude: float
    longitude: float
    horizontal_accuracy: float
    live_period: int
    heading: int
    proximity_alert_radius: int


@dataclass
class InputVenueMessageContent:
    """
    Represents the content of a venue message to be sent as the result of an inline query.

    Keyword arguments:

    :param latitude (Float): Latitude of the venue in degrees
    :param longitude (Float): Longitude of the venue in degrees
    :param title (String): Name of the venue
    :param address (String): Address of the venue
    :param foursquare_id (String): Optional. Foursquare identifier of the venue, if known
    :param foursquare_type (String): Optional. Foursquare type of the venue, if known. (For example, \xe2\x80\x9carts_entertainment/default\xe2\x80\x9d, \xe2\x80\x9carts_entertainment/aquarium\xe2\x80\x9d or \xe2\x80\x9cfood/icecream\xe2\x80\x9d.)
    :param google_place_id (String): Optional. Google Places identifier of the venue
    :param google_place_type (String): Optional. Google Places type of the venue. (See supported types.)
    """
    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: str
    foursquare_type: str
    google_place_id: str
    google_place_type: str


@dataclass
class InputContactMessageContent:
    """
    Represents the content of a contact message to be sent as the result of an inline query.

    Keyword arguments:

    :param phone_number (String): Contact's phone number
    :param first_name (String): Contact's first name
    :param last_name (String): Optional. Contact's last name
    :param vcard (String): Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes
    """
    phone_number: str
    first_name: str
    last_name: str
    vcard: str


@dataclass
class LabeledPrice:
    """
    This object represents a portion of the price for goods or services.

    Keyword arguments:

    :param label (String): Portion label
    :param amount (Integer): Price of the product in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    """
    label: str
    amount: int


@dataclass
class InputInvoiceMessageContent:
    """
    Represents the content of an invoice message to be sent as the result of an inline query.

    Keyword arguments:

    :param title (String): Product name, 1-32 characters
    :param description (String): Product description, 1-255 characters
    :param payload (String): Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.
    :param provider_token (String): Payment provider token, obtained via Botfather
    :param currency (String): Three-letter ISO 4217 currency code, see more on currencies
    :param prices (Array of LabeledPrice): Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)
    :param max_tip_amount (Integer): Optional. The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0
    :param suggested_tip_amounts (Array of Integer): Optional. A JSON-serialized array of suggested amounts of tip in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.
    :param provider_data (String): Optional. A JSON-serialized object for data about the invoice, which will be shared with the payment provider. A detailed description of the required fields should be provided by the payment provider.
    :param photo_url (String): Optional. URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.
    :param photo_size (Integer): Optional. Photo size
    :param photo_width (Integer): Optional. Photo width
    :param photo_height (Integer): Optional. Photo height
    :param need_name (Boolean): Optional. Pass True, if you require the user's full name to complete the order
    :param need_phone_number (Boolean): Optional. Pass True, if you require the user's phone number to complete the order
    :param need_email (Boolean): Optional. Pass True, if you require the user's email address to complete the order
    :param need_shipping_address (Boolean): Optional. Pass True, if you require the user's shipping address to complete the order
    :param send_phone_number_to_provider (Boolean): Optional. Pass True, if user's phone number should be sent to provider
    :param send_email_to_provider (Boolean): Optional. Pass True, if user's email address should be sent to provider
    :param is_flexible (Boolean): Optional. Pass True, if the final price depends on the shipping method
    """
    title: str
    description: str
    payload: str
    provider_token: str
    currency: str
    prices: List[LabeledPrice]
    max_tip_amount: int
    suggested_tip_amounts: List[int]
    provider_data: str
    photo_url: str
    photo_size: int
    photo_width: int
    photo_height: int
    need_name: bool
    need_phone_number: bool
    need_email: bool
    need_shipping_address: bool
    send_phone_number_to_provider: bool
    send_email_to_provider: bool
    is_flexible: bool


@dataclass
class ChosenInlineResult:
    """
    Represents a result of an inline query that was chosen by the user and sent to their chat partner.

    Keyword arguments:

    :param result_id (String): The unique identifier for the result that was chosen
    :param _from (User): The user that chose the result
    :param location (Location): Optional. Sender location, only for bots that require user location
    :param inline_message_id (String): Optional. Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. Will be also received in callback queries and can be used to edit the message.
    :param query (String): The query that was used to obtain the result
    """
    result_id: str
    _from: User
    location: Location
    inline_message_id: str
    query: str


@dataclass
class Invoice:
    """
    This object contains basic information about an invoice.

    Keyword arguments:

    :param title (String): Product name
    :param description (String): Product description
    :param start_parameter (String): Unique bot deep-linking parameter that can be used to generate this invoice
    :param currency (String): Three-letter ISO 4217 currency code
    :param total_amount (Integer): Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    """
    title: str
    description: str
    start_parameter: str
    currency: str
    total_amount: int


@dataclass
class ShippingAddress:
    """
    This object represents a shipping address.

    Keyword arguments:

    :param country_code (String): ISO 3166-1 alpha-2 country code
    :param state (String): State, if applicable
    :param city (String): City
    :param street_line1 (String): First line for the address
    :param street_line2 (String): Second line for the address
    :param post_code (String): Address post code
    """
    country_code: str
    state: str
    city: str
    street_line1: str
    street_line2: str
    post_code: str


@dataclass
class OrderInfo:
    """
    This object represents information about an order.

    Keyword arguments:

    :param name (String): Optional. User name
    :param phone_number (String): Optional. User's phone number
    :param email (String): Optional. User email
    :param shipping_address (ShippingAddress): Optional. User shipping address
    """
    name: str
    phone_number: str
    email: str
    shipping_address: ShippingAddress


@dataclass
class ShippingOption:
    """
    This object represents one shipping option.

    Keyword arguments:

    :param id (String): Shipping option identifier
    :param title (String): Option title
    :param prices (Array of LabeledPrice): List of price portions
    """
    id: str
    title: str
    prices: List[LabeledPrice]


@dataclass
class SuccessfulPayment:
    """
    This object contains basic information about a successful payment.

    Keyword arguments:

    :param currency (String): Three-letter ISO 4217 currency code
    :param total_amount (Integer): Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    :param invoice_payload (String): Bot specified invoice payload
    :param shipping_option_id (String): Optional. Identifier of the shipping option chosen by the user
    :param order_info (OrderInfo): Optional. Order info provided by the user
    :param telegram_payment_charge_id (String): Telegram payment identifier
    :param provider_payment_charge_id (String): Provider payment identifier
    """
    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: str
    order_info: OrderInfo
    telegram_payment_charge_id: str
    provider_payment_charge_id: str


@dataclass
class ShippingQuery:
    """
    This object contains information about an incoming shipping query.

    Keyword arguments:

    :param id (String): Unique query identifier
    :param _from (User): User who sent the query
    :param invoice_payload (String): Bot specified invoice payload
    :param shipping_address (ShippingAddress): User specified shipping address
    """
    id: str
    _from: User
    invoice_payload: str
    shipping_address: ShippingAddress


@dataclass
class PreCheckoutQuery:
    """
    This object contains information about an incoming pre-checkout query.

    Keyword arguments:

    :param id (String): Unique query identifier
    :param _from (User): User who sent the query
    :param currency (String): Three-letter ISO 4217 currency code
    :param total_amount (Integer): Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    :param invoice_payload (String): Bot specified invoice payload
    :param shipping_option_id (String): Optional. Identifier of the shipping option chosen by the user
    :param order_info (OrderInfo): Optional. Order info provided by the user
    """
    id: str
    _from: User
    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: str
    order_info: OrderInfo


@dataclass
class PassportFile:
    """
    This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB.

    Keyword arguments:

    :param file_id (String): Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id (String): Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :param file_size (Integer): File size
    :param file_date (Integer): Unix time when the file was uploaded
    """
    file_id: str
    file_unique_id: str
    file_size: int
    file_date: int


@dataclass
class EncryptedPassportElement:
    """
    Contains information about documents or other Telegram Passport elements shared with the bot by the user.

    Keyword arguments:

    :param type (String): Element type. One of \xe2\x80\x9cpersonal_details\xe2\x80\x9d, \xe2\x80\x9cpassport\xe2\x80\x9d, \xe2\x80\x9cdriver_license\xe2\x80\x9d, \xe2\x80\x9cidentity_card\xe2\x80\x9d, \xe2\x80\x9cinternal_passport\xe2\x80\x9d, \xe2\x80\x9caddress\xe2\x80\x9d, \xe2\x80\x9cutility_bill\xe2\x80\x9d, \xe2\x80\x9cbank_statement\xe2\x80\x9d, \xe2\x80\x9crental_agreement\xe2\x80\x9d, \xe2\x80\x9cpassport_registration\xe2\x80\x9d, \xe2\x80\x9ctemporary_registration\xe2\x80\x9d, \xe2\x80\x9cphone_number\xe2\x80\x9d, \xe2\x80\x9cemail\xe2\x80\x9d.
    :param data (String): Optional. Base64-encoded encrypted Telegram Passport element data provided by the user, available for \xe2\x80\x9cpersonal_details\xe2\x80\x9d, \xe2\x80\x9cpassport\xe2\x80\x9d, \xe2\x80\x9cdriver_license\xe2\x80\x9d, \xe2\x80\x9cidentity_card\xe2\x80\x9d, \xe2\x80\x9cinternal_passport\xe2\x80\x9d and \xe2\x80\x9caddress\xe2\x80\x9d types. Can be decrypted and verified using the accompanying EncryptedCredentials.
    :param phone_number (String): Optional. User's verified phone number, available only for \xe2\x80\x9cphone_number\xe2\x80\x9d type
    :param email (String): Optional. User's verified email address, available only for \xe2\x80\x9cemail\xe2\x80\x9d type
    :param files (Array of PassportFile): Optional. Array of encrypted files with documents provided by the user, available for \xe2\x80\x9cutility_bill\xe2\x80\x9d, \xe2\x80\x9cbank_statement\xe2\x80\x9d, \xe2\x80\x9crental_agreement\xe2\x80\x9d, \xe2\x80\x9cpassport_registration\xe2\x80\x9d and \xe2\x80\x9ctemporary_registration\xe2\x80\x9d types. Files can be decrypted and verified using the accompanying EncryptedCredentials.
    :param front_side (PassportFile): Optional. Encrypted file with the front side of the document, provided by the user. Available for \xe2\x80\x9cpassport\xe2\x80\x9d, \xe2\x80\x9cdriver_license\xe2\x80\x9d, \xe2\x80\x9cidentity_card\xe2\x80\x9d and \xe2\x80\x9cinternal_passport\xe2\x80\x9d. The file can be decrypted and verified using the accompanying EncryptedCredentials.
    :param reverse_side (PassportFile): Optional. Encrypted file with the reverse side of the document, provided by the user. Available for \xe2\x80\x9cdriver_license\xe2\x80\x9d and \xe2\x80\x9cidentity_card\xe2\x80\x9d. The file can be decrypted and verified using the accompanying EncryptedCredentials.
    :param selfie (PassportFile): Optional. Encrypted file with the selfie of the user holding a document, provided by the user; available for \xe2\x80\x9cpassport\xe2\x80\x9d, \xe2\x80\x9cdriver_license\xe2\x80\x9d, \xe2\x80\x9cidentity_card\xe2\x80\x9d and \xe2\x80\x9cinternal_passport\xe2\x80\x9d. The file can be decrypted and verified using the accompanying EncryptedCredentials.
    :param translation (Array of PassportFile): Optional. Array of encrypted files with translated versions of documents provided by the user. Available if requested for \xe2\x80\x9cpassport\xe2\x80\x9d, \xe2\x80\x9cdriver_license\xe2\x80\x9d, \xe2\x80\x9cidentity_card\xe2\x80\x9d, \xe2\x80\x9cinternal_passport\xe2\x80\x9d, \xe2\x80\x9cutility_bill\xe2\x80\x9d, \xe2\x80\x9cbank_statement\xe2\x80\x9d, \xe2\x80\x9crental_agreement\xe2\x80\x9d, \xe2\x80\x9cpassport_registration\xe2\x80\x9d and \xe2\x80\x9ctemporary_registration\xe2\x80\x9d types. Files can be decrypted and verified using the accompanying EncryptedCredentials.
    :param hash (String): Base64-encoded element hash for using in PassportElementErrorUnspecified
    """
    type: str
    data: str
    phone_number: str
    email: str
    files: List[PassportFile]
    front_side: Union[PassportFile]
    reverse_side: Union[PassportFile]
    selfie: Union[PassportFile]
    translation: List[PassportFile]
    hash: str


@dataclass
class EncryptedCredentials:
    """
    Contains data required for decrypting and authenticating EncryptedPassportElement. See the Telegram Passport Documentation for a complete description of the data decryption and authentication processes.

    Keyword arguments:

    :param data (String): Base64-encoded encrypted JSON-serialized data with unique user's payload, data hashes and secrets required for EncryptedPassportElement decryption and authentication
    :param hash (String): Base64-encoded data hash for data authentication
    :param secret (String): Base64-encoded secret, encrypted with the bot's public RSA key, required for data decryption
    """
    data: str
    hash: str
    secret: str


@dataclass
class PassportElementErrorDataField:
    """
    Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.

    Keyword arguments:

    :param source (String): Error source, must be data
    :param type (String): The section of the user's Telegram Passport which has the error, one of \xe2\x80\x9cpersonal_details\xe2\x80\x9d, \xe2\x80\x9cpassport\xe2\x80\x9d, \xe2\x80\x9cdriver_license\xe2\x80\x9d, \xe2\x80\x9cidentity_card\xe2\x80\x9d, \xe2\x80\x9cinternal_passport\xe2\x80\x9d, \xe2\x80\x9caddress\xe2\x80\x9d
    :param field_name (String): Name of the data field which has the error
    :param data_hash (String): Base64-encoded data hash
    :param message (String): Error message
    """
    source: str
    type: str
    field_name: str
    data_hash: str
    message: str


@dataclass
class PassportElementErrorFrontSide:
    """
    Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes.

    Keyword arguments:

    :param source (String): Error source, must be front_side
    :param type (String): The section of the user's Telegram Passport which has the issue, one of \xe2\x80\x9cpassport\xe2\x80\x9d, \xe2\x80\x9cdriver_license\xe2\x80\x9d, \xe2\x80\x9cidentity_card\xe2\x80\x9d, \xe2\x80\x9cinternal_passport\xe2\x80\x9d
    :param file_hash (String): Base64-encoded hash of the file with the front side of the document
    :param message (String): Error message
    """
    source: str
    type: str
    file_hash: str
    message: str


@dataclass
class PassportElementErrorReverseSide:
    """
    Represents an issue with the reverse side of a document. The error is considered resolved when the file with reverse side of the document changes.

    Keyword arguments:

    :param source (String): Error source, must be reverse_side
    :param type (String): The section of the user's Telegram Passport which has the issue, one of \xe2\x80\x9cdriver_license\xe2\x80\x9d, \xe2\x80\x9cidentity_card\xe2\x80\x9d
    :param file_hash (String): Base64-encoded hash of the file with the reverse side of the document
    :param message (String): Error message
    """
    source: str
    type: str
    file_hash: str
    message: str


@dataclass
class PassportElementErrorSelfie:
    """
    Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.

    Keyword arguments:

    :param source (String): Error source, must be selfie
    :param type (String): The section of the user's Telegram Passport which has the issue, one of \xe2\x80\x9cpassport\xe2\x80\x9d, \xe2\x80\x9cdriver_license\xe2\x80\x9d, \xe2\x80\x9cidentity_card\xe2\x80\x9d, \xe2\x80\x9cinternal_passport\xe2\x80\x9d
    :param file_hash (String): Base64-encoded hash of the file with the selfie
    :param message (String): Error message
    """
    source: str
    type: str
    file_hash: str
    message: str


@dataclass
class PassportElementErrorFile:
    """
    Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes.

    Keyword arguments:

    :param source (String): Error source, must be file
    :param type (String): The section of the user's Telegram Passport which has the issue, one of \xe2\x80\x9cutility_bill\xe2\x80\x9d, \xe2\x80\x9cbank_statement\xe2\x80\x9d, \xe2\x80\x9crental_agreement\xe2\x80\x9d, \xe2\x80\x9cpassport_registration\xe2\x80\x9d, \xe2\x80\x9ctemporary_registration\xe2\x80\x9d
    :param file_hash (String): Base64-encoded file hash
    :param message (String): Error message
    """
    source: str
    type: str
    file_hash: str
    message: str


@dataclass
class PassportElementErrorFiles:
    """
    Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.

    Keyword arguments:

    :param source (String): Error source, must be files
    :param type (String): The section of the user's Telegram Passport which has the issue, one of \xe2\x80\x9cutility_bill\xe2\x80\x9d, \xe2\x80\x9cbank_statement\xe2\x80\x9d, \xe2\x80\x9crental_agreement\xe2\x80\x9d, \xe2\x80\x9cpassport_registration\xe2\x80\x9d, \xe2\x80\x9ctemporary_registration\xe2\x80\x9d
    :param file_hashes (Array of String): List of base64-encoded file hashes
    :param message (String): Error message
    """
    source: str
    type: str
    file_hashes: List[str]
    message: str


@dataclass
class PassportElementErrorTranslationFile:
    """
    Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes.

    Keyword arguments:

    :param source (String): Error source, must be translation_file
    :param type (String): Type of element of the user's Telegram Passport which has the issue, one of \xe2\x80\x9cpassport\xe2\x80\x9d, \xe2\x80\x9cdriver_license\xe2\x80\x9d, \xe2\x80\x9cidentity_card\xe2\x80\x9d, \xe2\x80\x9cinternal_passport\xe2\x80\x9d, \xe2\x80\x9cutility_bill\xe2\x80\x9d, \xe2\x80\x9cbank_statement\xe2\x80\x9d, \xe2\x80\x9crental_agreement\xe2\x80\x9d, \xe2\x80\x9cpassport_registration\xe2\x80\x9d, \xe2\x80\x9ctemporary_registration\xe2\x80\x9d
    :param file_hash (String): Base64-encoded file hash
    :param message (String): Error message
    """
    source: str
    type: str
    file_hash: str
    message: str


@dataclass
class PassportElementErrorTranslationFiles:
    """
    Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change.

    Keyword arguments:

    :param source (String): Error source, must be translation_files
    :param type (String): Type of element of the user's Telegram Passport which has the issue, one of \xe2\x80\x9cpassport\xe2\x80\x9d, \xe2\x80\x9cdriver_license\xe2\x80\x9d, \xe2\x80\x9cidentity_card\xe2\x80\x9d, \xe2\x80\x9cinternal_passport\xe2\x80\x9d, \xe2\x80\x9cutility_bill\xe2\x80\x9d, \xe2\x80\x9cbank_statement\xe2\x80\x9d, \xe2\x80\x9crental_agreement\xe2\x80\x9d, \xe2\x80\x9cpassport_registration\xe2\x80\x9d, \xe2\x80\x9ctemporary_registration\xe2\x80\x9d
    :param file_hashes (Array of String): List of base64-encoded file hashes
    :param message (String): Error message
    """
    source: str
    type: str
    file_hashes: List[str]
    message: str


@dataclass
class PassportElementErrorUnspecified:
    """
    Represents an issue in an unspecified place. The error is considered resolved when new data is added.

    Keyword arguments:

    :param source (String): Error source, must be unspecified
    :param type (String): Type of element of the user's Telegram Passport which has the issue
    :param element_hash (String): Base64-encoded element hash
    :param message (String): Error message
    """
    source: str
    type: str
    element_hash: str
    message: str


@dataclass
class PassportData:
    """
    Contains information about Telegram Passport data shared with the bot by the user.

    Keyword arguments:

    :param data (Array of EncryptedPassportElement): Array with information about documents and other Telegram Passport elements that was shared with the bot
    :param credentials (EncryptedCredentials): Encrypted credentials required to decrypt the data
    """
    data: List[EncryptedPassportElement]
    credentials: EncryptedCredentials


@dataclass
class Game:
    """
    This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.

    Keyword arguments:

    :param title (String): Title of the game
    :param description (String): Description of the game
    :param photo (Array of PhotoSize): Photo that will be displayed in the game message in chats.
    :param text (String): Optional. Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls setGameScore, or manually edited using editMessageText. 0-4096 characters.
    :param text_entities (Array of MessageEntity): Optional. Special entities that appear in text, such as usernames, URLs, bot commands, etc.
    :param animation (Animation): Optional. Animation that will be displayed in the game message in chats. Upload via BotFather
    """
    title: str
    description: str
    photo: List[PhotoSize]
    text: str
    text_entities: List[MessageEntity]
    animation: Animation


@dataclass
class GameHighScore:
    """
    This object represents one row of the high scores table for a game.

    Keyword arguments:

    :param position (Integer): Position in high score table for the game
    :param user (User): User
    :param score (Integer): Score
    """
    position: int
    user: User
    score: int


@dataclass
class Chat:
    """
    This object represents a chat.

    Keyword arguments:

    :param id (Integer): Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    :param type (String): Type of chat, can be either \xe2\x80\x9cprivate\xe2\x80\x9d, \xe2\x80\x9cgroup\xe2\x80\x9d, \xe2\x80\x9csupergroup\xe2\x80\x9d or \xe2\x80\x9cchannel\xe2\x80\x9d
    :param title (String): Optional. Title, for supergroups, channels and group chats
    :param username (String): Optional. Username, for private chats, supergroups and channels if available
    :param first_name (String): Optional. First name of the other party in a private chat
    :param last_name (String): Optional. Last name of the other party in a private chat
    :param photo (ChatPhoto): Optional. Chat photo. Returned only in getChat.
    :param bio (String): Optional. Bio of the other party in a private chat. Returned only in getChat.
    :param description (String): Optional. Description, for groups, supergroups and channel chats. Returned only in getChat.
    :param invite_link (String): Optional. Primary invite link, for groups, supergroups and channel chats. Returned only in getChat.
    :param pinned_message (Message): Optional. The most recent pinned message (by sending date). Returned only in getChat.
    :param permissions (ChatPermissions): Optional. Default chat member permissions, for groups and supergroups. Returned only in getChat.
    :param slow_mode_delay (Integer): Optional. For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user. Returned only in getChat.
    :param message_auto_delete_time (Integer): Optional. The time after which all messages sent to the chat will be automatically deleted; in seconds. Returned only in getChat.
    :param sticker_set_name (String): Optional. For supergroups, name of group sticker set. Returned only in getChat.
    :param can_set_sticker_set (Boolean): Optional. True, if the bot can change the group sticker set. Returned only in getChat.
    :param linked_chat_id (Integer): Optional. Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier. Returned only in getChat.
    :param location (ChatLocation): Optional. For supergroups, the location to which the supergroup is connected. Returned only in getChat.
    """
    id: int
    type: str
    title: str
    username: str
    first_name: str
    last_name: str
    photo: ChatPhoto
    bio: str
    description: str
    invite_link: str
    pinned_message: "Message"
    permissions: ChatPermissions
    slow_mode_delay: int
    message_auto_delete_time: int
    sticker_set_name: str
    can_set_sticker_set: bool
    linked_chat_id: int
    location: ChatLocation


@dataclass
class ChatMemberUpdated:
    """
    This object represents changes in the status of a chat member.

    Keyword arguments:

    :param chat (Chat): Chat the user belongs to
    :param _from (User): Performer of the action, which resulted in the change
    :param date (Integer): Date the change was done in Unix time
    :param old_chat_member (ChatMember): Previous information about the chat member
    :param new_chat_member (ChatMember): New information about the chat member
    :param invite_link (ChatInviteLink): Optional. Chat invite link, which was used by the user to join the chat; for joining by invite link events only.
    """
    chat: Chat
    _from: User
    date: int
    old_chat_member: ChatMember
    new_chat_member: ChatMember
    invite_link: ChatInviteLink


@dataclass
class Message:
    """
    This object represents a message.

    Keyword arguments:

    :param message_id (Integer): Unique message identifier inside this chat
    :param _from (User): Optional. Sender, empty for messages sent to channels
    :param sender_chat (Chat): Optional. Sender of the message, sent on behalf of a chat. The channel itself for channel messages. The supergroup itself for messages from anonymous group administrators. The linked channel for messages automatically forwarded to the discussion group
    :param date (Integer): Date the message was sent in Unix time
    :param chat (Chat): Conversation the message belongs to
    :param forward_from (User): Optional. For forwarded messages, sender of the original message
    :param forward_from_chat (Chat): Optional. For messages forwarded from channels or from anonymous administrators, information about the original sender chat
    :param forward_from_message_id (Integer): Optional. For messages forwarded from channels, identifier of the original message in the channel
    :param forward_signature (String): Optional. For messages forwarded from channels, signature of the post author if present
    :param forward_sender_name (String): Optional. Sender's name for messages forwarded from users who disallow adding a link to their account in forwarded messages
    :param forward_date (Integer): Optional. For forwarded messages, date the original message was sent in Unix time
    :param reply_to_message (Message): Optional. For replies, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.
    :param via_bot (User): Optional. Bot through which the message was sent
    :param edit_date (Integer): Optional. Date the message was last edited in Unix time
    :param media_group_id (String): Optional. The unique identifier of a media message group this message belongs to
    :param author_signature (String): Optional. Signature of the post author for messages in channels, or the custom title of an anonymous group administrator
    :param text (String): Optional. For text messages, the actual UTF-8 text of the message, 0-4096 characters
    :param entities (Array of MessageEntity): Optional. For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text
    :param animation (Animation): Optional. Message is an animation, information about the animation. For backward compatibility, when this field is set, the document field will also be set
    :param audio (Audio): Optional. Message is an audio file, information about the file
    :param document (Document): Optional. Message is a general file, information about the file
    :param photo (Array of PhotoSize): Optional. Message is a photo, available sizes of the photo
    :param sticker (Sticker): Optional. Message is a sticker, information about the sticker
    :param video (Video): Optional. Message is a video, information about the video
    :param video_note (VideoNote): Optional. Message is a video note, information about the video message
    :param voice (Voice): Optional. Message is a voice message, information about the file
    :param caption (String): Optional. Caption for the animation, audio, document, photo, video or voice, 0-1024 characters
    :param caption_entities (Array of MessageEntity): Optional. For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption
    :param contact (Contact): Optional. Message is a shared contact, information about the contact
    :param dice (Dice): Optional. Message is a dice with random value
    :param game (Game): Optional. Message is a game, information about the game. More about games \xc2\xbb
    :param poll (Poll): Optional. Message is a native poll, information about the poll
    :param venue (Venue): Optional. Message is a venue, information about the venue. For backward compatibility, when this field is set, the location field will also be set
    :param location (Location): Optional. Message is a shared location, information about the location
    :param new_chat_members (Array of User): Optional. New members that were added to the group or supergroup and information about them (the bot itself may be one of these members)
    :param left_chat_member (User): Optional. A member was removed from the group, information about them (this member may be the bot itself)
    :param new_chat_title (String): Optional. A chat title was changed to this value
    :param new_chat_photo (Array of PhotoSize): Optional. A chat photo was change to this value
    :param delete_chat_photo (True): Optional. Service message: the chat photo was deleted
    :param group_chat_created (True): Optional. Service message: the group has been created
    :param supergroup_chat_created (True): Optional. Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup.
    :param channel_chat_created (True): Optional. Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel.
    :param message_auto_delete_timer_changed (MessageAutoDeleteTimerChanged): Optional. Service message: auto-delete timer settings changed in the chat
    :param migrate_to_chat_id (Integer): Optional. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    :param migrate_from_chat_id (Integer): Optional. The supergroup has been migrated from a group with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    :param pinned_message (Message): Optional. Specified message was pinned. Note that the Message object in this field will not contain further reply_to_message fields even if it is itself a reply.
    :param invoice (Invoice): Optional. Message is an invoice for a payment, information about the invoice. More about payments \xc2\xbb
    :param successful_payment (SuccessfulPayment): Optional. Message is a service message about a successful payment, information about the payment. More about payments \xc2\xbb
    :param connected_website (String): Optional. The domain name of the website on which the user has logged in. More about Telegram Login \xc2\xbb
    :param passport_data (PassportData): Optional. Telegram Passport data
    :param proximity_alert_triggered (ProximityAlertTriggered): Optional. Service message. A user in the chat triggered another user's proximity alert while sharing Live Location.
    :param voice_chat_scheduled (VoiceChatScheduled): Optional. Service message: voice chat scheduled
    :param voice_chat_started (VoiceChatStarted): Optional. Service message: voice chat started
    :param voice_chat_ended (VoiceChatEnded): Optional. Service message: voice chat ended
    :param voice_chat_participants_invited (VoiceChatParticipantsInvited): Optional. Service message: new participants invited to a voice chat
    :param reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons.
    """
    message_id: int
    _from: User
    sender_chat: Chat
    date: int
    chat: Chat
    forward_from: User
    forward_from_chat: Chat
    forward_from_message_id: int
    forward_signature: str
    forward_sender_name: str
    forward_date: int
    reply_to_message: "Message"
    via_bot: User
    edit_date: int
    media_group_id: str
    author_signature: str
    text: str
    entities: List[MessageEntity]
    animation: Animation
    audio: Audio
    document: Document
    photo: List[PhotoSize]
    sticker: Sticker
    video: Video
    video_note: VideoNote
    voice: Voice
    caption: str
    caption_entities: List[MessageEntity]
    contact: Contact
    dice: Dice
    game: Game
    poll: Poll
    venue: Venue
    location: Location
    new_chat_members: List[User]
    left_chat_member: User
    new_chat_title: str
    new_chat_photo: List[PhotoSize]
    delete_chat_photo: True
    group_chat_created: True
    supergroup_chat_created: True
    channel_chat_created: True
    message_auto_delete_timer_changed: MessageAutoDeleteTimerChanged
    migrate_to_chat_id: int
    migrate_from_chat_id: int
    pinned_message: "Message"
    invoice: Invoice
    successful_payment: SuccessfulPayment
    connected_website: str
    passport_data: Union[PassportData]
    proximity_alert_triggered: ProximityAlertTriggered
    voice_chat_scheduled: VoiceChatScheduled
    voice_chat_started: VoiceChatStarted
    voice_chat_ended: VoiceChatEnded
    voice_chat_participants_invited: VoiceChatParticipantsInvited
    reply_markup: InlineKeyboardMarkup




