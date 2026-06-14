from xml.dom import minidom

dom = minidom.Document()
root = dom.createElement('root')
dom.appendChild(root)

child = dom.createElement('child')
child.appendChild(dom.createTextNode('Content 1'))
root.appendChild(child)

with open('output.xml', 'w') as f:
    f.write(dom.toxml())  # Menyimpan XML ke file
# Fungsi: Menyimpan objek XML ke file di disk.
# Kondisi: Ketika Anda ingin menyimpan data XML yang telah dibangun selama pemrosesan.