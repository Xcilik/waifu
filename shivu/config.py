class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6649432492"
    sudo_users = "6649432492"
    GROUP_ID = -100212448722
    TOKEN = "6713160483:AAGgrbbljK05FwaOxwJ0pTs4o1kcZNL0024"
    mongo_url = "mongodb+srv://memek:memek@cluster0.xktxnyr.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "gcanimecommunity"
    UPDATE_CHAT = "Origanimeinfo"
    BOT_USERNAME = "AnimeharemindoBot"
    CHARA_CHANNEL_ID = "-1002124487227"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
