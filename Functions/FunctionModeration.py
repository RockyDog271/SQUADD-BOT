async def BlacklistCheck(DiscordMessage, ContentCheck, LoggingChannelID, ModerationActionPreformed, Client, BlacklistedWord):
    Blacklisted = False
    Blacklisted = LinkBlacklistCheck()
    
    with open("blacklist.txt", "r", encoding = "utf-8") as Blacklist:
        for line in Blacklist:
            BlacklistWord = line.strip().lower().replace("'", "")
            if BlacklistWord in ContentCheck:
                Blacklisted = True
                break
            


    # for word in blacklist, check if ContentCheck contains blacklisted word


    
    
    
    
    
    if Blacklisted == True:
        await DiscordMessage.delete()
        await DiscordMessage.channel.send(f"Message from {DiscordMessage.author.mention} deleted for containing a blacklisted word")
        await DiscordMessage.channel.send(f" {ModerationActionPreformed}")
        LoggingChannel = Client.get_channel(LoggingChannelID)
        await LoggingChannel.send(f"Deleted message from {DiscordMessage.author.mention} for containing a blacklisted word. Message content: {DiscordMessage.content}")
        return (Blacklisted)
    else:
        return (Blacklisted)

async def LinkBlacklistCheck():
    return

async def AutoRoleHierarchy():
    return

async def ChannelActions():
    return

# IF music

    # IF contains link

        # checks if valid link to music site

        # checks if link is blacklisted

        # IF blacklisted

            # moderate

# IF weblinks

    # IF contains link

        # checks if valid link

        # IF invalid

            # moderate

        # checks if link is blacklisted

        # IF blacklisted

            # moderate


# IF shareclips

    # IF contains link

        # checks for "clip"

        # IF missing "clip"

            # deletes message and moderation message

        # checks if link is blacklisted

        # IF blacklisted

            # moderate

            