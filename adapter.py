import json 
import xml.etree.ElementTree as ET

class JSONHandler:
    def read_json(self, path):
        with open(path, "r") as f:
            data = json.load(f)
        return data
    
    def write_json(self, path, data):
        with open(path, "w") as f:
            json.dump(data, f)
        
class XMLHandler:
    def _xml_to_dict(self, root):
        return {
            root.tag: {
                child.tag: child.text
                for child in root
            }
        }
    
    def _dict_to_xml(self,tag, data):
        root = ET.Element(tag)
        for key, value in data.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        return root
   
    

    def read_xml(self, path):
        tree = ET.parse(path)
        root = tree.getroot()
        return self._xml_to_dict(root)
    
    def write_xml(self, path, data):
        root = self._dict_to_xml("root", data)
        tree = ET.ElementTree(root)
        tree.write(path, encoding="utf-8", xml_declaration=True)

class FileAdapter:
    def __init__(self, handler, type):
        self.handler = handler
        self.type = type
    
    def read(self, path):
        if self.type == "json":
            return self.handler.read_json(path)
        elif self.type == "xml":
            return self.handler.read_xml(path)
        else:
            raise ValueError("Format not supported")

data ={
    "nombre": "Juan Perez",
    "edad": 30,
    "ciudad": " Quito"
}

json_adapter = FileAdapter(JSONHandler(), "json")
json_adapter.handler.write_json("data.json", data)
print("JSON data", json_adapter.read("data.json"))

xml_adapter = FileAdapter(XMLHandler(), "xml")
xml_adapter.handler.write_xml("data.xml", data)
print("XML data", xml_adapter.read("data.xml"))
   