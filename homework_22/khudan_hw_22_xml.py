import xml.etree.ElementTree as ET

class XMLProcessor:
    def __init__(self):
        self.root = None

    def xml_to_string(self):
        if self.root is None:
            return ""
        return ET.tostring(self.root, encoding='utf-8').decode('utf-8')

    def string_to_xml(self, xml_string):
        self.root = ET.fromstring(xml_string)

    def perform_operation(self):
        # Приклад операції - зміна значень всіх елементів <example> на 'New Value'
        if self.root is None:
            return

        for element in self.root.iter('example'):
            element.text = 'New Value'

# Приклад використання класу
processor = XMLProcessor()

# Перетворення XML в рядок
xml = '''<root>
    <example>Value 1</example>
    <example>Value 2</example>
</root>'''
string_xml = processor.xml_to_string()
print(string_xml)  # Виведе порожній рядок, оскільки root ще не визначений

processor.string_to_xml(xml)

# Декодування рядка у XML
string_xml = '''<root>
    <example>New Value</example>
    <example>New Value</example>
</root>'''
processor.string_to_xml(string_xml)

# Виконання операції
processor.perform_operation()

# Перетворення XML в рядок після операції
string_xml = processor.xml_to_string()
print(string_xml)
