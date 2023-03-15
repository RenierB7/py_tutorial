import os, re
def section_sort_key(x):
    pattern = re.compile(r".*?S(\d+).*?")
    match = pattern.fullmatch(x)
    return bool(match) and int(match.group(1))

def chapter_sort_key(x):
    pattern = re.compile(r".*?P(\d+).*?")
    match = pattern.fullmatch(x)
    return bool(match) and int(match.group(1))


toc = """# Table of contents
# Learn more at https://jupyterbook.org/customize/toc.html

format: jb-book
root: index
options:
 numbered: 2
chapters: """
print("Scanning root directory for chapters...")
folders = {folder.path:{} for folder in os.scandir("./py_tutorial/") if folder.name not in ["_build"] and folder.is_dir()}

print("Directory scanned.\nScanning for sections...")
for folder in folders:
    folders[folder] = [c_folder.path.replace("\\","/") for c_folder in os.scandir(folder) if c_folder.name not in ["_build"] and c_folder.is_dir()] # type: ignore
 
print("Sections scanned.\nBuilding toc...\n")
for folder in sorted(folders.keys(), key=chapter_sort_key):

    print(f"Adding chapter {(chapter_num := chapter_sort_key(folder))}: ({folder})")
    chapter = f"\n - file: {folder[14:]}/index"

    if folders[folder]:
        print("Sections available for chapter, adding sections...")
        chapter += "\n   sections:"

        for section in sorted(folders[folder], key = section_sort_key):
            print(f"\tAdding section {chapter_num}.{section_sort_key(section)}: ({section})")
            chapter += f"\n   - file: {section[14:]}/index"
            
    print("Chapter added to toc\n")
    toc += chapter

print("toc built.")
print(*map(lambda x: ">>> " + x,toc.splitlines(keepends=True)))
print("Removing old _toc.yml")
os.remove("./py_tutorial/_toc.yml")
print("Removed.\nCreating new _toc.yml...")
with open("./py_tutorial/_toc.yml",'x') as file:
    file.write(toc)
    print("File created")