import json
import webapp2
import google.auth.transport.requests
import requests_toolbelt.adapters.appengine

requests_toolbelt.adapters.appengine.monkeypatch()
HTTP_REQUEST = google.auth.transport.requests.Request()

HOSTS_ALLOWED = [
    'http://localhost:3000',
    'http://localhost:8080',
]

class RestHandler(webapp2.RequestHandler):
    def dispatch(self):
        """Middleware for all the routes."""
        super(RestHandler, self).dispatch()

    def SendUnauthorized(self):
        self.response.set_status(401)
        self.response.write('Unauthorized')

    def SendJson(self, r):
        # Prevent other apps from making requests to this server.
        headers = self.request.headers
        origin = headers.get('Origin')
        if origin in HOSTS_ALLOWED:
            self.response.headers['Access-Control-Allow-Origin'] = origin

        self.response.headers['content-type'] = 'text/plain'
        self.response.write(json.dumps(r))

    def SendNotFound(self):
        self.response.set_status(404)
