import os
saved_path = input("Enter path\n")
type(saved_path)
os.chdir(saved_path)
f = ["" for x in range(1000)]        # Directory Stack
k = -1
def recursion(saved):
    global k
    g = 0                        # Counts the number of directories
    c = 0                       # counter
    d = 0
    file = os.listdir(saved)
    for files in file:
        if os.path.isdir(files):
            g = g+1
    t = len(file) - g           # counts no. of files
    print("In Directory " + os.getcwd() + " Files: " + str(t) + " Directories: " + str(g) + "\n")
    for files in file:
        if os.path.isdir(files):
            os.chdir(saved+"/"+files)           # Going into the directory
            s = os.getcwd()
            k = k+1
            f[k] = "/" + files                  # Putting the directory name in stack
            d = d + 1
            print("\n Going in directory " + s)
            return recursion(s)
        else:
            statinfo = os.stat(files)
            days = statinfo.st_atime
            c = c + 1
            days = days/(3600*24)
            print(days)
            if days >= 150:
                decision = input("The file " + files + " in directory " + os.getcwd() + " has not been used recently," + " wanna delete it?" + " Enter 1 for yes, 0 for no \n")
                type(decision)
                if str(decision) == "1":
                    os.remove(files)
                    print(files + " is removed")
            if c >= t:                                  # If files are exhausted
                os.chdir(saved.replace(f[k], ''))
                saved = os.getcwd()
                k = k - 1
        if d >= g:                                      # If directories are exhausted
            os.chdir(saved.replace(f[k], ''))
            k = k - 1
            print(os.getcwd() + "\n")
            saved = os.getcwd()
        continue
    return
recursion(saved_path)
print("Done Checking for cleanup \n")
