class script(object):
    START_TXT = """đ·đŽđ»đ»đŸ {},
đŒđ đœđ°đŒđŽ đžđ <a href=https://t.me/{}>{}</a>, đž đČđ°đœ đżđđŸđđžđłđŽ đ°đ»đ» đœđŽđ đŒđŸđđžđŽđ, đčđđđ đ°đłđł đŒđŽ đđŸ đđŸđđ đ¶đđŸđđż đ°đœđł đŽđœđčđŸđ """
    HELP_TXT = """đ·đŽđ {}
đ·đŽđđŽ đžđ đđ·đŽ đ·đŽđ»đż đ”đŸđ đŒđ đČđŸđŒđŒđ°đœđłđ."""
    ABOUT_TXT = """đđđąđšđ§ đ đŠđ đđ đđđđ
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
ââââââ°  â±âââ±âÛȘÛȘ
ââ­ââââââââââââââââŁ 
ââŁâȘŒ đđČđ«đ»đȘđ»đ»đ - đżđđđŸđ¶đđ°đŒ
ââŁâȘŒ đđȘđ·đ°đŸđȘđ°đź - đżđđđ·đŸđœ đč
ââŁâȘŒ đđȘđœđȘ đđȘđŒđź - đŒđŸđœđ¶đŸ đłđ±
ââŁâȘŒ đđžđœ đŒđźđ»đżđźđ» -  OWN VPS
ââŁâȘŒ đđŸđČđ”đ­ đąđœđȘđœđŸđŒ - v1.0.1 [ đ±đŽđđ° ]
ââ°ââââââââââââââââŁ
âââââââââââââââââââââ±â"""
    ADMINS_TXT = """đđđ
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
ââââââ°  â±âââ±âÛȘÛȘ
ââ­ââââââââââââââââŁ 
ââŁâȘŒ đŒđ đœđ°đŒđŽ - TG Downloader Bot
ââŁâȘŒ đđđżđżđŸđđ đŒđ đČđ·đ°đœđœđŽđ»
ââŁ      <a href=https://t.me/Hollywood_in_HindiHD>Hollywood in HindiHD</a>
ââ°ââââââââââââââââŁ
âââââââââââââââââââââ±â"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and TG Downloader Bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. TG Downloader should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
âą /filter - <code>add a filter in chat</code>
âą /filters - <code>list all the filters of a chat</code>
âą /del - <code>delete a specific filter in chat</code>
âą /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """<b>Help: Buttons</b>

- <b>TG Downloader Supports both url and alert inline buttons.</b>

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. TG Downloader supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Hollywood in HindiHD)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
âą /connect  - <code>connect a particular chat to your PM</code>
âą /disconnect  - <code>disconnect from a chat</code>
âą /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of TG Downloader Bot

<b>Commands and Usage:</b>
âą /id - <code>get id of a specifed user.</code>
âą /info  - <code>get information about a user.</code>
âą /imdb  - <code>get the film information from IMDb source.</code>
âą /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
âą /logs - <code>to get the rescent errors</code>
âą /stats - <code>to get status of files in db.</code>
âą /delete - <code>to delete a specific file from db.</code>
âą /users - <code>to get list of my users and ids.</code>
âą /chats - <code>to get list of the my chats and ids </code>
âą /leave  - <code>to leave from a chat.</code>
âą /disable  -  <code>do disable a chat.</code>
âą /ban  - <code>to ban a user.</code>
âą /unban  - <code>to unban a user.</code>
âą /channel - <code>to get list of total connected channels</code>
âą /broadcast - <code>to broadcast a message to all users</code>
âą /donate - <code>to donate any gifts for my owner</code>"""
    STATUS_TXT = """ââââââ° ê«êȘđłđČ â±âââ±âÛȘÛȘ
ââ­ââââââââââââââââŁ 
ââŁâȘŒ đđŸđđ°đ» đ”đžđ»đŽđ: <code>{}</code>
ââŁâȘŒ đđŸđđ°đ» đđđŽđđ: <code>{}</code>
ââŁâȘŒ đđŸđđ°đ» đČđ·đ°đđ: <code>{}</code>
ââŁâȘŒ đđđŽđł đđđŸđđ°đ¶đŽ: <code>{}</code> đŒđđ±
ââŁâȘŒ đ”đđŽđŽ đđđŸđđ°đ¶đŽ: <code>{}</code> đŒđđ±
ââ°ââââââââââââââââŁ
âââââââââââââââââââââ±â"""
    DONATE_TXT = """<Hey {}
[Here is the Donation Link](https://t.me/Redxpromotionrobot) â€"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
