

# Fitness Class Booking API


**Live Demo:**
[https://p01--class-booking--q7xqfnhbd4ht.code.run](https://p01--class-booking--q7xqfnhbd4ht.code.run)

---

## API Base URL

`https://p01--class-booking--q7xqfnhbd4ht.code.run/api/`

---

## API Endpoints

---

### GET /classes/

View all upcoming fitness classes.

**URL:**
`https://p01--class-booking--q7xqfnhbd4ht.code.run/api/classes/`

---

### POST /classes/

Add a new fitness class.

**URL:**
`https://p01--class-booking--q7xqfnhbd4ht.code.run/api/classes/`

**Example JSON:**

```json
{
  "name": "Yoga",
  "datetime": "2025-06-12 17:30",
  "teacher": "ABCD XYZ",
  "total_slots": 15,
  "fees": 300
}
```

---

### POST /book/

Book a class using its ID.

**URL:**
`https://p01--class-booking--q7xqfnhbd4ht.code.run/api/book/`

**Example JSON:**

```json
{
  "class_id": 1,
  "client_name": "Rajat Rawal",
  "client_email": "rwlrajat@gmail.com",
  "phone_number": "8624094055"
}
```

**Example Response:**

```json
{
  "id": 2,
  "client_name": "Rajat Rawal",
  "client_email": "rwlrajat@gmail.com",
  "booking_datetime": "2025-06-07T17:45:00Z",
  "phone_number": "8624094055"
}
```

---

### GET /bookings/?email=[your@email.com](mailto:your@email.com)

See all your bookings using your email.

**URL:**
`https://p01--class-booking--q7xqfnhbd4ht.code.run/api/bookings/?email=rwlrajat@gmail.com`

**Example Response:**

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

## Run Locally

```bash
git clone https://github.com/rajatrawal/fitness-booking-api.git
cd fitness-booking-api

# Create virtual environment
python -m venv env
env\Scripts\activate  # on Windows

# Install packages
pip install -r requirements.txt

# Migrate and run server
python manage.py migrate
python manage.py runserver
```


