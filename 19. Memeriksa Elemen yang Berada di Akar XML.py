from xml.dom import minidom

xml_data = '''<root>
    <child>Content 1</child>
    <child>Content 2</child>
</root>'''

dom = minidom.parseString(xml_data)
if dom.documentElement.tagName == 'root':
    print("Root element exists.")
# Fungsi: Memeriksa apakah elemen root ada di XML.
# Kondisi: Ketika Anda ingin memastikan bahwa struktur XML memiliki elemen tertentu.