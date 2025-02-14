# Quick Setup Guide for Your Own Server

Follow these steps to set up the bot on your own server:

1. **Obtain the Bot Token**  
   Find your Bot Token and insert it into the `global_variables`.

2. **Create a Weather API Key**  
   Sign up at [OpenWeatherMap](https://openweathermap.org/) to create a Weather API key and insert it into the `global_variables`.

3. **Create a Channel on Your Server**  
   Create a channel specifically for the bot to prevent timeouts. The bot will send a message to this channel every 5 seconds.

4. **Obtain the Channel ID**  
   Find the Channel ID for the newly created channel and insert it into the `global_variables`.

5. **Install Required Libraries**  
   Run the following commands to install the necessary libraries:
   - Install Discord.py:  
     ```bash
     pip install discord.py
     ```
   - Install Requests:  
     ```bash
     pip install requests
     ```
   - Install JSON:  
     ```bash
     pip install json
     ```
   - Install Time:  
     ```bash
     pip install time
     ```

6. **Start the Script**  
   Run the `weatherbot.py` script.

7. **Run Certificate Installation on MacBook**  
   In the Python folder on your MacBook, execute `Install Certificates` command.
