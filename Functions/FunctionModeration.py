async def BlacklistCheck(DiscordMessage, ContentCheck, LoggingChannelID, ModerationActionPreformed, Client, BlacklistedWord):
    BlacklistedWord = False
    if BlacklistedWord == True:
        await DiscordMessage.delete()
        await DiscordMessage.channel.send(f"Message from {DiscordMessage.author.mention} deleted for containing a blacklisted word")
        await DiscordMessage.channel.send(f" {ModerationActionPreformed}")
        LoggingChannel = Client.get_channel(LoggingChannelID)
        await LoggingChannel.send(f"Deleted message from {DiscordMessage.author.mention} for containing a blacklisted word. Message content: {DiscordMessage.content}")
        return (BlacklistedWord)
    else:
        return (BlacklistedWord)
    
async def AutoRoleHierarchy():
    return

async def ChannelActions():
    return