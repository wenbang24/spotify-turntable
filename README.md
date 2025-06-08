# Spotify Turntable
A spotify controller that looks like a cute turntable! Uses a Raspberry Pi Zero 2 W to connect to the Spotify API and control playback, and displays the current track on a small HDMI display. The turntable is made from a 3D-printed case.

## Features
- Control Spotify playback (play, pause, next, previous)
- Display current track information on a small HDMI display
- Looks like a cute turntable with a 3D-printed case

## BOM
- Raspberry Pi Zero 2 W
- 3D-printed case (files in `case/`)
- 2.8 inch circular HDMI display e.g. [this](https://www.aliexpress.com/item/1005008141918894.html?spm=a2g0o.productlist.main.11.7bc2JT6sJT6sUY&algo_pvid=8cb02878-8df8-4e4d-9da4-27218fc37741&algo_exp_id=8cb02878-8df8-4e4d-9da4-27218fc37741-10&pdp_ext_f=%7B%22order%22%3A%222%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21AUD%2158.45%2153.19%21%21%21265.94%21242.01%21%402101efeb17487435104118944e23aa%2112000043966697454%21sea%21AU%210%21ABX&curPageLogUid=orTnAghOjGGx&utparam-url=scene%3Asearch%7Cquery_from%3A)
- 15mm half shaft rotary encoder e.g. [this](https://www.aliexpress.com/item/1005004907970664.html?spm=a2g0o.productlist.main.5.2da045d1nlJrMq&aem_p4p_detail=202506020223422245208670988800003310716&algo_pvid=1ed82abb-ead1-40ac-a9ce-d23354ae28b5&algo_exp_id=1ed82abb-ead1-40ac-a9ce-d23354ae28b5-4&pdp_ext_f=%7B%22order%22%3A%22919%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21AUD%212.61%211.82%21%21%2112.00%218.37%21%40210318ec17488562220337880ee573%2112000035534364750%21sea%21AU%210%21ABX&curPageLogUid=be3vKUHMXXIE&utparam-url=scene%3Asearch%7Cquery_from%3A&search_p4p_id=202506020223422245208670988800003310716_5)
- 8x 8mm diameter, 3mm thick neodymium magnets e.g. [this](https://www.bunnings.com.au/everhang-8mm-rare-earth-disc-magnet-10-pack_p3690098)
- 2x Cherry MX switches
- 2x Cherry MX keycaps
- Jumper wires

## Wiring
(haven't prototyped this yet bc i dont have parts :|)

## Setting Up The Raspberry Pi
1. Install Raspberry Pi OS Lite on the Raspberry Pi Zero 2 W (remember to enable SSH), then SSH in. I set the username to be pi, so if you want something different, change the commands accordingly.
2. Install the necessary packages:
    ```bash
    sudo apt update
    sudo apt install python3-pip python3-dev libffi-dev libssl-dev
    ```
3. Install the Spotipy and PyGame libraries:
    ```bash
    pip3 install spotipy
    sudo apt install python3-pygame
    ```
4. Install the X server and necessary display drivers for the HDMI display:
   ```bash
   sudo apt install xserver-xorg xinit
   ```
5. Configure the HDMI display by editing the `/boot/config.txt` file:
    ```bash
    sudo nano /boot/config.txt
    ```

    Add the following lines to configure the display:
    ```plaintext
    hdmi_force_hotplug=1
    hdmi_group=2
    hdmi_mode=87 # not sure about this yet, might need to change
    hdmi_cvt=320 240 60 6 0 0 0
    ```
6. Reboot the Raspberry Pi
7. Enable Auto-login for the Pi user:
    ```bash
    sudo mkdir -p /etc/systemd/system/getty@tty1.service.d
    sudo nano /etc/systemd/system/getty@tty1.service.d/autologin.conf
    ```

    Add the following lines:
    ```plaintext
    [Service]
    # Clear out the original ExecStart so we can override it:
    ExecStart=
    # Launch agetty with --autologin pi on tty1, no-clear
    ExecStart=-/sbin/agetty --autologin pi --noclear %I $TERM
    ```

    Reload the systemd configuration:
    ```bash
    sudo systemctl daemon-reload
    sudo reboot
    ```
8. Start the X server automatically on boot:
    Edit the `~/.bash_profile` file to start the X server automatically:
    ```bash
    sudo nano /home/pi/.bash_profile
    ```

    Add the following lines at the end:
    ```bash
    if [ -z "$DISPLAY" ] && [ "$(tty)" = "/dev/tty1" ]; then
        startx
    fi
    ```

    Ensure it is executable:
    ```bash
    sudo chmod +x /home/pi/.bash_profile
    ```
9. Get your Spotify API credentials by creating an app on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications). You will need the Client ID and Client Secret.
10. Clone this repository to the Raspberry Pi:
    ```bash
    git clone https://github.com/wenbang24/spotify-turntable
    cd spotify-turntable
    ```
11. Create a `.env` file in the root of the repository with your Spotify API credentials:
    ```plaintext
    SPOTIFY_CLIENT_ID='your-spotify-client-id'
    SPOTIFY_CLIENT_SECRET='your-spotify-client-secret'
    SPOTIFY_REDIRECT_URI='your-app-redirect-url'
    ```

    Note: The redirect URI can be set to `http://localhost:8888/callback` - it doesn't really matter.
12. Run the `spotify_turntable.py` script to start the application and cache authentication details:
    ```bash
    python3 spotify_turntable.py
    ```

    Follow the instructions.
13. Set the X server to run the script on boot:
    Edit the `~/.xinitrc` file:
    ```bash
    nano /home/pi/.xinitrc
    ```

    Add the following line to run the script:
    ```bash
    python3 /home/pi/spotify-turntable/spotify_turntable.py
    ```

    Make sure it is executable:
    ```bash
    sudo chmod +x /home/pi/.xinitrc
    ```

    Reboot the Raspberry Pi to test if everything works:
    ```bash
    sudo reboot
    ```
