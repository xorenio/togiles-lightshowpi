# COPY OF https://bitbucket.org/togiles/lightshowpi.git

Edits to make work only plus shrek file




Join us on our [Reddit page](https://www.reddit.com/r/LightShowPi/) and / or [Facebook page](https://www.facebook.com/lightshowpi) as well to share your experiences using lightshowPi, as well as videos of your shows!

Thanks, and enjoy ;)

Todd Giles ([todd@lightshowpi.org](mailto:todd@lightshowpi.org))

Installation / Getting Started
==============================

Please visit the [Getting Started Page](http://lightshowpi.org/getting-started) for details on getting
started.  Or for those who want to just jump on in, feel free to run the install.sh script and go 
for it :-)

Directory Structure
===================

* bin/* - Various bash scripts / tools to aid in playing songs, controlling volume, etc...
* config/* - Configuration files.
* crontab/synchronized_lights - Add these via 'sudo crontab -e' to start / stop the lightshow automatically
* logs/* - Log files will be output here.
* music/* - Music files go here (includes some samples to get you started).
* py/* - All the python code.
* tools/* - Various tools helpful in configuring / using / etc... LightshowPi

Contributors
============

A huge thanks to all those that have contributed to the Lightshow Pi codebase:

* Todd Giles
* Chris Usey
* Ryan Jennings
* Sean Millar
* Scott Driscoll
* Micah Wedemeyer
* Chase Cromwell
* Bruce Goheen
* Paul Dunn
* Stephen Burning
* Eric Higdon
* Tom Enos
* Brandon Lyon
* Ken B
* Paul Barnett
* Anthony Tod
* Brent Reinhard
* Caleb H
* Filippo B

Release Notes
============

2021/11/11 :: Version 3.21
-------------------------------

* Caleb H contribution of .csv parsing as import sequence channel data
* Filippo B contribution of add active_low_mode by channel

2021/11/09 :: Version 3.20
-------------------------------

* Fixes for Pi4(B), kernel and Debian 11 based OS
* dir_play support multiple uploads

2019/12/24 :: Version 3.11
-------------------------------

* microweb - Directory Play page under Playlist page

2019/12/20 :: Version 3.10
-------------------------------

* network - support for server/serverjson send to specific IPs
* LED - add tools/led_test.py 
* add Arduino/nodemcu/lspi-gpio-mcp23017-0.ino for nodemcu/MCP23017 combination to allow 16 GPIOs

2019/11/27 :: Version 3.02
-------------------------------

* bin/vol to support USB sound devices
* serverjson fix for hardware_controller.py and sketch v1.5, broadcast bug
* minor bugs and error handling 

2019/11/09 :: Version 3.01
-------------------------------

* Expander chipset bug fixed
* Custom LED strip color maps, allow LEDs to work in network client mode 

2019/10/05 :: Version 3.0
-------------------------------

* Upgrade to python 3.x
* Various bug-fixes and updates to support install on latest Raspbian versions and Pi 4

2018/10/16 :: Version 1.4
-------------------------------

* Microweb V3 with multiple features
* More patterns and features for RGB LED Pixels
* Option to add argument --config=overridesX.cfg to synchronized_lights.py and others
* Networking serverraw option and NodeMCU sketch for client device 
* Various bug-fixes and updates to support install on latest Raspbian versions and Pi 3b+

2017/10/27 :: Version 1.3
-------------------------------

* Added initial support for controlling individually controllable RGB LED lights (thanks to Tom Enos, Ken B, and Chris Usey)
* Addition of the "microweb" UI for controlling your lightshow (thanks to Ken B)
* Twitter support, tweeting current song playing (thanks to Brent Reinhard and Ken B)
* Various bug-fixes and updates to support latest kernel versions (thanks to Ken B)

2016/10/16 :: Version 1.2
-------------------------------

* 3 to 4 times speed improvement by utilizing GPU for fft and other optimizations (thanks to Tom Enos, Colin Guyon, and Ken B)
* support for streaming audio from pandora, airplay, and other online sources (thanks to Tom Enos and Ken B)
* support fm broadcast on the pi2 and pi3 (thanks to Ken B)
* multiple refactors + addition of comments to the code + clean-up (thanks to Tom Enos)
* add the ability to override configuration options on a per-song basis (thanks to Tom Enos)
* support pagination for the SMS 'list' command (thanks to Brandon Lyon)
* support for running lightshow pi on your linux box for debugging (thanks to Micah Wedemeyer)
* addition of new configuration parameters to tweak many facets of the way lights blink / fade (thanks to Ken B)
* addition of new configuration parameters to tweak standard deviation bounds used (thanks to Paul Barnett)
* support a "terminal" mode for better debugging w/out hardware attached (thanks to Anthony Tod)
* many other misc bug fixes (see Issues list for more details)

2014/11/27 :: Version 1.1
-------------------------------

* piFM support (thanks to Stephen Burning)
* audio-in support (thanks to Paul Dunn)
* command line play-list generator (thanks to Eric Higdon)
* enhancements to preshow configuration, including per-channel control  (thanks to Chris Usey)
* support for expansion cards, including mcp23s17,mcp23017 (thanks to Chris Usey)
* updated to support RPi B+ (thanks to Chris Usey)
* clarification on comments and in-code documentation (thanks to Bruce Goheen, Chase Cromwell, and Micah Wedemeyer)
* other misc bug fixes (see Issues list for more details)

2014/02/16 :: Version 1
-------------------------------

* First "stable" release
