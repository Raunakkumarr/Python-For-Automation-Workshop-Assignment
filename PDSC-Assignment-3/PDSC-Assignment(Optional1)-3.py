import pyautogui
pyautogui.moveTo(255,1075,duration=2)
pyautogui.click()
pyautogui.typewrite('chrome')
pyautogui.typewrite(['enter'])
pyautogui.moveTo(970,100,duration=2)
pyautogui.click()
pyautogui.typewrite('https://www.youtube.com/channel/UChLNiQTld_EJOHaKqB3BDSg')
pyautogui.typewrite(['enter'])
pyautogui.moveTo(1330,308,duration=2)
pyautogui.click()
print(pyautogui.position())