from xml.dom import minidom

xml_data = '''<root>
    <child>Content 1</child>
    <child>Content 2</child>
</root>'''

dom = minidom.parseString(xml_data)
children = dom.getElementsByTagName('child')

for i in range(children.length):
    print(children.item(i).firstChild.data)
# Fungsi: Menggunakan DOM untuk mencetak semua konten dari elemen dengan tag tertentu.
# Kondisi: Ketika Anda ingin mencetak semua elemen dengan tag yang dijelaskan.