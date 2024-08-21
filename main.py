import os, discord

# Load the environment variables from the .env file (For local enviroment)
from dotenv import load_dotenv
load_dotenv()

# Get Secrets
IT_JOBS_RADAR_TOKEN = os.getenv('IT_JOBS_RADAR_TOKEN')
LISTENING_CHANNEL = int(os.getenv('LISTENING_CHANNEL'))
CHANNEL_REMOTE = int(os.getenv('CHANNEL_REMOTE'))
CHANNEL_NSW = int(os.getenv('CHANNEL_NSW'))
CHANNEL_VIC = int(os.getenv('CHANNEL_VIC'))
CHANNEL_QLD = int(os.getenv('CHANNEL_QLD'))
CHANNEL_SA = int(os.getenv('CHANNEL_SA'))
CHANNEL_WA = int(os.getenv('CHANNEL_WA'))
CHANNEL_NT = int(os.getenv('CHANNEL_NT'))
CHANNEL_TAS = int(os.getenv('CHANNEL_TAS'))


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.channel.id == LISTENING_CHANNEL:
        # Get the information matadata
        message_id = message.id
        message_content = message.content

        # Get the information from the raw message
        filtered_message = message_content.split('\n')
        job_title = filtered_message[1]
        job_location = filtered_message[4]
        job_company = filtered_message[7]
        job_url = filtered_message[10]

        # Find the target channel
        target_channel = client.get_channel(1274728634946687006)

        # Create embed message
        message_to_send = f'**Location:** {job_location}\n\n**Company:** {job_company}\n\n<@&1273005059055030305>'
        footer = discord.EmbedFooter(text="This job is founded on Linkedin")
        image = discord.EmbedMedia("https://content.linkedin.com/content/dam/brand/site/img/logo/do/do-approved-assets.png")
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















client.run(IT_JOBS_RADAR_TOKEN)