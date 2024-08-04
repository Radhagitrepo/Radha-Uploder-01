import os

API_ID = API_ID =  23303247

API_HASH = os.environ.get("API_HASH", "23623f737dc15708708c65a7297e1510")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6807305648:AAFTD-XuufEPUVgdEub1QfDNpm5xdaVHjiw")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", ))

LOG = ,

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6335525003").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


