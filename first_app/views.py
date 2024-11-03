from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contact(request):
    d = {
    "name": "Jane Doe",
    "email": "janedoe@example.com",
    "phone_numbers": ["123-456-7890", "098-765-4321"],  # Array of phone numbers
    "addresses": [  # Array of address objects (dictionaries)
        {
            "street": "123 Maple St",
            "city": "Springfield",
            "state": "IL",
            "zip_code": "62701"
        },
        {
            "street": "456 Oak St",
            "city": "Springfield",
            "state": "IL",
            "zip_code": "62702"
        }
    ]
}
    return render(request, 'first_app/contact.html',d)
def about(request):
    return render(request, 'first_app/about.html')
