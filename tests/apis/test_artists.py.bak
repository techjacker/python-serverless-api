from urllib.parse import urlencode

import pytest
import requests

from app.models import Artist, db


def test_post(server):
    with server.app_context():
        assert Artist.query.count() == 0

        r = requests.post(server.url + '/artists', data={
            'name': 'a'
        })

        assert r.status_code == 200
        assert r.json()['name'] == 'a'

    with server.app_context():
        assert Artist.query.count() == 1
        artist = Artist.query.first()
        assert artist.name == 'a'


@pytest.mark.parametrize('data, status_code', [
    ({}, 422),
    ({'name': ''}, 422),
])
def test_post_errors(server, data, status_code):
    with server.app_context():
        assert Artist.query.count() == 0

        r = requests.post(server.url + '/artists', data=data)

        assert r.status_code == status_code
        assert Artist.query.count() == 0


def test_post_errors_on_unique(server):
    with server.app_context():
        artist = Artist('a')
        db.session.add(artist)
        db.session.commit()

        assert Artist.query.count() == 1

        r = requests.post(server.url + '/artists', data={'name': 'a'})

        assert r.status_code == 422
        assert Artist.query.count() == 1


def test_put(server):
    with server.app_context():
        artist = Artist('a')
        db.session.add(artist)
        db.session.commit()

        assert Artist.query.count() == 1

        r = requests.put(server.url + '/artists/{}'.format(artist.id), data={
            'name': 'b'
        })
        assert r.status_code == 200
        assert r.json()['name'] == 'b'

    with server.app_context():
        assert Artist.query.count() == 1
        artist = Artist.query.get(artist.id)
        assert artist.name == 'b'


def test_put_same_name(server):
    with server.app_context():
        artist = Artist('b')
        db.session.add(artist)
        db.session.commit()

        assert Artist.query.count() == 1

        r = requests.put(server.url + '/artists/{}'.format(artist.id), data={
            'name': 'b'
        })
        assert r.status_code == 200
        assert r.json()['name'] == 'b'

    with server.app_context():
        assert Artist.query.count() == 1
        artist = Artist.query.get(artist.id)
        assert artist.name == 'b'


def test_put_errors(server):
    with server.app_context():
        artist = Artist('a')
        db.session.add(artist)
        artist2 = Artist('b')
        db.session.add(artist2)
        db.session.commit()

        assert Artist.query.count() == 2

        r = requests.put(server.url + '/artists/{}'.format(artist.id), data={
            'name': 'b'
        })
        assert r.status_code == 422


def test_delete(server):
    with server.app_context():
        artist = Artist('a')
        db.session.add(artist)
        db.session.commit()

        assert Artist.query.count() == 1

        r = requests.delete(server.url + '/artists/{}'.format(artist.id))
        assert r.status_code == 204

    with server.app_context():
        assert Artist.query.count() == 0


def test_get_one(server):
    with server.app_context():
        artist = Artist('a')
        db.session.add(artist)
        db.session.commit()

        assert Artist.query.count() == 1

        r = requests.get(server.url + '/artists/{}'.format(artist.id))
        assert r.status_code == 200
        assert r.json()['name'] == artist.name


@pytest.mark.parametrize('arguments, names', [
    ({}, ['a', 'b', 'c']),
    ({'page': 1, 'per_page': 2}, ['a', 'b']),
    ({'page': 2, 'per_page': 2}, ['c']),
])
def test_get_many(server, arguments, names):
    with server.app_context():
        for name in ('a', 'b', 'c'):
            db.session.add(Artist(name))
        db.session.commit()

    r = requests.get(server.url + '/artists?{}'.format(urlencode(arguments)))
    assert r.status_code == 200
    items = r.json()
    assert len(items) == len(names)
    assert list(map(lambda x: x['name'], items)) == names
