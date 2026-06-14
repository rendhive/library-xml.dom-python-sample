from xml.dom import minidom

xml_data = '''<root>
    <child>Content 1</child>
    <child>Content 2</child>
</root>'''

dom = minidom.parseString(xml_data)
children = dom.getElementsByTagName('child')
for child in children:
    print(child.firstChild.data)  # Mengakses teks dari setiap elemen child
# Fungsi: Mengakses isi teks dari elemen.
# Kondisi: Ketika Anda ingin mendapatkan data yang tersimpan dalam elemen tertentu.