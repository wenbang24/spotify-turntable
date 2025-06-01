---
title: "Spotify Turntable"
author: "Ben Wang"
description: "A spotify controller that looks like a cute turntable!"
created_at: "2025-05-30"
---

# Journal of Changes
## 2025-05-30
Spent ages fighting with spotifyd, spotify-cli-linux, spotify-tui, raspotify, librespot, and other spotify clients. None of them worked.
Eventually I made an [issue](https://github.com/Spotifyd/spotifyd/issues/1221#issuecomment-2925151914) and found out it probably will not work.
Time spent: 6 hrs

## 2025-06-01
So there's this cool library called spotipy which I probably should have used in the first place. It has a python client that can control spotify so I can interface it with GPIO pins too :)
Also spent a while trying to get it to work with my HDMI display and the X server
Time spent: 5 hrs
