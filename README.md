# Spotify Turntable
A spotify controller that looks like a cute turntable! Uses an ESP32 to connect to the Spotify API and control playback, and displays the current track on a small HDMI display. The turntable is made from a 3D-printed case.
![images](img/v1.png)

## Features
- Control Spotify playback (play, pause, next, previous)
- Display current track information on a small display
- Looks like a cute turntable with a 3D-printed case and a vinyl with your song's album art

## BOM
- 2.8 inch circular HDMI display with ESP32 without touch e.g. [this ($35.80)](https://www.aliexpress.com/item/1005008550178220.html?src=google&pdp_npi=4@dis!AUD!54.99!54.99!!!!!@!12000045664378399!ppc!!!&gPromoCode=5000000171197014)
- 3D-printed case (files in `case/`)
- 15mm half shaft rotary encoder e.g. [this ($1.20)](https://www.aliexpress.com/item/1005004907970664.html?spm=a2g0o.productlist.main.5.2da045d1nlJrMq&aem_p4p_detail=202506020223422245208670988800003310716&algo_pvid=1ed82abb-ead1-40ac-a9ce-d23354ae28b5&algo_exp_id=1ed82abb-ead1-40ac-a9ce-d23354ae28b5-4&pdp_ext_f=%7B%22order%22%3A%22919%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21AUD%212.61%211.82%21%21%2112.00%218.37%21%40210318ec17488562220337880ee573%2112000035534364750%21sea%21AU%210%21ABX&curPageLogUid=be3vKUHMXXIE&utparam-url=scene%3Asearch%7Cquery_from%3A&search_p4p_id=202506020223422245208670988800003310716_5)
- 8x 8mm diameter, 3mm thick neodymium magnets e.g. [this ($4.80)](https://www.bunnings.com.au/everhang-8mm-rare-earth-disc-magnet-10-pack_p3690098)
- 2x Cherry MX switches e.g. [this ($2.60)](https://www.aliexpress.com/item/1005004738349644.html?spm=a2g0o.productlist.main.8.4142XNWnXNWnFW&aem_p4p_detail=202506130317312222566771085360000959567&algo_pvid=b3c08b78-df88-4a49-b418-2b445499a557&algo_exp_id=b3c08b78-df88-4a49-b418-2b445499a557-7&pdp_ext_f=%7B%22order%22%3A%2231%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21AUD%214.46%214.01%21%21%212.85%212.56%21%402103246617498098511304569e5b37%2112000030295107214%21sea%21AU%210%21ABX&curPageLogUid=6nv1vCw1BfIO&utparam-url=scene%3Asearch%7Cquery_from%3A&search_p4p_id=202506130317312222566771085360000959567_2)
- 2x Cherry MX keycaps e.g [this ($2.80)](https://www.aliexpress.com/item/1005006073494474.html?spm=a2g0o.productlist.main.10.73d47efdeEOdyM&algo_pvid=3c78a5cd-8d96-460d-8827-cda468addcdf&algo_exp_id=3c78a5cd-8d96-460d-8827-cda468addcdf-9&pdp_ext_f=%7B%22order%22%3A%22229%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21AUD%217.92%213.16%21%21%2136.31%2114.48%21%402101eac917498101722201935e6426%2112000035608346606%21sea%21AU%210%21ABX&curPageLogUid=4BB2LDatnVO5&utparam-url=scene%3Asearch%7Cquery_from%3A)
- 2x 10kΩ resistors e.g. [this ($1.00)](https://www.aliexpress.com/item/1005005670101072.html?spm=a2g0o.productlist.main.9.502679b58dP7TT&algo_pvid=da143a61-6084-434e-a1ad-542ed48c36c8&algo_exp_id=da143a61-6084-434e-a1ad-542ed48c36c8-8&pdp_ext_f=%7B%22order%22%3A%222261%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21AUD%212.86%211.55%21%21%2113.12%217.09%21%402101c5b217498102409561094e5ffb%2112000033959066986%21sea%21AU%210%21ABX&curPageLogUid=DTdR2VHUucR0&utparam-url=scene%3Asearch%7Cquery_from%3A)
- Jumper wires (male to anything) e.g. [this ($2.00)](https://www.aliexpress.com/item/1005003641187997.html?spm=a2g0o.productlist.main.2.679753e8nMWokI&algo_pvid=cf617b24-7e97-4b1f-a866-4745926139bb&algo_exp_id=cf617b24-7e97-4b1f-a866-4745926139bb-1&pdp_ext_f=%7B%22order%22%3A%225331%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21AUD%213.66%212.66%21%21%212.34%211.70%21%402101efeb17498100009593808e9df1%2112000026613929400%21sea%21AU%210%21ABX&curPageLogUid=7PAP1hNr6YuX&utparam-url=scene%3Asearch%7Cquery_from%3A)

Total: $50.20

## Wiring
Something like this:
![image](img/wiring.png)

## Setting Up
(will refine this when I get the parts)
1. Get your Spotify API credentials by creating an app on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications). You will need the Client ID and Client Secret.
2. Clone this repository:
    ```bash
    git clone https://github.com/wenbang24/spotify-turntable
    cd spotify-turntable
    ```
3. Create a `.env` file in the root of the repository with your Spotify API credentials:
    ```plaintext
    SPOTIFY_CLIENT_ID='your-spotify-client-id'
    SPOTIFY_CLIENT_SECRET='your-spotify-client-secret'
    SPOTIFY_REDIRECT_URI='your-app-redirect-url'
    ```

    Note: The redirect URI can be set to `http://localhost:8888/callback` - it doesn't really matter.
4. Run the `spotify_turntable.py` script to start the application and cache authentication details:
    ```bash
    python3 spotify_turntable.py
    ```

    Follow the instructions.
