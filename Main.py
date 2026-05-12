# Global imports
from dotenv import load_dotenv
import asyncio
import discord
import json
import os

# Local imports
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
ModerationActionPreformed = "Did I get it wrong? Tell me with !report <insert text here>"


# I honestly don't know what this does but it's important
@Client.event
async def on_ready():
    print(f"\033[34mDISCORD_BOT_INFO:\033[0m Logged in as: {Client.user}")

@Client.event
async def on_message(RawMessage):
    # Message cleanup code
    ContentCheck = RawMessage.content.strip().lower().replace("'", "")
    Message = RawMessage.content.strip("'", "")

    # Checks for the prefix, if prefix found executes that code
    if ContentCheck.startswith(CommandPrefix):
        await CommandSystem(ContentCheck, Message)
        return
    elif RawMessage.channel.id == COUNTING_CHANNEL_ID:
        await CountingSystem(ContentCheck, RawMessage)
        return
    else:



















