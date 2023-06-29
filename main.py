@client.event
async def on_ready():
    os.system('clear')
    activity = discord.Activity(type=discord.ActivityType.watching,
                                name="BY.IKGA-SOURCEC")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    vc = discord.utils.get(client.get_guild(GUILD_ID).channels, id=CHANNEL_ID)
    await vc.guild.change_voice_state(channel=vc,
                                      self_mute=False,
                                      self_deaf=True)
    print("Start ! BY.IKGA-SOURCE")


keep_alive()
client.run(os.getenv("TOKEN"), bot=True)
