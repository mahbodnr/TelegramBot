from Tbot.database import Database
from Tbot.types import User, Update

from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.pymongo import ModelView, filters
from wtforms import form, fields

print(User.__fields__)

database = Database()

app = Flask(__name__)

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

class UserForm(form.Form):
    for field in User.__fields__:
        exec(f"{field} = fields.TextField('{field}')")

class UserView(ModelView):
    column_list = list(User.__fields__.keys())
    form = UserForm

class UpdateForm(form.Form):
    for field in Update.__fields__:
        exec(f"{field} = fields.TextField('{field}')")

class UpdateView(ModelView):
    column_list = list(Update.__fields__.keys())
    form = UpdateForm

admin = Admin(
    app,
    name='Telegram Bot',
    # base_template='my_master.html',
    template_mode='bootstrap4',
)

# Add administrative views here
admin.add_view(UserView(database.users, 'User'))
admin.add_view(UpdateView(database.updates, 'Updates'))

app.run()