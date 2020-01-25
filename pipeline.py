import gzip
import shutil

# Unzips gzip files
with gzip.open('file.txt.gz', 'rb') as f_in:
    with open('file.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
