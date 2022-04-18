import os
from glob import glob
from pathlib import Path
import shutil

root = r"D:\data\train"
des = r"D:\wandavision_data"

for text in glob(os.path.join(root, "*.txt")):
    name = Path(text).stem
    shutil.move(text, os.path.join(des, name+".txt"))
    if name == "classes":
        continue
    shutil.move(os.path.join(root, name+".jpg"),
                os.path.join(des, name+".jpg"))
