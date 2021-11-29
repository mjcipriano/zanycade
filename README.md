# zanycade


# Setup


## GoDot

```bash
cd ~
git clone https://github.com/hiulit/RetroPie-Godot-Game-Engine-Emulator.git
cd RetroPie-Godot-Game-Engine-Emulator/
sudo chmod +x setup-godot-engine-scriptmodule.sh
./setup-godot-engine-scriptmodule.sh --install
```
To update
```bash
cd ~/RetroPie-Godot-Game-Engine-Emulator/
git pull
./setup-godot-engine-scriptmodule.sh --update

To update the 'godot-engine' emulator, run:

'sudo /home/pi/RetroPie-Setup/retropie_setup.sh'

Go to:

|- Manage packages
  |- Manage optional packages
    |- godot-engine
      |- Update (from source)


```

NOTE: After running, I had to edit the /opt/retropie/configs/godot-engine/emulators.cfg file to remove the "--resolution x" line.



```bash
pi@zanycade:~/RetroPie/roms/godot-engine $ more override.cfg

[audio]
mix_rate=44100
output_latency=15
pi@zanycade:~/Retro

##############################

pi@zanycade:~/RetroPie/roms/godot-engine $ more settings/godot-engine-settings.cfg
# Settings for the godot-engine system (v1.8.1)

gpio_virtual_keyboard = ""
kms_drm_driver = ""
audio_driver = "ALSA"
video_driver = "GLES2"
#################################

pi@zanycade:~/RetroPie/roms/godot-engine $ more /opt/retropie/configs/godot-engine/emulators.cfg
godot-engine-2.1.6 = "FRT_X11_UNDECORATED=true   /opt/retropie/emulators/godot-engine/frt_2.1.6_pi2.bin -main_pack %ROM% -ad ALSA -vd GLES2 --frt exit_on_shiftenter=true"
godot-engine-3.0.6 = "FRT_X11_UNDECORATED=true   /opt/retropie/emulators/godot-engine/frt_3.0.6_pi2.bin --main-pack %ROM% --audio-driver ALSA --video-driver GLES2 --frt exit_on_shiftenter=true"
godot-engine-3.1.2 = "FRT_X11_UNDECORATED=true   /opt/retropie/emulators/godot-engine/frt_3.1.2_pi2.bin --main-pack %ROM% --audio-driver ALSA --video-driver GLES2 --frt exit_on_shiftenter=true"
godot-engine-3.3.4 = "FRT_X11_UNDECORATED=true   /opt/retropie/emulators/godot-engine/frt_3.3.4_pi2.bin --main-pack %ROM% --audio-driver ALSA --video-driver GLES2 --frt exit_on_shiftenter=true"
godot-engine-3.4 = "FRT_X11_UNDECORATED=true   /opt/retropie/emulators/godot-engine/frt_3.4_pi2.bin --main-pack %ROM% --audio-driver ALSA --video-driver GLES2 --frt exit_on_shiftenter=true"
default = "godot-engine-3.4"


```
https://github.com/hiulit/RetroPie-Godot-Engine-Emulator


### Building/Exporting from GoDot

Download export template from: 

https://github.com/hiulit/Unofficial-Godot-Engine-Raspberry-Pi/blob/main/README.md

* In the editor, go to Project -> Export.
* Select the Linux/X11 template.
* In Binary Format, uncheck 64 bits.
* In Custom template -> Release, select the version of the export template that matches the version of your project.
* Click Export Project.
* Uncheck Export With Debug.
* Optionally, after the game is packed, you can rename the extension of the game's executable binary from .x86 to .rpi4 to avoid confusion.

Optionaly, you can export a pck
* In the editor, go to Project -> Export.
* Select the Linux/X11 template.
* In Binary Format, uncheck 64 bits.
* Click Export PCK/ZIP.
* Uncheck Export With Debug.
* Enter the name of your game with the .pck extension.
* Click Save.

## 🎮 How to run a game

### Case 1

- The is no `.pck` file (meaning that it's embedded/compiled in the executable binary).
- The `.pck` file has the same name as the executable binary and they are both in the same directory.

You can just run the executable binary, like this:

```
./name_of_your_godot_game.ext
```

### Case 2

- The `.pck` file has a different name than the executable binary.
- The `.pck` file is in a different directory than the executable binary.
- You are using an independent `.pck` file (without an executable binary).

You'll have to pass the `.pck` file's path using the `--main-pack` option, like this:

```
./godot_x.x.x_rpi4_export-template.bin --main-pack "/path/to/the/pck/file.pck"
```

