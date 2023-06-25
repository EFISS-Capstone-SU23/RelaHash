import pandas as pd
from tqdm.auto import tqdm
tqdm.pandas()
df = pd.read_csv('./data/shopee/database.txt', nrows=None, header=None, sep=' ')
# df = df.iloc[-1000:]
check = '/media/saplab/Data_Win/RSI_Do_An/AnhND/Dynamic-Crawler-Tool/output' + df[0].str[18:]
check
import os
mask = check.progress_apply(lambda x: os.path.isfile(x))
filtered = check[mask]
not_exist = check[~mask]
filtered
df.loc[filtered.index]
new_db = df.loc[filtered.index]
new_db[0] = filtered
new_db
import cv2
import numpy as np
import os
from PIL import Image
import shutil

#  mixed png, jpg, jpeg, webp, etc files. All files have been accidental renamed
#  to .jpeg. Rename them back to their original extension

def rename_path_to_original_extension(img_path):
    try:
        with Image.open(img_path) as img:
            img.verify()
            image_format = img.format.lower()
            new_filename = img_path.replace('.jpeg', f'.{image_format}')
            # os.rename(img_path, new_filename)
            shutil.move(img_path, new_filename)
            return new_filename
    except Exception as e:
        print(e)
        return None

new_db[0] = new_db[0].progress_apply(rename_path_to_original_extension)
extension = new_db[0].str.split('.').str[-1]
print(extension)
new_db.dropna(inplace=True)
new_db[0] = 'data/shopee' + new_db[0].str[59:]
new_db
new_db.to_csv('./data/shopee/database-filtered2.txt', header=None, index=None, sep=' ')
test_df = new_db.sample(1000)
test_df.to_csv('./data/shopee/test2.txt', header=None, index=None, sep=' ')