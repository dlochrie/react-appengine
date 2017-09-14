import webapp2

from controllers import widget_controller

APP = webapp2.WSGIApplication([
    ('/rest/widgets/all', widget_controller.All),
], debug=True)
