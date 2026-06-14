from xml.dom import minidom

dom = minidom.Document()  # Membuat dokumen baru
root = dom.createElement('root')
dom.appendChild(root)

child = dom.createElement('child')
child.appendChild(dom.createTextNode('Content 1'))
root.appendChild(child)

print(dom.toxml())  # Mengonversi objek XML ke string
# Fungsi: Menambahkan elemen baru ke dalam struktur XML.
# Kondisi: Ketika Anda ingin membangun XML secara programatik.