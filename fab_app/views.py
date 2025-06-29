from flask_appbuilder import ModelView, expose, BaseView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from . import app_builder
from .models import MyModel


class MyModelView(ModelView):
    datamodel = SQLAInterface(MyModel)
    list_columns = ['name', 'description']
    show_columns = ['name', 'description']
    add_columns = ['name', 'description']
    edit_columns = ['name', 'description']


class CustomFabView(BaseView):
    route_base = "/custom_fab"

    @expose("/hello/")
    def hello_world(self):
        return "Hello from Custom FAB View!"

    @expose("/info/")
    def info_page(self):
        return "This is an info page from Flask-AppBuilder."


app_builder.add_view(MyModelView, "My Data", icon="fa-database", category="My FAB App")
app_builder.add_view(CustomFabView, "Custom FAB Endpoints", icon="fa-cube", category="My FAB App")

from flask_appbuilder.api import BaseApi, expose


class MyFabApi(BaseApi):
    resource_name = "myapi"

    @expose("/status")
    def get_status(self):
        return self.response(200, message="FAB API is up!")


app_builder.add_api(MyFabApi)

# Ensure models are imported for SQLA to pick them up
from . import models
