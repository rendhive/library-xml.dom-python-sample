from xml.dom import minidom

xml_data = '''<config>
    <setting name="theme">dark</setting>
    <setting name="language">en</setting>
</config>'''

dom = minidom.parseString(xml_data)
theme = dom.getElementsByTagName('setting')[0]
print(f"Theme setting: {theme.firstChild.data}")
# Fungsi: Menggunakan XML untuk menyimpan data konfigurasi aplikasi.
# Kondisi: Ketika Anda ingin menggunakan XML sebagai sumber data yang terstruktur