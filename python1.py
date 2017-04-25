#!/usr/bin/python

def get_filepaths(dir):

     file_paths = []
   
     for root, directories, files in os.walk(dir):
         for filename in files:
   
             filepath = os.path.join(root, filename)
             file_paths.append(filepath)

     return file_paths

