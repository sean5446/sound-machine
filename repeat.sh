#!/bin/bash

DIR=$PWD/sounds
SOUND_FILE=rain

if [ ! -z "$1" ]; then
    SOUND_FILE=$1
fi

while [ 1 ]; do
  omxplayer $DIR/$SOUND_FILE.mp3
  sleep 0.1
done

