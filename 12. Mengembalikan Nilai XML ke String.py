from xml.dom import minidom

xml_data = '''<root>
    <child>Content 1</child>
</root>'''

dom = minidom.parseString(xml_data)
xml_string = dom.toxml()  # Mengonversi objek DOM ke string
print(xml_string)
# Fungsi: Mengonversi objek XML kembali ke string.
# Kondisi: Ketika Anda ingin mendapatkan representasi string dari DOM yang telah dimodifikasi.