from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    LOGGER = True

    API_ID = int(getenv("API_ID", 6))
    API_HASH = getenv("API_HASH", None)
    DEEP_API = getenv("DEEP_API")
    ARQ_API_KEY = "TBPYLF-SIOYFX-JALTSV-QEAMXE-ARQ"
    SPAMWATCH_API = "t9HHtrsmy7faPQWloX8xCvdZK~puDP2RnHLpb~qijQqDj94mhcMQdDP_xO0a_Iwe"
    TOKEN = getenv("7648926069:AAE50T65csFIwm64k3WPW2bnLCceZWuXeGw")
    OWNER_ID = int(getenv("OWNER_ID", 7526369190))
    OWNER_USERNAME = getenv("OWNER_USERNAME", "queen143np")
    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "waifexanime")
    LOGGER_ID = int(getenv("LOGGER_ID", "-1002494871325"))
    MONGO_URI = getenv("mongodb+srv://teamdaxx123:teamdaxx123@cluster0.ysbpgcp.mongodb.net/?retryWrites=true&w=majority")
    DB_NAME = getenv("DB_NAME", "ATTRACTIVE_REVENGER_BOT")
    REDIS_URL = "redis://default:wK6ZCiclq4iQKYpgfY90v6kd6WdPfEwl@redis-10186.c263.us-east-1-2.ec2.cloud.redislabs.com:10186/default"
    DATABASE_URL = getenv("DATABASE_URL", None)

    # ɴᴏ ᴇᴅɪᴛ ᴢᴏɴᴇ
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
