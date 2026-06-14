from xml.dom import minidom

xml_data = '''<company>
    <employee>
        <name>John Doe</name>
        <position>Developer</position>
    </employee>
    <employee>
        <name>Jane Smith</name>
        <position>Manager</position>
    </employee>
</company>'''

dom = minidom.parseString(xml_data)
employees = dom.getElementsByTagName('employee')

for employee in employees:
    name = employee.getElementsByTagName('name')[0].firstChild.data
    position = employee.getElementsByTagName('position')[0].firstChild.data
    print(f"Name: {name}, Position: {position}")
# Fungsi: Mengelola struktur DOM yang lebih kompleks dengan nested elements.
# Kondisi: Ketika Anda bekerja dengan data XML yang mencakup elemen yang memiliki sub-elemen.