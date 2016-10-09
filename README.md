# Discord Music Bot

This plugin allows Discord users with the `DJ` role to use a variety of commands to control a jukebox style music bot.

## Usage

## Requirements

- Vagrant
- Virtualbox

## Building & Running

Run the following commands to start the virtual machine:
```bash
git clone git@github.com:dddicillo/discord-music-bot.git
cd discord-music-bot

# If you don't already have the hostmanager plugin
vagrant plugin install vagrant-hostmanager

vagrant up
vagrant ssh
cd /vagrant
```

You will need a Discord API key in order to run the bot. Go [here](https://discordapp.com/developers/applications/me) if you need to generate a new key. You'll need to paste your key into the appropriate location within the `conf/music_bot.ini` file. A template configuration file can be found under `conf/sample.music_bot.ini`.

Run the following commands to launch the bot program:
```bash
python3.5 -m pip install -r requirements.txt
python3.5 -m music_bot
```

