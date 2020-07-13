import requests

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open('crop.jpg', 'rb')},
    data={'size': 'auto','bg_image_url': 'https://www.vincentborrelli.com/pictures/113526_10.jpg?v=1563566253', 'add_shadow': true},
    headers={'X-Api-Key': 'RmmfVP6eQNFUGyjwtykypA7h'},
)
if response.status_code == requests.codes.ok:
    with open('no-bg.jpg', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)
