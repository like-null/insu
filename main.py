import time
import pyautogui as pg
from pyfiglet import Figlet
f = Figlet(font='doom')
print(f.renderText('InSu'))
print("------------------------------Namaste------------------------------------")
#screensize = pyautogui.size()
#setp 1 search Point(x=236, y=98)
print("----------------(Insu(v0.5) Instagram Bot by likenull)-------------------")
count = 0
numlikes = int(input("How many post to like: "))
print(str(numlikes) + " posts to like")
print()
hastag = str(input("Hashtag to use:"))
print("Using hashtag: " + str(hastag))
print()
print("Launching(slow mode)...")
time.sleep(2)
pg.click(236, 98)
pg.write(hastag)
print()
pg.PAUSE = 3.25
pg.press('down')
pg.PAUSE = 2.0
pg.press('enter')
pg.press('enter')
pg.PAUSE = 3.6
pg.press('pagedown')
#Step 2 post click
pg.PAUSE = 2.0
pg.click(98, 518)
pg.PAUSE = 3.0
#alinging pointer to the middle Point(x=339, y=400)
print("Liking recent Post by tag.....")
print()
pg.moveTo(332, 400)
pg.Pause = 2.0
pg.doubleClick(332, 400)
print("First post liked")
print()
print("************************************************************************")
pg.Pause = 3.5
pg.press('right')
count = 1
while (count < numlikes):
    count = count + 1
    pg.doubleClick(332, 400)
    pg.Pause = 4.0
    pg.press('right')
    print("\rPosts liked: "+str(count), end='')
    pg.Pause = 0.1


else:
    print("********************************************************************")
    Print()
    print(str(numlikes) +" Post liked. By tag" + str(hastag))


#print(screensize)
#print(pointer)
