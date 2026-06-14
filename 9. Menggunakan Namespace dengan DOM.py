from xml.dom import minidom

xml_data = '''<root xmlns:ns="http://example.com/ns">
    <ns:child>Content 1</ns:child>
</root>'''

dom = minidom.parseString(xml_data)
child = dom.getElementsByTagNameNS("http://example.com/ns", "child")[0]
print(child.firstChild.data)  # Mengambil konten di dalam elemen namespace
# Fungsi: Mengelola XML yang memiliki namespace menggunakan DOM.
# Kondisi: Ketika Anda bekerja dengan XML yang mengandung elemen namespace