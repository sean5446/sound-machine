#!/bin/bash

DIR=$PWD/sounds
SOUND_FILE=rain

if [ ! -z "$1" ]; then
    SOUND_FILE=$1
fi

# old pi add:
#  -A alsa to cvlc command
#  remove the force_hdmi from /boot/config.txt 

cvlc -R --intf dummy $DIR/$SOUND_FILE.mp3

#while [ 1 ]; do
#  omxplayer $DIR/$SOUND_FILE.mp3
#  sleep 0.1
#done
