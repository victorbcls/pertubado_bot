Here's a README for your Python Discord bot code:

# Discord Bot with Audio and Text-to-Speech Functionality

This Python Discord bot is designed to play audio files in a voice channel and convert text to speech. It includes a daily audio feature, custom text-to-speech commands, and more.

## Prerequisites

Before running the bot, ensure you have the following dependencies installed:

- Python 3.6+
- discord.py library (Install using `pip install discord.py`)
- FFmpeg (Required for audio playback, download from [FFmpeg website](https://www.ffmpeg.org/download.html))

## Setup

1. Clone or download the repository to your local machine.

2. Create a `config.py` file in the same directory as your bot code. Add the following configuration:

```python
# config.py

# Dictionary of jokes and their corresponding audio files
jokes = {
    "victorbarcelos": "icq.mp3",
   
}

# Allowed channels where the command can be executed
allowed_channels = ["🪐 Dathomir"]
```

3. Replace `TOKEN` in your bot code with your actual bot token.

## Usage

### Running the Bot

1. Open a terminal or command prompt.

2. Navigate to the directory containing your bot code.

3. Run the bot using the following command:

   ```shell
   python bot.py
   ```

### Bot Commands

- `!call_daily` or `!daily`: Plays a daily audio clip in the user's voice channel.

- `!play <text>` or `!fala <text>`: Converts the provided text into speech and plays it in the user's voice channel.

### Customization

- You can add more jokes and their corresponding audio files to the `config.py` file.

- Modify the `allowed_channels` list in `config.py` to specify where the bot commands are allowed.

- Customize the bot prefix by changing `command_prefix="!"` in your bot code.

- Implement the `read.readAndSave` function to handle text-to-speech conversion according to your needs.

### Daily Audio

The bot plays a daily audio clip at a specific time (currently set to 13:00 UTC). You can change the time by modifying the `routine_audio` function in your bot code.

## Contributing

Feel free to contribute to this project by adding new features, improving existing code, or fixing issues. Submit pull requests to the GitHub repository.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
