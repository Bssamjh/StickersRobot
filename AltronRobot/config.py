class Config(object):
    LOGGER = True

    API_ID = 
    API_HASH = ""
    TOKEN = ""
    OWNER_ID = 
    OWNER_USERNAME = ""
    SUPPORT_CHAT = ""
    JOIN_LOGGER = ()
    EVENT_LOGS = ()

    SQLALCHEMY_DATABASE_URI = ""
    MONGO_DB_URI = ""
    LOAD = []
    NO_LOAD = ["rss"]
    INFOPIC = True

    # OPTIONAL
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = 
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BL_CHATS = []
    SPAMMERS = None
    START_IMG = ""
    ARQ_API_KEY = "LJMETG-DPHBCX-DGHJCD-TMFIGB-ARQ"
    ARQ_API_URL = "https://arq.hamker.in"
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
