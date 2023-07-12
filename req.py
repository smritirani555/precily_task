import requests

url = 'http://localhost:8000/predict'

payload = {'text1': 'nuclear body seeks new tech .....', 'text2': 'terror suspects face arrest ....'}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=payload, headers=headers)

if response.status_code == 200:
    similarity_score = response.json()['similarity_score']
    print(f'Similarity score: {similarity_score}')
else:
    print(f'Error: {response.status_code}')
