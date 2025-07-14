
KPA Wheel Specification API Assignment
By Sirjan Murmu

This project implements two REST API endpoints using Django REST Framework and PostgreSQL. The endpoints allow users to submit and retrieve wheel specification form data, as specified in the SwaggerHub API documentation.

Features Implemented
---------------------
1. Create Wheel Specification
   - Endpoint: POST /api/forms/wheel-specifications/create/
   - Description: Stores a new wheel specification form in the database.
   - Request Type: JSON
   - Status Code: 201 Created

2. Get All Wheel Specifications
   - Endpoint: GET /api/forms/wheel-specifications/
   - Description: Returns all saved wheel specs as a JSON array.
   - Status Code: 200 OK

Tech Stack
-----------
- Language: Python 3.x
- Framework: Django, Django REST Framework
- Database: PostgreSQL
- API Tool: Postman (Collection v2.1)
- Server: Django Dev Server (localhost:8000)

Setup Instructions
-------------------
1. Clone the Repo
   git clone https://github.com/your-username/kpa-wheel-api.git
   cd kpa-wheel-api

2. Create a Virtual Environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
   pip install -r requirements.txt

4. Configure PostgreSQL in settings.py
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'kpa_db',
           'USER': 'postgres',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }

5. Run Migrations
   python manage.py makemigrations
   python manage.py migrate

6. Start Server
   python manage.py runserver

Test API with Postman
-----------------------
Import the Postman Collection: kpa-assignment-sirjan-murmu.postman_collection.json

POST Request:
URL: http://127.0.0.1:8000/api/forms/wheel-specifications/create/
Body:
{
  "axleBoxHousingBoreDia": "156.1",
  "bearingSeatDiameter": "205.0",
  "condemningDia": "172.3",
  "intermediateWP": "180.7",
  "lastShopIssueSize": "179.6",
  "rollerBearingBoreDia": "92.0",
  "rollerBearingOuterDia": "194.0",
  "rollerBearingWidth": "54.7",
  "treadDiameterNew": "843.5",
  "variationSameAxle": "2.4",
  "variationSameBogie": "3.3",
  "variationSameCoach": "4.5",
  "wheelDiscWidth": "103.0",
  "wheelGauge": "1679",
  "wheelProfile": "Reinforced",
  "formNumber": "WS-2025-006",
  "submittedBy": "Pooja Sharma",
  "submittedDate": "2025-07-08"
}

GET Request:
URL: http://127.0.0.1:8000/api/forms/wheel-specifications/

Video Demonstration
---------------------
Features & Walkthrough: [INSERT LINK]
API Demo in Postman: [INSERT LINK]

Submission Package
-------------------
- README.txt
- Django Project Code
- Postman Collection (v2.1)
- Video Demo Links
- Tested APIs (POST + GET)

Limitations & Notes
---------------------
- No authentication layer implemented
- All fields are required
- No pagination or filtering
- Deployment not configured

Author
--------
Sirjan Murmu
Email: your-email@example.com
GitHub: https://github.com/your-username
