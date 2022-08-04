# Heroes-and-Villains

As a developer, I want to make good, consistent commits. 

As a developer, I want to register the SuperType model with the admin site so I can:
Register a new super user (python manage.py createsuperuser)
Visit the admin site
Seed two values (“Hero” and “Villain”) into the “super_type” table

As a developer, I want my API to serve the “supers” app’s content on the following urls paths:
Paths must match these exactly!
‘127.0.0.1:8000/api/supers/' - optional params
‘127.0.0.1:8000/api/supers/<int:pk>/’



As a developer, I want to create a GET endpoint the responds with a 200 success status code and all of the supers within the supers table.
This view function should be implemented in a way to accept a “type” parameter
Example: " http://127.0.0.1:8000/api/supers?type=hero”
If a type query parameter is sent to the view function with the value of “hero”, the view function response should be a list of all supers that are associated with the type of “Hero” (Shown in End Result Overview video on portal)
If a type query parameter is sent to the view function with the value of “villain”, the view function response should be a list of all supers that are associated with the type of “Villain” (Shown in End Result Overview video on portal)
If no type query parameter is sent, return a custom dictionary response with a “heroes” key set equal to a list of supers of type “Hero” and a “villains” key set equal to a list of supers of type “Villain” (Shown in End Result Overview video on portal)
Custom_response = {“heroes” = [], “villains” = []}
