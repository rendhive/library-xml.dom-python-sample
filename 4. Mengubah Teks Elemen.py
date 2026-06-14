from xml.dom import minidom

xml_data = '''<root>
    <child>Old Content</child>
</root>'''

dom = minidom.parseString(xml_data)
child = dom.getElementsByTagName('child')[0]
child.firstChild.data = 'New Content'  # Mengubah isi elemen child
print(dom.toxml())  # Menampilkan XML yang diubah kembali ke string
# Fungsi: Mengubah isi dari elemen dalam XML.
# Kondisi: Ketika Anda perlu memperbarui nilai yang sudah ada di struktur XML.