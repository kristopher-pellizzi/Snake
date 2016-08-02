#! /bin/bash

clear

echo "Installing Homebrew..."
ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
echo "Homebrew installed successfully!"
echo "\n###########################\n"
echo "Installing python3..."
brew install python3 hg sdl sdl_image sdl_mixer sdl_ttf portmidi
echo "Python3 installed successfully!"
echo "\n###########################\n"
echo "Installing pygame..."
pip3 install hg+http://bitbucket.org/pygame/pygame
echo "pygame installed successfully"!
exit