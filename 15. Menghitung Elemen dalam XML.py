from xml.dom import minidom

xml_data = '''<root>
    <child>Content 1</child>
    <child>Content 2</child>
    <child>Content 3</child>
</root>'''

dom = minidom.parseString(xml_data)
count = dom.getElementsByTagName('child').length
print(f"Number of child elements: {count}")
# Fungsi: Menghitung jumlah elemen berdasarkan tag di dalam XML.
# Kondisi: Ketika Anda ingin mengetahui berapa banyak elemen dengan tag tertentu tersedia.