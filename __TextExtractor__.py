from os import remove
from sqlite3 import connect
from xml.dom.minidom import Text


class xmlExtractor:
    def __init__(self, path, target_list):
        import xml.dom.minidom as minidom
        xml_file = minidom.parse(path)
        TextValue = xml_file.getElementsByTagName('TextValue')
        Old_ID_List = []

        for elem in TextValue:
            Old_ID = str(elem.attributes['TextID'].value)
            Old_ID_List.append(Old_ID)

        target_list.append(Old_ID_List)

class xmlExtractorFull:
    def __init__(self, path, target_list_IDs, target_list_Text):
        import xml.dom.minidom as minidom
        xml_file = minidom.parse(path)
        TextValue = xml_file.getElementsByTagName('TextValue')
        Old_ID_List = []
        Old_Text_List = []

        for elem in TextValue:
            if str(elem.attributes['TextID'].value).isspace() == False:
                try:
                    Old_Text = elem.firstChild.nodeValue
                    Old_Text_List.append(Old_Text)
                    Old_ID = elem.attributes['TextID'].value
                    Old_ID_List.append(Old_ID)
                except:
                    print("There's a problem with Readin TextValues in current XML File ", str(elem.attributes['TextID'].value))
                    Old_Text_List.append("Wrong Text Value!!!")

        target_list_IDs.append(Old_ID_List)
        target_list_Text.append(Old_Text_List)
        
class xmlGenerator:
    def __init__(self, root, current_language, attributeList, commonList, textList, save_path_file):
        xml = root.createElement('Texts') 
        xml.setAttribute('TextLanguage', current_language)
        root.appendChild(xml)

        for x in range(0,len(attributeList)):
            if str(attributeList[x]) not in commonList:
                productChild = root.createElement('TextValue')
                attribute = str(attributeList[x]).replace('\n','&#xA;').replace('\r','&#xD;').replace('\t','&#x9;')
                productChild.setAttribute('TextID', attribute)

                text = root.createTextNode(str(textList[x]).replace("&quot;",'"'))
                productChild.appendChild(text)
                xml.appendChild(productChild)
            
        xml_str = root.toprettyxml(indent ="  ", newl='\n', encoding="utf-8")
        import os
        
        try:
            with open(save_path_file, "wb") as f:
                f.write(xml_str)
        except:
            temp_save_path_file = save_path_file.split('\ '.replace(' ',''))[:-1]
            temp_save_path_file = '/'.join(temp_save_path_file)
            print(temp_save_path_file)
            os.makedirs(temp_save_path_file)
            with open(save_path_file, "wb") as f:
                f.write(xml_str)

        content = []
        with open(save_path_file, "r", encoding='utf-8') as file:
            content_test = file.readlines()
        
        with open(save_path_file, "w", encoding='utf-8') as f:
            for line in content_test:
                contetnForAll = line.replace('&amp;#xA;','&#xA;').replace('&amp;#xD;','&#xD;').replace('&amp;#x9;','&#x9;')
                contetnForTextOnly = contetnForAll[int(contetnForAll.find(">") + len(">")):int(contetnForAll.find("</TextValue>"))].replace("&quot;",'"')
                if "TextID" in str(contetnForAll):
                    content = "".join(contetnForAll[:int(contetnForAll.find(">"))+1] + contetnForTextOnly + "</TextValue>\n")
                else:
                    content = "".join(contetnForAll)
                f.write(content)

        
