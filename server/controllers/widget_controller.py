import json

from server.models import widget_model as model
import rest_controller as rest


class All(rest.RestHandler):

    def get(self):
        widgets = model.All()
        self.SendJson(widgets)
