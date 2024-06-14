def my_xml2dict(xml_filepath):
    """
    This function will open a given xml filepath, and returns a dictonary.
    Uses xmltodict (https://pypi.org/project/xmltodict/) to convert from xml 
    to dict.
    """
    
    import xmltodict
    
    # open the xml file and read
    with open(xml_filepath, 'r', encoding='utf-8') as file:
        xml_file = file.read()
        
    # use xmltodict to parse and convert to a dictonary
    return xmltodict.parse(xml_file)
        