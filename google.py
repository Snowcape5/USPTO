import requests
import json

url = 'https://ped.uspto.gov/api/queries'

headers = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Headers": "*",
    "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
}


data = {
    'searchText': 'firstNamedApplicant:(Google)',
    'fq': ['appFilingDate:[2013-01-01T00:00:00Z TO 2014-01-31T23:59:59Z]', 'appStatus:"Patented Case"'],
    'fl': '*',
    'mm': '100%',
    'df': 'patentTitle',
    'qf': 'appEarlyPubNumber applId appLocation appType appStatus_txt appConfrNumber appCustNumber appGrpArtNumber appCls appSubCls appStatus_txt patentNumber patentTitle primaryInventor firstNamedApplicant appExamName appExamPrefrdName appAttrDockNumber appPCTNumber appIntlPubNumber wipoEarlyPubNumber pctAppType firstInventorFile appClsSubCls rankAndInventorsList',
    'facet': 'false',
    'sort': 'applId asc',
    'start': '0'
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.text)
