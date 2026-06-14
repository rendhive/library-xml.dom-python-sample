from xml.dom import minidom

dom = minidom.Document()
root = dom.createElement('root')
dom.appendChild(root)

child = dom.createElement('child')
child.appendChild(dom.createTextNode('content with spaces'))
root.appendChild(child)

xml_string = dom.toprettyxml(indent="  ")  # Menformat XML menjadi lebih rapi
print(xml_string)
# Fungsi: Menggunakan `toprettyxml` untuk menformat XML dan membuatnya lebih mudah dibaca.
# Kondisi: Ketika Anda ingin mengekspor atau mencetak XML secara rapi.