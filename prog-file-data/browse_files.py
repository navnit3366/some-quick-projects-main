import osfor files in os.listdir("C:\Users\SOS\Favorites\Desktop\programme_prog_yoann"):    if os.path.isdir(files):        print(files)        for file_sub in os.listdir(files):            print(file_sub)