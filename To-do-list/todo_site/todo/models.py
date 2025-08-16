from django.db import models
from django.utils import timezone



from django.db import models
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
# When you look at a list of items on your computer, you want to see names you understand, not just a bunch of technical code.

# The __str__ method is the rule that tells Django, "Whenever you need to show me one of my to-do items, use the title of that item as its name."

# It's like giving your database items a proper label so they're easy for you to read.


# The models.Model part means that the Todo class is inheriting from django.db.models.Model.
#  This is a special Django class that provides all the necessary functionality to interact with a database.
# By inheriting from models.Model, Todo becomes a Django model. It means that Django will automatically map this class to a 
# table in your database and manage CRUD (Create, Read, Update, Delete) operations for it.