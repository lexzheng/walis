# coding=utf8
import json

headers = [('Content-Type', 'application/json')]


def test_get_event(web_client):
    response = web_client.get('/api/cs/event')
    events = json.loads(response.data)
    assert response.status_code == 200
    assert events['count'] >= 1
    assert len(events['events']) == events['count']
