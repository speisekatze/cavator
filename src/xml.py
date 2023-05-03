import xml.etree.ElementTree as ET

def load(data):
    tree = ET.parse('data/'+data+'.xml')
    return tree.getroot()

def lookup(law, para):
    root = load(law)
    el = root.findall(".//enbez/[.='§ "+para+"']/../..//Content")[0]
    result = ""
    for p in el:
        result += p.text + "\r\n"
        dt = p.findall('.//DT')
        dd = p.findall('.//DD')
        for num, text in zip(dt, dd):
            result += f"\t{num.text} {''.join(text.itertext())}" + "\r\n"
    return result
