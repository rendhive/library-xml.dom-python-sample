from xml.dom import minidom

xml_data = '''<root>
    <child id="1">Content 1</child>
</root>'''

dom = minidom.parseString(xml_data)
child = dom.getElementsByTagName('child')[0]
child.setAttribute('name', 'Child 1')  # Menambahkan atribut baru
print(child.getAttribute('id'), child.getAttribute('name'))  # Mengambil atribut
# Fungsi: Menambahkan dan mengambil atribut dari elemen XML.
# Kondisi: Ketika Anda ingin mengelola informasi lebih banyak dalam elemen elemen XML.