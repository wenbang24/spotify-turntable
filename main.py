from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import pygame
import requests
from io import BytesIO
from PIL import Image, ImageStat
from time import sleep

load_dotenv()
sp = Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
    open_browser=False,
    scope="user-modify-playback-state user-read-playback-state"
))

pygame.init()
screen_width, screen_height = 480, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Now Playing')

pygame.font.init()
font = pygame.font.SysFont('SF Pro Display', 24)

last_track_id = None

def songInfo():
    playback = sp.current_playback()
    if playback and playback['is_playing']:
        track = playback['item']
        album_img_url = track['album']['images'][0]['url']
        track_name = track['name']
        artist_name = ", ".join([artist['name'] for artist in track['artists']])
        return album_img_url, track_name, artist_name
    return None, None, None

def textColor(image: Image.Image):
    resized = image.resize((50, 50)).convert("L")
    stat = ImageStat.Stat(resized)
    brightness = stat.mean[0]
    return (0, 0, 0) if brightness > 127 else (255, 255, 255)

def renderAlbumArt(img, track_name, artist_name):
    screen.fill((0, 0, 0))
    img = img.resize((screen_width, screen_height))
    text_color = textColor(img)
    mode = img.mode
    size = img.size
    data = img.tobytes()
    pygame_image = pygame.image.fromstring(data, size, mode)
    screen.blit(pygame_image, (0, 0))
    overlay = pygame.Surface((screen_width, 60), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 100))
    screen.blit(overlay, (0, screen_height - 60))
    track_text = font.render(track_name, True, text_color)
    artist_text = font.render(artist_name, True, text_color)
    screen.blit(track_text, (10, screen_height - 55))
    screen.blit(artist_text, (10, screen_height - 30))
    pygame.display.flip()

def displayAlbumArt():
    global last_track_id
    album_url, track_name, artist_name = songInfo()
    if album_url:
        playback = sp.current_playback()
        track_id = playback['item']['id']
        if track_id != last_track_id:
            response = requests.get(album_url)
            img = Image.open(BytesIO(response.content))
            renderAlbumArt(img, track_name, artist_name)
            last_track_id = track_id

def play_pause():
    playback = sp.current_playback()
    if playback and playback['is_playing']:
        print("Pausing playback")
        sp.pause_playback()
    else:
        print("Resuming playback")
        sp.start_playback()

def seek_forward():
    print("Skipping to next track")
    sp.next_track()

def seek_backward():
    print("Going to previous track")
    sp.previous_track()

def main():
    displayAlbumArt()
    try:
        while True:
            # make this work with the actual wiring once parts are received.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        play_pause()
                    elif event.key == pygame.K_RIGHT:
                        seek_forward()
                    elif event.key == pygame.K_LEFT:
                        seek_backward()
            displayAlbumArt()
            sleep(1)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
