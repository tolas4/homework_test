from jsonpath import jsonpath
from Common.func_rep_data import EnvData

def extract_data_from_res(data, res):
    data = eval(data)
    for key, value in data.items():
        value = str(jsonpath(res.json(), value)[0])
        setattr(EnvData, key, value)

# extract_data_from_res({"token":"$..token"}, {'id': 11, 'username': 'axmaki', 'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMSwidXNlcm5hbWUiOiJheG1ha2kiLCJleHAiOjE1OTc4MDY0NTgsImVtYWlsIjoiMjM1MjY2MjRAcXEuY29tIn0.bQd55V2uJutsqPfB64NgKGmnbEdjSisdbJ7W79ruyG4'}
# )
