import numpy as np
import os
import os.path

from rechtschreib import correct

folder="../../write/data/"
folder="../../pre/data/"


for dirpath, dirnames, filenames in os.walk(folder):
  for filename in [f for f in filenames]:
    os.system("notepad++ "+dirpath+"/"+filename)
