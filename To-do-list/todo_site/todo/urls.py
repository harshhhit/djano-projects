from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('', views.index, name="todo"),
    path('del/<str:item_id>', views.remove, name="del"),
    path('admin/', admin.site.urls),
]


# The line of code path('del/<str:item_id>', views.remove, name="del") is like a rule for your website's address book.

# What's the rule?

# The rule says: "If someone visits an address that looks like /del/ followed by some text, I want to do something."

#     del/: This is a fixed part of the address. It tells the website what the user wants to do—in this case, "delete."

#     <str:item_id>: This is the important part. It's a placeholder for a specific item's ID.

#         str: This just means the ID is a string (a bunch of text).

#         item_id: This is the name we'll use to refer to that ID in our code.

# What happens when the rule is followed?

# When someone goes to an address like /del/123, the website finds this rule, grabs the 123, and hands it over to a specific function called views.remove.

# So, in simple terms, this line of code creates a dynamic "delete" link for every item on your list. The views.remove function then uses the item_id (like 123) to find and delete that specific item from your database.