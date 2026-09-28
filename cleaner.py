import os, shutil
desktop = os.path.expanduser("~/Desktop")
target = os.path.join(desktop, "Code_Projects")
shutil.move(desktop + "/vanderbilt.py", target + "/vanderbilt.py")
print("Successfully moved vanderbilt.py")