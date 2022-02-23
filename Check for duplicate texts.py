from typing import Type
import __TextExtractor__ as te
import os
breaker = False
howmany = int(input('Wie viele Alte XML Dateien möchtest du prüfen? '))

def DataFinder():

  path_parent = os.path.realpath(__file__)
  path_parent = path_parent.split('\ '.replace(' ',''))[:-1]
  global path_parent_absolute
  path_parent_absolute = ''
  for element in path_parent:
      path_parent_absolute = path_parent_absolute + str(element) + '\ '.replace(' ','')

  import shutil
  temp_save_path_file = path_parent_absolute + 'Vorbereitete XMLs'
  try:
    shutil.rmtree(temp_save_path_file)
  except:
    "Folder already didn't exist"

  
  Paths = []
  #Open text file with paths
  try:
    with open((path_parent_absolute+'Paths.txt'),'r', encoding='UTF-8') as pathFile:
        for paths in pathFile:
          Paths.append(paths.rstrip('\n').split('> ')[1])
  except:
    print("Path.txt is not existing in this path: ",str(path_parent_absolute+'Paths.txt'))

  #Search for old texts folders
  global Old_Texts_Folders
  Old_Texts_Folders = []
  from pathlib import Path
  try:
    for file in sorted(Path(Paths[1]).iterdir(), key=os.path.getmtime, reverse=True):
        d = os.path.join(Paths[1], file)
        if os.path.isdir(d):
            Old_Texts_Folders.append(d)
  except:
    print("There is no such a directory: ", str(Paths[1]))
    breaker = True
  Old_Texts_Folders = Old_Texts_Folders[0:howmany]

  print()
  print('Es werden XMLs aus folgende Pfade geprüft: ')
  for element in Old_Texts_Folders:
    print(element)
  print()

  #Search for current .xml files
  global Current_Texts_Files
  Current_Texts_Files = []
  global Language_List
  Language_List = []
  try:
    for file in os.listdir(Paths[0]):
      d = os.path.join(Paths[0], file)
      if '.xml' in d:
        Current_Texts_Files.append(d)
        if "_de" in d and "MEDAPS" not in d:
          Language_List.append('_de')
        if "_de" in d and "MEDAPS" in d:
          Language_List.append('MEDAPS_de')
        if "_en" in d:
          Language_List.append('_en')
        if "_es" in d:
          Language_List.append('_es')
        if "_fr" in d:
          Language_List.append('_fr')
        if "_it" in d:
          Language_List.append('_it')
        if "_ru" in d:
          Language_List.append('_ru')
        if "_zh" in d:
          Language_List.append('_zh')
    if len(Language_List) == 0:
      print("There is no Text-XML files in directory: ", str(Paths[0]))
      breaker = True
  except:
    print("There is no such a directory: ", str(Paths[0]))
    breaker = True

#Current XML files and folders with old XML files will be found
DataFinder()

