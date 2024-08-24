import os, discord, json
from views.regionSettingView import regionSettingView
from views.languageSettingView import languageSettingView
from views.frameworkSettingView import frameworksSettingView
from views.jobTitleSettingView import jobTitleSettingView

from src.roleSelector import locationRoleSelector

# Load the environment variables from the .env file (For local enviroment)
from dotenv import load_dotenv
load_dotenv()

# Get Secrets
IT_JOBS_RADAR_TOKEN = os.getenv('IT_JOBS_RADAR_TOKEN')
SERVER_ID = int(os.getenv('SERVER_ID'))
LISTENING_CHANNEL = int(os.getenv('LISTENING_CHANNEL'))
CHANNEL_REMOTE = int(os.getenv('CHANNEL_REMOTE'))
CHANNEL_NSW = int(os.getenv('CHANNEL_NSW'))
CHANNEL_VIC = int(os.getenv('CHANNEL_VIC'))
CHANNEL_QLD = int(os.getenv('CHANNEL_QLD'))
CHANNEL_SA = int(os.getenv('CHANNEL_SA'))
CHANNEL_WA = int(os.getenv('CHANNEL_WA'))
CHANNEL_NT = int(os.getenv('CHANNEL_NT'))
CHANNEL_TAS = int(os.getenv('CHANNEL_TAS'))

main_guild = None

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)
# all_guilds = bot.guilds
# print(all_guilds)

@bot.event
async def on_connect():
    if bot.auto_sync_commands:
        await bot.sync_commands()
    print(f"{bot.user.name} connected.")

@bot.event
async def on_ready():
    global main_guild
    main_guild = await bot.fetch_guild(SERVER_ID)
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return
    
    if message.channel.id == LISTENING_CHANNEL:
        # Get the information matadata
        global main_guild
        message_id = message.id
        message_content = message.content

        # Get the information from the raw message
        filtered_message = message_content.split('\n')
        job_title = filtered_message[1]
        job_location = filtered_message[4]
        job_company = filtered_message[7]
        job_url = filtered_message[10]
        job_source = filtered_message[13]

        # Get the location role names which are related to the job
        target_location_role_tag = locationRoleSelector(job_location)
        print(target_location_role_tag)
        print(main_guild.roles)
        role = discord.utils.get(main_guild.roles , name=target_location_role_tag)

        if target_location_role_tag == None:
            with open("./data/errors/error.txt", "a") as f:
                f.write(f"Error: {job_location} is not a valid location\n")

        # Find the target channel
        CHANNEL_ID = int(os.getenv(f'CHANNEL_{target_location_role_tag}'))
        target_channel = bot.get_channel(CHANNEL_ID)

        # Create embed message
        message_to_send = f'**Location:** {job_location}\n\n**Company:** {job_company}\n\n<@&{role.id}>'
        footer = discord.EmbedFooter(text=f"This job is founded on {job_source}")
        with open('./data/banners/banner.json', 'r') as f:
            data = json.load(f)
            job_source_banner_url = data[job_source.lower()]
        image = discord.EmbedMedia(job_source_banner_url)
        embed = discord.Embed(title=job_title, description=message_to_send, url=job_url, footer=footer, image=image, colour=discord.Colour.blue())

        # Create URL button
        url_button = discord.ui.Button(url=job_url, label="Check details")

        # Create view
        view = discord.ui.View(url_button, timeout=None)

        # Send the message to the target channel
        await target_channel.send(embed=embed, view=view)
    else:
        return

# ----------------------------- Slash Commands -----------------------------
@bot.command(description="Select your regions")
async def region(interaction: discord.Interaction):
    global main_guild
    user = interaction.user
    view = regionSettingView(user, main_guild)

    await interaction.respond("**Select your regions**",view=view, ephemeral=True)

@bot.command(description="Select your programming languages")
async def lang(interaction: discord.Interaction):
    global main_guild
    user = interaction.user
    view = languageSettingView(user, main_guild)

    await interaction.respond("**Select your programming languages**",view=view, ephemeral=True)

@bot.command(description="Select your frameworks or libraries")
async def frame(interaction: discord.Interaction):
    global main_guild
    user = interaction.user
    view = frameworksSettingView(user, main_guild)

    await interaction.respond(f"**Select your frameworks or libraries**",view=view, ephemeral=True)

@bot.command(description="Select job titles you want to apply")
async def title(interaction: discord.Interaction):
    global main_guild
    user = interaction.user
    view = jobTitleSettingView(user, main_guild)

    await interaction.respond("**Select job titles you want to apply**",view=view, ephemeral=True)




bot.run(IT_JOBS_RADAR_TOKEN)