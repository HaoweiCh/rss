import xml.etree.ElementTree as ET


class AtomFeed:
    def __init__(self, id, title, updated, link_href, link_type='text/html', link_rel='alternate', lang='en-US'):
        self.root = ET.Element("feed")
        self.root.set('xmlns', 'http://www.w3.org/2005/Atom')
        self.root.set('xmlns:media', 'http://search.yahoo.com/mrss/')
        self.root.set('xml:lang', lang)

        id_elem = ET.SubElement(self.root, 'id')
        id_elem.text = id

        title_elem = ET.SubElement(self.root, 'title')
        title_elem.text = title

        updated_elem = ET.SubElement(self.root, 'updated')
        updated_elem.text = updated

        link1 = ET.SubElement(self.root, 'link')
        link1.set('type', link_type)
        link1.set('rel', link_rel)
        link1.set('href', link_href)

        link2 = ET.SubElement(self.root, 'link')
        link2.set('type', 'application/atom+xml')
        link2.set('rel', 'self')
        link2.set('href', 'https://github.com/FreshRSS/FreshRSS/releases.atom')

    def add_entry(self, id, updated, title, link, content, author_name, thumbnail_url="", thumbnail_height='30',
                  thumbnail_width='30'):
        entry_elem = ET.SubElement(self.root, 'entry')

        id_elem = ET.SubElement(entry_elem, 'id')
        id_elem.text = id

        updated_elem = ET.SubElement(entry_elem, 'updated')
        updated_elem.text = updated

        link_elem = ET.SubElement(entry_elem, 'link')
        link_elem.set('rel', 'alternate')
        link_elem.set('type', 'text/html')
        link_elem.set('href', link)

        title_elem = ET.SubElement(entry_elem, 'title')
        title_elem.text = title

        content_elem = ET.SubElement(entry_elem, 'content')
        content_elem.set('type', 'html')
        content_elem.text = content

        author_elem = ET.SubElement(entry_elem, 'author')
        name_elem = ET.SubElement(author_elem, 'name')
        name_elem.text = author_name

        if thumbnail_url:
            media_elem = ET.SubElement(entry_elem, '{http://search.yahoo.com/mrss/}thumbnail')
            media_elem.set('height', thumbnail_height)
            media_elem.set('width', thumbnail_width)
            media_elem.set('url', thumbnail_url)

    def __str__(self):
        return bytes(self).decode("utf8")

    def __bytes__(self):
        return ET.tostring(self.root, encoding='utf8', method='xml')

    def write_xml(self, filename):
        tree = ET.ElementTree(self.root)
        tree.write(filename)
