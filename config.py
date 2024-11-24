from os import environ
from pyrogram import Client
from pyrogram.storage import MemoryStorage  # Import MemoryStorage

class Config:
    API_ID = environ.get("API_ID", "")
    API_HASH = environ.get("API_HASH", "")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "BQFna_QAv59YZnkXZtxBk3cJ18uOz_da3Iw3S8X2Yxu1wQ_Dmk0cd7DTzj86EnG6cKYsWDjB2HkUzCgAe1Fqzl8BFr_DIZgcgh1IxrqPg1wJt1KImhgilf64NC49WL6FdAtscNZH3LukSurS6q4ke4zuOEybvC7cFrxsPJ0y4qBuegmYCtsvOSpvkIEbmFWoUjx9TB0h22fXzULvE5WvEUmwJyTREql3WmLT4pMNYQ91NcyGvoUjh1DgcXs4b2Ws2vRolNXPup6Jm7FNIpOSBVm-SSet57O938cdH6S5QCNKRWB4txztDesmEDZkpxI0MuOtXVoQmSDgXuqUY924lABzX9MudAAAAAHFfn7mAQ") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://tejaschavan1110:sYKaW4zHLgbxAMQY@cluster0.bvhjz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7210955390').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []

# Initialize the bot client using MemoryStorage
app = Client(
    "bot_session",
    session_string=Config.BOT_SESSION,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    storage=MemoryStorage()  # Use MemoryStorage for in-memory session
)

@app.on_message()
def my_handler(client, message):
    message.reply_text("Hello, I received your message!")

if __name__ == "__main__":
    app.run()
