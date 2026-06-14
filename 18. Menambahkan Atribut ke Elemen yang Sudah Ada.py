from xml.dom import minidom

xml_data = '''<root>
    <child>Content 1</child>
</root>'''

dom = minidom.parseString(xml_data)
child = dom.getElementsByTagName('child')[0]
child.setAttribute('id', '1')  # Menambahkan atribut baru
print(child.toxml())  # Menampilkan elemen child setelah penambahan atribut
# Fungsi: Menambahkan atribut baru ke elemen XML yang sudah ada.
# Kondisi: Ketika Anda butuh mengelola informasi tambahan di elemen XML.