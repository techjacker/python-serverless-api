import requests


def test_404(server):
    r = requests.get(server.url + '/not-found')
    assert r.status_code == 404
    data = r.json()
    assert 'error' in data
    assert 'Not found' in data['error']['message']


def test_405(server):
    r = requests.delete(server.url + '/artists')
    assert r.status_code == 405
    data = r.json()
    assert 'error' in data
    assert 'Method not supported' in data['error']['message']
