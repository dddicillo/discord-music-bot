# Discord Music Bot

This plugin allows Discord users with the `DJ` role to use a variety of commands to control a jukebox style music bot.

## Usage

## Requirements

- Vagrant
- Virtualbox

## Building

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

