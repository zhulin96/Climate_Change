import requests
import xarray as xr

#define the parameters
server = "https://esgf-data.dkrz.de/esg-search/search"
key_setting = {
    "format": "application%2Fsolr%2Bjson",
    "distrib": False,
    "type": "Dataset",
    "limit": 100,
    "offset": 0
}
searching_variable_setting = {
    "project": "CMIP6",
    "table_id": "Amon",
    "experiment_id": "ssp585",
    "source_id": "TaiESM1",
    "institution_id": "AS-RCEC",
    "variant_label": "r1i1p1f1",
    "variable_id": "sfcWind",
    "grid_label": "gn",
    "version" : 20200901
}

url_keys = []
searching_variables = []
for k in key_setting:
    url_keys += ["{}={}".format(k, key_setting[k])]
for v in searching_variable_setting:
    searching_variables += ["{}={}".format(v, searching_variable_setting[v])]
url = "{}/?{}&{}".format(server,"&".join(searching_variables), "&".join(url_keys))

client = requests.session()
r = client.get(url)
r.raise_for_status()
response = r.json()["response"]

numFound = int(response["numFound"])
docs = response["docs"]
all_files = []
for d in docs:
    if "url" in d.keys():
        url = d["url"]
        for f in d["url"]:
            sp = f.split("|")
            all_files.append(sp[0].split(".html")[0])
print(all_files)
