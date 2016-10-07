import os
from os import path

l_n = 3
t_n = 6


for a in range (1,l_n+1):

    newpath = 'D:\Python for QA\lesson' + str(a)
    if not os.path.exists(newpath):
        os.makedirs(newpath)


    for b in range (1,t_n+1):
        file_path = path.relpath(newpath + '\\' + 'task' + str (b) + '.py')
        f = open (file_path, 'w')



