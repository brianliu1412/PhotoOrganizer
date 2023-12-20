# Photo Importer


import PySimpleGUI as sg
import os
import sys
import shutil
from datetime import datetime
import calendar
import shutil

from pathlib import Path
import glob

from PIL import Image
from PIL.ExifTags import TAGS

today = datetime.now()



layout = [
     [
        sg.Text("SD Card Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDERIN-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Text("Export Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDEROUT-"),
        sg.FolderBrowse(),
    ],
    [ sg.Button("Continue", key="-CONTINUE-")]
]


# Create the window
window = sg.Window("Photo Importer", layout)

folderin, folderout = None, None



# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break
    
    if event == "-FOLDERIN-":
      folderin = values["-FOLDERIN-"]
      print(folderin)
    if event == "-FOLDEROUT-":
      folderout = values["-FOLDEROUT-"]
      print(folderout)

    if event == "-CONTINUE-":
       if folderin != None and folderout != None:
          print("Break")
          break
          

# print([os.path.join(dirpath,f) for (dirpath, dirnames, filenames) in os.walk(folderin) for f in filenames])

jpgs = [os.path.join(root, file)
        for root, dirs, files in os.walk(folderin)
        for file in files
        if (file.endswith('.JPG') or file.endswith('.jpg')) ]


curr_dir = ""
for jpg in jpgs:
  image = Image.open(jpg)
  exifdata = image.getexif()
  
  datetimedata = exifdata[306]

  date_format = '%Y:%m:%d %H:%M:%S'
  
  date_obj = datetime.strptime(datetimedata, date_format)

  year = str(date_obj.year)
  month = str(date_obj.month)
  day = str(date_obj.day)
  
  if os.path.isdir(folderout+'/'+year) != True:
    os.mkdir(folderout+'/'+year)
    try:
      os.mkdir(folderout+'/'+year)
    except FileExistsError as exists:
      print('Folder exists:', exists.filename)
      print('Using existing folder...')
  
  if os.path.isdir(folderout+'/'+year+'/'+year+'-'+month+'-'+day) != True:
    try:
      os.mkdir(folderout+'/'+year+'/'+year+'-'+month+'-'+day)
    except FileExistsError as exists:
      print('Folder exists:', exists.filename)
      print('Using existing folder...')


  print(f'Copying {len(jpgs)} JPG files to {folderout}')
  filepath = folderout+'/'+year+'/'+year+'-'+month+'-'+day
  print(jpg)
  print(filepath)
  name_arr = jpg.split('/') 
  name = name_arr[-1]
  final_path = filepath + '/' + name
  print(final_path)
  try:
      shutil.copyfile(jpg, final_path)
  except:
      print("Error") 

print('Finished!')





window.close()



