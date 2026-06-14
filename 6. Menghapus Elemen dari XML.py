from xml.dom import minidom

xml_data = '''<root>
    <child>Content 1</child>
    <child>Content 2</child>
</root>'''

dom = minidom.parseString(xml_data)
child = dom.getElementsByTagName('child')[0]
child.parentNode.removeChild(child)  # Menghapus elemen child dari DOM

print(dom.toxml())  # Menampilkan XML yang diubah
# Fungsi: Menghapus elemen dari XML menggunakan DOM.
# Kondisi: Ketika Anda perlu memodifikasi struktur XML dengan penghapusan elemen.