def current_Texts_Extractor():

  Current_List_Temp_de = []
  Current_Text_List_Temp_de = []
  Current_List_Temp_de_MEDAPS = []
  Current_Text_List_Temp_de_MEDAPS = []
  Current_List_Temp_en = []
  Current_Text_List_Temp_en = []
  Current_List_Temp_es = []
  Current_Text_List_Temp_es = []
  Current_List_Temp_fr = []
  Current_Text_List_Temp_fr = []
  Current_List_Temp_it = []
  Current_Text_List_Temp_it = []
  Current_List_Temp_ru = []
  Current_Text_List_Temp_ru = []
  Current_List_Temp_zh = []
  Current_Text_List_Temp_zh = []
  
  for xml_file in Current_Texts_Files:
    if "_de" in str(xml_file) and "MEDAPS" not in str(xml_file):
      te.xmlExtractorFull(path=xml_file, target_list_IDs=Current_List_Temp_de, target_list_Text=Current_Text_List_Temp_de)
    if "_de" in str(xml_file) and "MEDAPS" in str(xml_file):
      te.xmlExtractorFull(path=xml_file, target_list_IDs=Current_List_Temp_de_MEDAPS, target_list_Text=Current_Text_List_Temp_de_MEDAPS)
    if "_en" in str(xml_file):
      te.xmlExtractorFull(path=xml_file, target_list_IDs=Current_List_Temp_en, target_list_Text=Current_Text_List_Temp_en)
    if "_es" in str(xml_file):
      te.xmlExtractorFull(path=xml_file, target_list_IDs=Current_List_Temp_es, target_list_Text=Current_Text_List_Temp_es)
    if "_fr" in str(xml_file):
      te.xmlExtractorFull(path=xml_file, target_list_IDs=Current_List_Temp_fr, target_list_Text=Current_Text_List_Temp_fr)
    if "_it" in str(xml_file):
      te.xmlExtractorFull(path=xml_file, target_list_IDs=Current_List_Temp_it, target_list_Text=Current_Text_List_Temp_it)
    if "_ru" in str(xml_file):
      te.xmlExtractorFull(path=xml_file, target_list_IDs=Current_List_Temp_ru, target_list_Text=Current_Text_List_Temp_ru)
    if "_zh" in str(xml_file):
      te.xmlExtractorFull(path=xml_file, target_list_IDs=Current_List_Temp_zh, target_list_Text=Current_Text_List_Temp_zh)

  if "_de" in Language_List:
    global Current_List_de
    Current_List_de = [item for sublist in Current_List_Temp_de for item in sublist]
    global Current_Text_List_de
    Current_Text_List_de = [item for sublist in Current_Text_List_Temp_de for item in sublist]
  if "MEDAPS_de" in Language_List:
    global Current_List_de_MEDAPS
    Current_List_de_MEDAPS = [item for sublist in Current_List_Temp_de_MEDAPS for item in sublist]
    global Current_Text_List_MEDAPS_de
    Current_Text_List_MEDAPS_de = [item for sublist in Current_Text_List_Temp_de_MEDAPS for item in sublist]
  if "_en" in Language_List:
    global Current_List_en
    Current_List_en = [item for sublist in Current_List_Temp_en for item in sublist]
    global Current_Text_List_en
    Current_Text_List_en = [item for sublist in Current_Text_List_Temp_en for item in sublist]
  if "_es" in Language_List:
    global Current_List_es
    Current_List_es = [item for sublist in Current_List_Temp_es for item in sublist]
    global Current_Text_List_es
    Current_Text_List_es = [item for sublist in Current_Text_List_Temp_es for item in sublist]
  if "_fr" in Language_List:
    global Current_List_fr
    Current_List_fr = [item for sublist in Current_List_Temp_fr for item in sublist]
    global Current_Text_List_fr
    Current_Text_List_fr = [item for sublist in Current_Text_List_Temp_fr for item in sublist]
  if "_it" in Language_List:
    global Current_List_it
    Current_List_it = [item for sublist in Current_List_Temp_it for item in sublist]
    global Current_Text_List_it
    Current_Text_List_it = [item for sublist in Current_Text_List_Temp_it for item in sublist]
  if "_ru" in Language_List:
    global Current_List_ru
    Current_List_ru = [item for sublist in Current_List_Temp_ru for item in sublist]
    global Current_Text_List_ru
    Current_Text_List_ru = [item for sublist in Current_Text_List_Temp_ru for item in sublist]
  if "_zh" in Language_List:
    global Current_List_zh
    Current_List_zh = [item for sublist in Current_List_Temp_zh for item in sublist]
    global Current_Text_List_zh
    Current_Text_List_zh = [item for sublist in Current_Text_List_Temp_zh for item in sublist]

