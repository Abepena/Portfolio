### THE MODEL

1. Go to models.py in your application directory
2. Write out your model class inheriting from the models.Model
3. Add in all the fields you would like your model to have
4. Give it a string representation if necessary using a `__str__` method

### MAKING IT ACCESSIBLE FROM THE ADMIN SITE

1. Add the app to settings.py app
2. Makemigrations now that your model has been created --> `python manage.py makemigrations`
3. Migrate after confirming that the migrations have been created and are ready to migrate to your db --> `python manage.py migrate`
4. Add your model to your admin.py file to have the newly migrated model and its corresponding fields show up on the admin panel as editable
