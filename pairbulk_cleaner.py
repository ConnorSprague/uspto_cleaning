# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
import pandas as pd
from flatten_json import flatten
import numpy as np
from os import listdir
from os.path import isfile, join

filepath = "pairbulkdata"
onlyfiles = [f for f in listdir(filepath) if isfile(join(filepath, f))]
onlyfiles.sort()
df = {}
counter = 0
for fname in onlyfiles:
    path = 'pairbulkdata/' + fname
    #path = 'pairbulkdata/1970.json'
    json1_file = open(path)
    json1_str = json1_file.read()
    json_file = json.loads(json1_str)
    json_dict = json_file["PatentBulkData"]
    dic_flattened = (flatten(d) for d in json_dict)
    inter_df = pd.DataFrame(dic_flattened)
    #Columns to keep; expiration date, entity size, application date, title, grant date, patent #, uspto link
    inter_df = inter_df[['applicationDataOrProsecutionHistoryDataOrPatentTermData_0_applicationStatusDate',
                         'applicationDataOrProsecutionHistoryDataOrPatentTermData_0_businessEntityStatusCategory',
                         'applicationDataOrProsecutionHistoryDataOrPatentTermData_0_filingDate',
                         'applicationDataOrProsecutionHistoryDataOrPatentTermData_0_inventionTitle_content_0',
                         'applicationDataOrProsecutionHistoryDataOrPatentTermData_0_patentGrantIdentification_grantDate',
                         'applicationDataOrProsecutionHistoryDataOrPatentTermData_0_patentGrantIdentification_patentNumber',
                         'applicationDataOrProsecutionHistoryDataOrPatentTermData_2_grantPublication_webURI']]
    df[fname] = inter_df
    counter += 1
    #break for my poor computer
    if counter == 5:
        break

master_df = pd.concat(df.values(), ignore_index=True)