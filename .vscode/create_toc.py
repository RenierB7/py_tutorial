import os



toc = """# Table of contents
# Learn more at https://jupyterbook.org/customize/toc.html

format: jb-book
root: index
chapters: """
print("Scanning root directory for chapters...")
folders = {folder.path:{} for folder in os.scandir("./py_tutorial/") if folder.name not in ["_build"] and folder.is_dir()}
print("Directory scanned.\nScanning for sections...")
for folder in folders:
    folders[folder] = {c_folder.path.replace("\\","/"):[] for c_folder in os.scandir(folder) if c_folder.name not in ["_build"] and c_folder.is_dir()}
print("Sections scanned.\nBuilding toc...")
for folder in folders:
    print(f"Adding chapter {folder}")
    chapter = f"\n- file: {folder[14:]}/index"
    if folders[folder].keys():
        print("Sections available for chapter, adding sections...")
        chapter += "\n  sections:"
        for section in folders[folder]:
            print(f"\tAdding section {section}")
            chapter += f"\n  - file: {section[14:]}/index"
    print("Chapter added to toc")
    toc += chapter

#print(toc)
print("Removing old _toc.yml")
os.remove("./py_tutorial/_toc.yml")
print("Removed.\nCreating new _toc.yml...")
with open("./py_tutorial/_toc.yml",'x') as file:
    file.write(toc)
    print("File created")