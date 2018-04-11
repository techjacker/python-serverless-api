import requests


def test_post(server):
    with server.app_context():
        r = requests.post(server.url + '/artists', data={
            'name': 'a'
        })
        assert r.status_code == 200
        assert r.text == 'ok'


def test_get_many(server):
    r = requests.get(server.url + '/artists')
    assert r.status_code == 200
    items = r.json()
    assert items[0]['name'] == 'enya'
