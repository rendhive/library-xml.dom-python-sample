from xml.dom import minidom

# Pastikan Anda memiliki file 'data.xml' di direktori yang sama
dom = minidom.parse('data.xml')
root = dom.documentElement
print(root.tagName)  # Menampilkan tag root
# Fungsi: Membaca dan mem-parsing file XML dari file eksternal.
# Kondisi: Ketika Anda ingin memproses data XML yang disimpan dalam file.