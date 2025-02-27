import json
import xml.etree.ElementTree as ET

class JSONHandler:
    def read_json(self, path):
        with open(path, "r") as f:
            data = json.load(f)
        return data
    
    def write_json(self, path, data):
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

class XMLHandler:
    def _xml_to_dict(self, root):
        return {
            root.tag: {
                child.tag: child.text
                for child in root
            }
        }
    
    def _dict_to_xml(self, tag, data):
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
        root = self._dict_to_xml("Paciente", data)
        tree = ET.ElementTree(root)
        tree.write(path, encoding="utf-8", xml_declaration=True)

class FileAdapter:
    def __init__(self, handler, file_type):
        self.handler = handler
        self.file_type = file_type
    
    def read(self, path):
        if self.file_type == "json":
            return self.handler.read_json(path)
        elif self.file_type == "xml":
            return self.handler.read_xml(path)
        else:
            raise ValueError("Formato no soportado")

    def write(self, path, data):
        if self.file_type == "json":
            self.handler.write_json(path, data)
        elif self.file_type == "xml":
            self.handler.write_xml(path, data)
        else:
            raise ValueError("Formato no soportado")

paciente_data = {
    "nombre": "Ana Gómez",
    "edad": "45",
    "diagnóstico": "Hipertensión",
    "tratamiento": "Medicamento A",
    "doctor": "Dr. Martínez"
}

json_adapter = FileAdapter(JSONHandler(), "json")
json_adapter.write("paciente.json", paciente_data)
print("Datos en JSON:", json_adapter.read("paciente.json"))

xml_adapter = FileAdapter(XMLHandler(), "xml")
xml_adapter.write("paciente.xml", paciente_data)
print("Datos en XML:", xml_adapter.read("paciente.xml"))
