import os


class Config(object):
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    TELEGRAM_API = os.environ["TELEGRAM_API"]
    OWNER = os.environ.get("OWNER")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Merge-Bot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "Sujan_BotZ")
    PASSWORD = os.environ.get("PASSWORD")
    DATABASE_URL = os.environ.get("DATABASE_URL")
    LOGCHANNEL = os.environ.get("LOGCHANNEL")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BAE9PdcARk15elSrxYFC5511RdbqfoABPs48OePG9pbrXLepgewGlV7HKiqN1JB5SakrAx1U9IQch4wNuujjf_X2eVXvStTJm9fh7RBAF4HaPDESQ_k3QYAwMR7gbrvWuwFKIbEwHLSjOVlABTc-T70WPe57MVRUjL2JQPYkuF1eAZAK6lTyS8jBx_NoXXz77pXYCVPF9vkcXnSnxN2sccSGAqFANQKWyYzL8NKsW7N35m-7BQsTRdVH5hWFJjxUVu9vlQbp-qgPaeJL7hGcdCh77InW-ZK4Ymvm8gtYUuIIkhwcwR56F_68jZJdwARn_q0QyrgUP9AYR3BZkuTRkmjmReCMuQAAAAGB6XFoAA")
    IS_PREMIUM = True
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
    UPSTREAM_REPO = "https://github.com/SujanCh549/4Gb-VIDEO-MERGE-BOT"
    UPSTREAM_BRANCH = "master"

    START_TEXT = """
Hɪ 👋 I Aᴍ A Fɪʟᴇ/Vɪᴅᴇᴏ Mᴇʀɢᴇ Bᴏᴛ. I Cᴀɴ Mᴇʀɢᴇ Tᴇʟᴇɢʀᴀᴍ Fɪʟᴇs!, Aɴᴅ Uᴘʟᴏᴀᴅ Iᴛ Tᴏ Tᴇʟᴇɢʀᴀᴍ.

"""
