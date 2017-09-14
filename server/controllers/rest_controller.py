import json
import webapp2
import google.auth.transport.requests
import requests_toolbelt.adapters.appengine

requests_toolbelt.adapters.appengine.monkeypatch()
HTTP_REQUEST = google.auth.transport.requests.Request()

# TODO(dlochrie): Provide a nice way of allowing arguments or a config file to provide allowed URLS.
ALLOWED_HOSTS = 'http://localhost:3000'

class RestHandler(webapp2.RequestHandler):
    def dispatch(self):
        """Middleware for all the routes."""
        super(RestHandler, self).dispatch()

    def SendUnauthorized(self):
        self.response.set_status(401)
        self.response.write('Unauthorized')

    def SendJson(self, r):
        self.response.headers['Access-Control-Allow-Origin'] = ALLOWED_HOSTS
        self.response.headers['content-type'] = 'text/plain'
        self.response.write(json.dumps(r))

    def SendNotFound(self):
        self.response.set_status(404)
