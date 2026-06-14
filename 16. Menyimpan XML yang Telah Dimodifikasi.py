from xml.dom import minidom

dom = minidom.Document()
root = dom.createElement('root')
dom.appendChild(root)

child = dom.createElement('child')
child.appendChild(dom.createTextNode('Content 1'))
root.appendChild(child)

# Simpan file XML ke disk
with open('output.xml', 'w') as f:
    f.write(dom.toxml())
# Fungsi: Menyimpan objek XML yang telah dimodifikasi ke dalam file.
# Kondisi: Ketika Anda ingin menyimpan hasil akhir pemrosesan XML ke dalam file.