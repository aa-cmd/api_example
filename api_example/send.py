import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY3OTcyNjk0LCJqdGkiOiJlNGEyNDNjNzM1Zjk0NmNiYWMwZTAwMDlhM2U1ZTYwMiIsInVzZXJfaWQiOjF9.D-W2ahEVJ9nf8lRQt7ag7_aXkX3q2e-nM-e1aST-JqM'

r = requests.get('http://127.0.0.1:8000/paradigms', headers=headers)

print(r.text)