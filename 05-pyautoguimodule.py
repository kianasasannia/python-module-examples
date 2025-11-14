import pyautogui  
import time


screenWidth, screenHeight = pyautogui.size() # returns the monitor size  
# print("The Screen Width is: ", screenWidth)  
# print("The Screen Height is: ", screenHeight)   

currentMouseX, currentMouseY = pyautogui.position()  
# print("X Cordinate is: ", currentMouseX)  
# print("Y Cordinate is: ", currentMouseY)  

# pyautogui.moveTo(100, 150, duration = 3)  

# pyautogui.moveRel(72,23, 2)  

# time.sleep(5)

# pyautogui.click(72,23, 5, 2, 'left')  

x = 100  
y = 100  
# These methods are equivalent to the click(x,y)  
# pyautogui.mouseDown(x=x, y=y, button='left')  
# pyautogui.mouseUp(x=x, y=y, button='left')  

# time.sleep(2)
# pyautogui.scroll(100, 200, 500)   

# pyautogui.typewrite('Asghar', 0.5) 

# pyautogui.typewrite(["a","s","g","h","a","r", 'backspace', 'enter']) 

#pyautogui.alert(text='Hello I am a message box', title='JavaTpoint', buttons=['OK', 'Cancel']) 

# pyautogui.password(text='Please Enter Your First Name', title='', default='', mask='*')  

# pyautogui.alert('To Continue, Click OK to continue')  

# pyautogui.password('Enter password (text will be hidden)')

