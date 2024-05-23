#Emiline Stewart
#Goes through a given folder and deletes all duplicate files
#########TO DO: Continue comparing files for all nested folders########

import hashlib, os, shutil
from zipfile import ZipFile

picture_folder = "C:\\Users\\estew\\Desktop\\New folder"
hash_list, file_list, pic_dict = [], [], {'hashes':[], 'fileNames':[]}

def dedup(folder):
    for file in os.listdir(folder):
        file_path = folder + '\\' + file 
        if os.path.isfile(file_path):
            hash = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
            hash_list.append(hash)
            file_list.append(file)
            pic_dict['hashes'] = hash_list
            pic_dict['fileNames'] = file_list
            matches = hash_list.count(hash)
            if matches > 1:
                dup_index = hash_list.index(hash) #Get the index value for the hash of the duplicate file
                dup_file = folder + "\\" + pic_dict['fileNames'][dup_index] #Get the name & path of the duplicate file based on that same index
                os.remove(dup_file) #Delete the duplicate file
                del pic_dict['hashes'][dup_index] #remove the duplicate file information from the dictionary since that dupe. file has been deleted
                del pic_dict['fileNames'][dup_index]

if picture_folder[-3:] == 'zip':
    uz_picture_folder = picture_folder.replace('.zip','')
    with ZipFile(picture_folder, 'r') as zipped:
        zipped.extractall(uz_picture_folder)
    for item in os.listdir(uz_picture_folder):
        try: 
            for file in os.listdir(item):
                old = uz_picture_folder + "\\" + item + "\\" + file
                new = uz_picture_folder + "\\" + file
                shutil.move(old, new)
                os.rmdir(uz_picture_folder + "\\" + item)
        except:
            continue
    #os.remove(picture_folder) #Delete the zip file after it's been unzipped
    dedup(uz_picture_folder)
else:
    dedup(picture_folder)