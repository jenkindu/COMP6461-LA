import unittest
import sys
sys.path.extend(["../"])
from LA1.http import http


class TestHTTPMethods(unittest.TestCase):

    def test_get(self):
        h = http("http://localhost", 8080)
        h.setType('get')
        h.constructContent()
        reply = h.send()
        self.assertEqual(reply.state, '200')

    def test_get_file(self):
        h = http("http://localhost/foo", 8080)
        h.setType('get')
        h.constructContent()
        reply = h.send()
        self.assertEqual(reply.state, '200')

    def test_get_no_file(self):
        h = http("http://localhost/foo_no", 8080)
        h.setType('get')
        h.constructContent()
        reply = h.send()
        self.assertEqual(reply.state, '404')

    def test_post_request(self):
        body = '{"Assignment":"2", "name":"bar"}'
        h = http("http://localhost/bar", 8080)
        h.setType('post')
        h.setData(body)
        h.addHeader("Content-Type", "application/json")
        h.addHeader("Content-Length",str(len(body)))
        h.constructContent()
        reply = h.send()
        print(reply.headMap)
        print(reply.body)
        self.assertEqual(reply.state, '200')
        
if __name__ == '__main__':
    unittest.main()