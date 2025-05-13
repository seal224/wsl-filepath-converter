import pyperclip
path = input("Enter file path: ")
path = path.replace("\\", "/")
path = path.replace(":", "", 1) #replace drive letters
path = path.replace('"', '')
path = path.lower()
path = "/mnt/" + path
print(path)
pyperclip.copy(path)
input("Press any key to exit")