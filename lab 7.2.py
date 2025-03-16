import pygame
import os
from pygame import mixer
import keyboard

pygame.init()
mixer.init()

music = "music"
songs = [os.path.join(music, file) for file in os.listdir(music) if file.endswith(".mp3")]
song_index = 0
paused = False

def play_music():
    global paused
    if paused:
        mixer.music.unpause()
    else:
        mixer.music.load(songs[song_index])
        mixer.music.play()
    paused = False

def stop_music():
    global paused
    mixer.music.pause()
    paused = True

def next_song():
    global song_index, paused
    if not paused:
        song_index = (song_index + 1) % len(songs)
        mixer.music.load(songs[song_index])
        mixer.music.play()

def prev_song():
    global song_index, paused
    if not paused:
        song_index = (song_index - 1) % len(songs)
        mixer.music.load(songs[song_index])
        mixer.music.play()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Music Player")

keyboard.add_hotkey("space", play_music)
keyboard.add_hotkey("s", stop_music)
keyboard.add_hotkey("right", next_song)
keyboard.add_hotkey("left", prev_song)

keyboard.wait("esc")