import os


class Config():
    # Bu dəyərləri my.telegram.org saytından əldə edin
    #>>> https://my.telegram.org
    API_ID = int(os.environ.get("API_ID","16157584"))
    API_HASH = os.environ.get("API_HASH","8ce53801c1b49cd4d2fa108eb151b255")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","533")
    BOT_USERNAME = os.environ.get("BOT_USERNAME","dejavy")
    BOT_NAME = os.environ.get("BOT_NAME","jhkoijl")
    BOT_ID = int(os.environ.get("BOT_ID","234567890-"))
    SUDO_USERS = os.environ.get("SUDO_USERS","rseyutiydou").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT","ioj")
    OWNER_ID = int(os.environ.get("OWNER_ID","43567890"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME","uijio;kl,")