def old_Texts_Extractor():

  Old_List_Temp_de = []
  Old_List_Temp_de_MEDAPS = []
  Old_List_Temp_en = []
  Old_List_Temp_es = []
  Old_List_Temp_fr = []
  Old_List_Temp_it = []
  Old_List_Temp_ru = []
  Old_List_Temp_zh = []
  Old_Texts_Files = []

  for folder in Old_Texts_Folders:
    try:
      for file in os.listdir(folder):
        d = os.path.join(folder, file)
        if '.xml' in d:
          Old_Texts_Files.append(d)
          for xml_file in Old_Texts_Files:
            if "_de" in str(xml_file) and "MEDAPS" not in str(xml_file):
              te.xmlExtractor(path=xml_file, target_list=Old_List_Temp_de)
            if "_de" in str(xml_file) and "MEDAPS" in str(xml_file):
              te.xmlExtractor(path=xml_file, target_list=Old_List_Temp_de_MEDAPS)
            if "_en" in str(xml_file):
              te.xmlExtractor(path=xml_file, target_list=Old_List_Temp_en)
            if "_es" in str(xml_file):
              te.xmlExtractor(path=xml_file, target_list=Old_List_Temp_es)
            if "_fr" in str(xml_file):
              te.xmlExtractor(path=xml_file, target_list=Old_List_Temp_fr)
            if "_it" in str(xml_file):
              te.xmlExtractor(path=xml_file, target_list=Old_List_Temp_it)
            if "_ru" in str(xml_file):
              te.xmlExtractor(path=xml_file, target_list=Old_List_Temp_ru)
            if "_zh" in str(xml_file):
              te.xmlExtractor(path=xml_file, target_list=Old_List_Temp_zh)
    except:
      print('Unknown error')

  #Flatten the list and remove duplicated elements
  if "_de" in Language_List:
    global Old_List_de
    Old_List_de = [item for sublist in Old_List_Temp_de for item in sublist]
    Old_List_de = list(dict.fromkeys(Old_List_de))
  if "MEDAPS_de" in Language_List:
    global Old_List_de_MEDAPS
    Old_List_de_MEDAPS = [item for sublist in Old_List_Temp_de_MEDAPS for item in sublist]
    Old_List_de_MEDAPS = list(dict.fromkeys(Old_List_de_MEDAPS))
  if "_en" in Language_List:
    global Old_List_en
    Old_List_en = [item for sublist in Old_List_Temp_en for item in sublist]
    Old_List_en = list(dict.fromkeys(Old_List_en))
  if "_es" in Language_List:
    global Old_List_es
    Old_List_es = [item for sublist in Old_List_Temp_es for item in sublist]
    Old_List_es = list(dict.fromkeys(Old_List_es))
  if "_fr" in Language_List:
    global Old_List_fr
    Old_List_fr = [item for sublist in Old_List_Temp_fr for item in sublist]
    Old_List_fr = list(dict.fromkeys(Old_List_fr))
  if "_it" in Language_List:
    global Old_List_it
    Old_List_it = [item for sublist in Old_List_Temp_it for item in sublist]
    Old_List_it = list(dict.fromkeys(Old_List_it))
  if "_ru" in Language_List:
    global Old_List_ru
    Old_List_ru = [item for sublist in Old_List_Temp_ru for item in sublist]
    Old_List_ru = list(dict.fromkeys(Old_List_ru))
  if "_zh" in Language_List:
    global Old_List_zh
    Old_List_zh = [item for sublist in Old_List_Temp_zh for item in sublist]
    Old_List_zh = list(dict.fromkeys(Old_List_zh))

def file_comparison_engine():

  current_Texts_Extractor()
  old_Texts_Extractor()

  if "_de" in Language_List:
    global Common_IDs_de
    Common_IDs_de = list(set(Old_List_de).intersection(Current_List_de))
  if "MEDAPS_de" in Language_List:
    global Common_IDs_de_MEDAPS
    Common_IDs_de_MEDAPS = list(set(Old_List_de_MEDAPS).intersection(Current_List_de_MEDAPS))
  if "_en" in Language_List:
    global Common_IDs_en
    Common_IDs_en = list(set(Old_List_en).intersection(Current_List_en))
  if "_es" in Language_List:
    global Common_IDs_es
    Common_IDs_es = list(set(Old_List_es).intersection(Current_List_es))
  if "_fr" in Language_List:
    global Common_IDs_fr
    Common_IDs_fr = list(set(Old_List_fr).intersection(Current_List_fr))
  if "_it" in Language_List:
    global Common_IDs_it
    Common_IDs_it = list(set(Old_List_it).intersection(Current_List_it))
  if "_ru" in Language_List:
    global Common_IDs_ru
    Common_IDs_ru = list(set(Old_List_ru).intersection(Current_List_ru))
  if "_zh" in Language_List:
    global Common_IDs_zh
    Common_IDs_zh = list(set(Old_List_zh).intersection(Current_List_zh))

#Lists with current and old text-ids will be created and compared
file_comparison_engine()

