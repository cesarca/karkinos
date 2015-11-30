from lxml import etree
from lxml import objectify


class XmlParser:
    _FILES_DIR = "files/"
    _XSD_FILE = "extension_CCR.xsd"
    _CLINICAL_HISTORY_FILE = "HC.xml"

    def __init__(self):
        self.xsd = open(self._FILES_DIR + self._XSD_FILE)
        self.clinical_history = open(self._FILES_DIR + self._CLINICAL_HISTORY_FILE).read()
        self.xml_parser = self.build_xml_parser()

    def build_xml_parser(self):
        schema = etree.XMLSchema(file=self.xsd)
        return objectify.makeparser(schema=schema)

    def parse(self):
        return objectify.fromstring(self.clinical_history, self.xml_parser)
