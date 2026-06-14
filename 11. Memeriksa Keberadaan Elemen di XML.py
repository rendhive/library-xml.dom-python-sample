from xml.dom import minidom

xml_data = '''<root>
    <child>Content 1</child>
</root>'''

dom = minidom.parseString(xml_data)

if dom.getElementsByTagName('child'):
    print("Child element exists.")
else:
    print("Child element does not exist.")
# Fungsi: Memeriksa apakah elemen tertentu ada dalam XML atau tidak.
# Kondisi: Ketika Anda ingin memeriksa keberadaan elemen sebelum melakukan operasi lebih lanjut.