def XML_files_creator():
  import xml.dom.minidom as minidom

  if '_de' in Language_List:
    rootde = minidom.Document()
    current_language = 'de'
    path_de = str(path_parent_absolute+'Vorbereitete XMLs\\Text_de.xml')
    te.xmlGenerator(root=rootde, current_language=current_language, attributeList=Current_List_de, commonList=Common_IDs_de, textList=Current_Text_List_de, save_path_file=path_de)

  if 'MEDAPS_de' in Language_List:
    rootdeMEDAPS = minidom.Document()
    current_language = 'de'
    path_de = str(path_parent_absolute+'Vorbereitete XMLs\\MEDAPSText_de.xml')
    te.xmlGenerator(root=rootdeMEDAPS, current_language=current_language, attributeList=Current_List_de_MEDAPS, commonList=Common_IDs_de_MEDAPS, textList=Current_Text_List_MEDAPS_de, save_path_file=path_de)

  if '_en' in Language_List:
    rooten = minidom.Document()
    current_language = 'de'
    path_en = str(path_parent_absolute+'Vorbereitete XMLs\\Text_Missing_en.xml')
    te.xmlGenerator(root=rooten, current_language=current_language, attributeList=Current_List_en, commonList=Common_IDs_en, textList=Current_Text_List_en, save_path_file=path_en)
  
  if '_es' in Language_List:
    rootes = minidom.Document()
    current_language = 'de'
    path_es = str(path_parent_absolute+'Vorbereitete XMLs\\Text_Missing_es.xml')
    te.xmlGenerator(root=rootes, current_language=current_language, attributeList=Current_List_es, commonList=Common_IDs_es, textList=Current_Text_List_es, save_path_file=path_es)
  
  if '_fr' in Language_List:
    rootfr = minidom.Document()
    current_language = 'de'
    path_fr = str(path_parent_absolute+'Vorbereitete XMLs\\Text_Missing_fr.xml')
    te.xmlGenerator(root=rootfr, current_language=current_language, attributeList=Current_List_fr, commonList=Common_IDs_fr, textList=Current_Text_List_fr, save_path_file=path_fr)
  
  if '_it' in Language_List:
    rootit = minidom.Document()
    current_language = 'de'
    path_it = str(path_parent_absolute+'Vorbereitete XMLs\\Text_Missing_it.xml')
    te.xmlGenerator(root=rootit, current_language=current_language, attributeList=Current_List_it, commonList=Common_IDs_it, textList=Current_Text_List_it, save_path_file=path_it)
  
  if '_ru' in Language_List:
    rootru = minidom.Document()
    current_language = 'de'
    path_ru = str(path_parent_absolute+'Vorbereitete XMLs\\Text_Missing_ru.xml')
    te.xmlGenerator(root=rootru, current_language=current_language, attributeList=Current_List_ru, commonList=Common_IDs_ru, textList=Current_Text_List_ru, save_path_file=path_ru)

  if '_zh' in Language_List:
    rootzh = minidom.Document()
    current_language = 'de'
    path_zh = str(path_parent_absolute+'Vorbereitete XMLs\\Text_Missing_zh.xml')
    te.xmlGenerator(root=rootzh, current_language=current_language, attributeList=Current_List_zh, commonList=Common_IDs_zh, textList=Current_Text_List_zh, save_path_file=path_zh)

XML_files_creator()

def infoEngine():
  if '_de' in Language_List:
    print('IDs, die in alten und neuen DE XML-Dateien verwendet werden: ')
    for element in Common_IDs_de:
      print(element)
    print()
  if 'MEDAPS_de' in Language_List:
    print('IDs, die in alten und neuen MEDAPS DE XML-Dateien verwendet werden: ')
    for element in Common_IDs_de_MEDAPS:
      print(element)
    print()
  if '_en' in Language_List:
    print('IDs, die in alten und neuen EN XML-Dateien verwendet werden: ')
    for element in Common_IDs_en:
      print(element)
    print()
  if '_es' in Language_List:
    print('IDs, die in alten und neuen ES XML-Dateien verwendet werden: ')
    for element in Common_IDs_es:
      print(element)
    print()
  if '_fr' in Language_List:
    print('IDs, die in alten und neuen FR XML-Dateien verwendet werden: ')
    for element in Common_IDs_fr:
      print(element)
    print()
  if '_it' in Language_List:
    print('IDs, die in alten und neuen IT XML-Dateien verwendet werden: ')
    for element in Common_IDs_it:
      print(element)
    print()
  if '_ru' in Language_List:
    print('IDs, die in alten und neuen RU XML-Dateien verwendet werden: ')
    for element in Common_IDs_ru:
      print(element)
    print()
  if '_zh' in Language_List:
    print('IDs, die in alten und neuen ZH XML-Dateien verwendet werden: ')
    for element in Common_IDs_zh:
      print(element)
    print()

infoEngine()

input('Press ENTER to continue')