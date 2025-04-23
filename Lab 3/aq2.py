def backup(folder):
    import zipfile, os
    with zipfile.ZipFile(folder+'.zip','w') as z:
        for f in os.listdir(folder):
            z.write(os.path.join(folder,f))

backup("test_folder")  # replace with folder name