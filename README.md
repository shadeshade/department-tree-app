#Setup/run instructions
###Run the following commands to get started

Make migrations:

```python manage.py migrate```

Create superuser:

```python manage.py createsuperuser```

Load initial data into db:

`python manage.py fill_db`

Run server:

`python manage.py runserver`

## GET api/v1/departments/tree-view/

+ ### Request
```
http://127.0.0.1:8000/api/v1/departments/tree-view/?page=3
```

* ### Response 200
```
{
    "1": {
            "name": "Department 1",
            "employees": {
                "count": 2000,
                "next": "http://127.0.0.1:8000/api/v1/departments/tree-view/?page=4",
                "previous": "http://127.0.0.1:8000/api/v1/departments/tree-view/?page=2",
                "results": [
                    {
                        "id": 1,
                        "name": "Kaitlin",
                        "surname": "Parks",
                        "patronymic": null,
                        "position": "Ranger/warden",
                        "salary": "69970.00"
                    },
            ...
            
                    {
                    "id": 8020,
                    "name": "Joseph",
                    "surname": "Wells",
                    "patronymic": null,
                    "position": "Retail manager",
                    "salary": "96929.00"
                }
            ]
        },
        "children_departments": {...}
    }
}
```

##Working with data
You can perform CRUD operations in admin panel

```http://127.0.0.1:8000/admin/```