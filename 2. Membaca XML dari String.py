from xml.dom import minidom

xml_data = '''<root>
    <child>Content 1</child>
    <child>Content 2</child>
</root>'''

dom = minidom.parseString(xml_data)
print(dom.documentElement.tagName)  # Menampilkan nama tag root
# Fungsi: Membaca dan mem-parsing file XML sederhana dari string.
# Kondisi: Ketika Anda ingin mulai dengan data XML dalam format string.