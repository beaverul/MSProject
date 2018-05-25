from pygame import mixer # Load the required library
import time
mixer.init()
mixer.music.load('/home/pi/morning_alarm_2.mp3')
mixer.music.set_volume(1.0)
mixer.music.play()
mixer.music.set_volume(1.0)
time.sleep(1)
mixer.music.set_volume(0.5)
time.sleep(2)
mixer.music.set_volume(1)
time.sleep(10)
mixer.music.stop()