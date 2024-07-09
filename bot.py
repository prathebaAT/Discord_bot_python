import discord
from job_portal import JobPortal  # Import the JobPortal class from job_portal.py

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
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$job'):
        await send_job_alerts(message.channel)

async def send_job_alerts(channel):
    feed_url = ' ' #your url link here
    portal = JobPortal(feed_url)
    portal.fetch_jobs()
    recent_jobs = portal.get_recent_job_listings(days=1)
    
    
    if not recent_jobs:
        await channel.send("No job listings found.")
        return
    
    for job in recent_jobs:
        job_message = (
            f"**Title:** {job.title}\n"
            f"**Company:** {job.company}\n"
            f"**Location:** {job.location}\n"
            f"**Type:** {job.job_type}\n"
            f"**Link:** {job.link}\n"
            f"**Published:** {job.published}\n"
            f"**Category:** {job.category}\n"
            f"{'=' * 30}"
        )
        await channel.send(job_message)

client.run('')
