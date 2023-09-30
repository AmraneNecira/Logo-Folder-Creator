import os

home_dir = "logo-file"
sub_folders = ["full-mockup", "iconic-mark", "word-mark", "master-file"]
node_folders = ["x1", "pdf", "svg"]


def sub_folder_creator():
    for x in range(len(sub_folders)):
        os.makedirs(sub_folders[x])
        if sub_folders[x] == "master-file":
            break
        for y in range(len(node_folders)):
            os.makedirs(os.path.join(sub_folders[x], node_folders[y]))


def file_creator(folder_name, path):
    if path == 'pwd':
        path = os.getcwd()
    elif path == '':
        path = os.path.join(os.path.expanduser('~'), 'Documents')
    os.chdir(path)
    try:
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' have been created successfully")
    except:
        print("This folder already exist")
    os.chdir(folder_name)
    if not os.path.isdir(home_dir):
        os.makedirs(home_dir)
        os.chdir(home_dir)
        sub_folder_creator()
        print("Sub_Folders have been created successfully")
    else:
        os.chdir(home_dir)
        sub_folder_creator()
        print("Folders have been updated successfully")


if __name__ == '__main__':
    folder_name = input("Enter folder name: ")
    path = input("Enter desired path: ")

    file_creator(folder_name, path)
