bash $HOME/RetroPie-BGM-Player/bgm_system.sh -s
pkill -STOP mpg123
echo "starting system:$1 emulator:$2 rom:$3"  >> ~/logs/gamerun.log
/home/pi/custom/setLedByGame.py $1 $2 $3 &
# the line below is needed to use the joystick selection by name method
bash "/opt/retropie/supplementary/joystick-selection/js-onstart.sh" "$@"
