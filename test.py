#!/usr/bin/python3
import xml.etree.ElementTree as ET
import json

data_file = "data.xml"


def scrap_data(context=None, event=None):
    data = []
    for event, elem in ET.iterparse(data_file):
        for meps in elem.findall(".//mep"):
            full_name = meps.find(".//fullName").text
            political_group = meps.find(".//politicalGroup").text
            country = meps.find(".//country").text
            id = meps.find(".//id").text
            national_political_group = meps.find(".//nationalPoliticalGroup").text

            data.append(
                {
                    "fullName": full_name,
                    "country": country,
                    "politicalGroup": political_group,
                    "id": id,
                    "nationalPoliticalGroup": national_political_group,
                }
            )
    return data
