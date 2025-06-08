
---

# Fitness Class Booking API

This is a simple Django REST API for a fitness studio.
People can **view available classes**, **book a class**, and **see their bookings** using this API.

🚀 Live demo: [https://p01--class-booking--q7xqfnhbd4ht.code.run](https://p01--class-booking--q7xqfnhbd4ht.code.run)

---


---

## API Endpoints

All endpoints are under:
`https://p01--class-booking--q7xqfnhbd4ht.code.run/api/`

---

### `GET /classes/`

Get a list of all upcoming fitness classes.



---

###  `POST /classes/`

Create a new fitness class. *(For admin usage)*

#### Sample Request:

```json
{
  "name": "Yoga",
  "datetime": "2025-06-12 17:30",
  "teacher": "Anjali Mehra",
  "total_slots": 15,
  "fees": 300
}
```

---

### `POST /book/`

Book a spot in a fitness class.

####  Sample Request:

```json
{
  "class_id": 1,
  "client_name": "Rajat Rawal",
  "client_email": "rajat@example.com",
  "phone_number": "9876543210"
}
```

#### Response Example:

```json
{
  "id": 2,
  "client_name": "Rajat Rawal",
  "client_email": "rajat@example.com",
  "booking_datetime": "2025-06-07T17:45:00Z",
  "phone_number": "9876543210"
}
```

---

### `GET /bookings/?email=rajat@example.com`

Get all bookings made by a specific email.

#### Response Example:

```json
[
  {
    "id": 2,
    "client_name": "Rajat Rawal",
    "client_email": "rajat@example.com",
    "booking_datetime": "2025-06-07T17:45:00Z",
    "phone_number": "9876543210"
  }
]
```

---

## Tech Used

* **Python**
* **Django + DRF**
* **SQLite (in-memory)**

---

## How to Run Locally

```bash
git clone https://github.com/yourusername/fitness-booking-api.git
cd fitness-booking-api

# Create virtual environment
python -m venv env
source env/bin/activate   # or env\Scripts\activate on Windows

# Install packages
pip install -r requirements.txt

# Run migrations and server
python manage.py migrate
python manage.py runserver
```

