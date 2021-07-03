#This is the first optional assignment of day 3, this code is to auto-subscribe a youtube channel.
#The thing to b e considered in this code is that the x and y positions in pyautogui.moveTo varies with your screen resolution.
import pyautogui
pyautogui.moveTo(255,1075,duration=2)
pyautogui.click()
pyautogui.typewrite('chrome')
pyautogui.typewrite(['enter'])
pyautogui.moveTo(970,100,duration=2)
pyautogui.click()
pyautogui.typewrite('https://www.youtube.com/channel/UChLNiQTld_EJOHaKqB3BDSg')
pyautogui.typewrite(['enter'])
pyautogui.moveTo(1325,308,duration=2)
pyautogui.click()
print(pyautogui.position())
