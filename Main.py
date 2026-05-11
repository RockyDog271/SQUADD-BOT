import osimport json
import asyncio
import discord
from dotenv import load_dotenv

# load in the .env file
load_dotenv()

# all the "loading" of the .env variables
CLIPSHARE_CHANNEL_ID = int(os.getenv("CLIPSHARE_CHANNEL_ID"))
WEBLINKS_CHANNEL_ID = int(os.getenv("WEBLINKS_CHANNEL_ID"))
COUNTING_CHANNEL_ID = int(os.getenv("COUNTING_CHANNEL_ID"))
MUSIC_CHANNEL_ID = int(os.getenv("MUSIC_CHANNEL_ID"))
# TOKEN FOR BOT, seperate from /\ cuz its imporetant
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# this is required
intents = discord.Intents.default()

# all the easily changable variables for bot
    # GENERAL FUNCTIONS
CommandPrefix = ">>"
EnableHelpCommand = True
EnableVerboseLogging = True
LoggingChannelID = 0000000000000000
    # MODERATION FUNCTIONS
RoleOnJoinID = 0000000000000000
NumberOfMessagesUntilMember = 1
MemberRoleID = 0000000000000000
NumberOfMessagesUntilVerification = 20
VerifiedRoleID = 0000000000000000
    # COUNTING FUNCTIONS
SuccessfulCountsUntilSave = 20
MaxNumberOfSaves = 5
    # MESSAGE REFERENCES
ModerationActionPreformed = "Did I get it wrong? Tell me with !report <insert text here>