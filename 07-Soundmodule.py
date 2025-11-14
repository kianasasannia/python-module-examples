import playsound
playsound.playsound('music.mp3')

import vlc
p = vlc.MediaPlayer("music.mp3")
p.play()

import webbrowser
webbrowser.open("music.mp3")

import os
os.system("mpg123 " + "music.mp3")
