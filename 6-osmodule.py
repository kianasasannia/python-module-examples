import os
print(os.name)
os.mkdir("c://users/Alice")
os.rmdir("c://users/Alice")
os.system("music.mp3")
print("path:",os.getcwd())
os.chdir("d://")
os.rename("C:\\Users\Student\Desktop\m3.mp3","C:\\Users\Student\Desktop\m1.mp3")
print("path:",os.getcwd())
a=os.access("C:\Program Files\\nodejs\\node.exe",os.F_OK) #R,W,X
print(a)
os.system("tree")














