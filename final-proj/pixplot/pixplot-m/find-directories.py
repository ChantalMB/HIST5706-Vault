import os

# create list of my pages
path = "./chapbook-illustrations/"
list_of_illustrations = []

for file in os.listdir(path):
    list_of_illustrations.append(file)

# locate the parent folder of these pages
path = "/home/cbrou/Desktop/YODH-project/nls-data-chapbooks/"
og_paths = []
for i in list_of_illustrations:
    for root, dirs, files in os.walk(path):
        for name in files:
            if name == i:
                og_paths.append(os.path.join(root, name))

folder_key = []
illu_value = []
for path in og_paths:
    sep_path = path.split(os.sep))

    folder_key.append(sep_path[6])
    illu_value.append(sep_path[8])