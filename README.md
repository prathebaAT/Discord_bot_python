# Remotive Job Alert Discord Bot

This Discord bot fetches job listings from an Remotive RSS feed and sends recent job alerts to your created  Discord channel. 

## Features

- Fetch job listings from an RSS feed.
- Filter and display recent job listings based on the publication date.
- Display job details such as title, company, location, job type, link, published date, and category.


### Prerequisites

- Python 3.6 or higher
- `discord.py` library
- `feedparser` library

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/Discord_bot_python.git
    cd job-alert-discord-bot
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install discord.py feedparser
    ```

### Configuration

1. Replace your Discord token 

  
2. Create a new Discord server and add your bot to this server. To do this:
   - Go to the Discord Developer Portal.
   - Create a new application and add a bot to it.
   - Copy the bot token to the `config.py` file as mentioned above.
   - Generate an OAuth2 URL with the necessary permissions and use it to invite the bot to your server.

### Channel Configuration

Ensure that your bot has the necessary permissions to send messages in the channel where you want to receive job alerts. 
You may need to adjust the bot's role and permissions within your Discord server settings.

## Usage

1. Run the bot:

    ```bash
    python bot.py
    ```

2. Interact with the bot on your Discord server using the following commands:
    - `$hello`: The bot will respond with "Hello!"
    - `$job`: The bot will fetch and display recent job listings from the RSS feed.


## File Structure

- `job_portal.py`: Contains the `JobListing` and `JobPortal` classes to fetch and store job listings.
- `bot.py`: Contains the Discord bot implementation, handles commands, and sends job alerts.


Acknowledgments
This project uses job listings from Remotive.com, a remote job board and community.

Reference : https://remotive.com/remote-jobs/rss-feed


