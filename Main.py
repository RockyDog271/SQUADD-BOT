# Global imports
from dotenv import load_dotenv
import discord
import json
import os

# Local file imports
from Functions import FunctionModeration as ModerationSystem
from Functions import FunctionCounting as CountingSystem
from Functions import FunctionCommands as CommandSystem

# load in the .env file
load_dotenv()

# all the "loading" of the .env variables
CLIPSHARE_CHANNEL_ID = int(os.getenv("CLIPSHARE_CHANNEL_ID"))
WEBLINKS_CHANNEL_ID = int(os.getenv("WEBLINKS_CHANNEL_ID"))
COUNTING_CHANNEL_ID = int(os.getenv("COUNTING_CHANNEL_ID"))
MUSIC_CHANNEL_ID = int(os.getenv("MUSIC_CHANNEL_ID"))
# TOKEN FOR BOT, separate from /\ cuz its important
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# this is required for DISCORD
intents = discord.Intents.default()
Client = discord.Client(intents = intents)

# all the easily changeable variables for bot
    # GENERAL FUNCTIONS
CommandPrefix = ">>"
EnableHelpCommand = True
EnableVerboseLogging = True
LoggingChannelID = 1367403105930580038
    # MODERATION FUNCTIONS
RoleOnJoinID = 1366230527375577149
NumberOfMessagesUntilMember = 1
MemberRoleID = 1366230433230229554
NumberOfMessagesUntilVerification = 20
VerifiedRoleID = 1366230321938567269
    # COUNTING FUNCTIONS
SuccessfulCountsUntilSave = 20
MaxNumberOfSaves = 5
    # MESSAGE REFERENCES
ModerationActionPreformed = 'Did I get it wrong? Tell me with "!report <insert text here>"'


# I honestly don't know what this does but it's important
@Client.event
async def on_ready():
    print(f"\033[34mDISCORD_BOT_INFO:\033[0m Logged in as: {Client.user}")

@Client.event
async def on_message(DiscordMessage):
    # Message cleanup code
    ContentCheck = DiscordMessage.content.strip().lower().replace("'", "")
    Message = DiscordMessage.content.strip("'", "")

    # Check blacklist before moving forward
    Blacklisted = ModerationSystem.BlacklistCheck(DiscordMessage, ContentCheck, LoggingChannelID, ModerationActionPreformed, Client, Blacklisted)
    if Blacklisted == True:
        return
    ModerationSystem.AutoRoleHierarchy()

    # Checks for Command prefix, if contains prefix proceeds to call function
    if ContentCheck.startswith(CommandPrefix):
        await CommandSystem(DiscordMessage, Message, ContentCheck)
        return
    # Checks for the counting channel, if found calls that function
    elif DiscordMessage.channel.id == COUNTING_CHANNEL_ID:
        await CountingSystem(DiscordMessage, Message, ContentCheck)
        return
    # Checks for specific channels, if none are found it quits
    else:
        await ModerationSystem.ChannelActions(DiscordMessage, Message, ContentCheck)
        return
    
# Run da bot
Client.run(DISCORD_BOT_TOKEN)