# Utility Script to Parse XML filesself.

import xml.etree.ElementTree as et
import argparse
import os
import pandas as pd

#xtree = et.parse('student_details.xml')

def xml_parser(xml_file):
    """
    Function to parse a simple XML file into a Pandas Dataframe
    """
    xtree = et.parse(xml_file)
    xroot = xtree.getroot()

    cols = ['name','email','grade','age']
    out_dataframe = pd.DataFrame(columns = cols)

    for node in xroot:
        res = []
        res.append(node.attrib.get(cols[0]))
        for element in cols[1:]:
            if node is not None and node.find(element) is not None:
                res.append(node.find(element).text)
            else:
                res.append(None)

        out_dataframe = out_dataframe.append(pd.Series(res, index = cols), ignore_index = True)
    return out_dataframe



def main(xml_file):
    xml_file_path = os.path.join(os.getcwd(), xml_file)
    print("In the main function , The path location::", xml_file_path)
    extracted_dataframe = xml_parser(xml_file_path)
    print(extracted_dataframe)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-xml_file', help='Specify location of XML file')
    args = parser.parse_args()
    main(**vars(args))
