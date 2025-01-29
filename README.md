

# HNG Stage 0 Backend Task

This is a Django-based API developed as part of the HNG Stage 0 Backend Task. The API returns basic information in JSON format, including the registered email address, the current datetime in ISO 8601 format (UTC), and the GitHub URL of the project's codebase.

---

## **Table of Contents**
1. [Project Description](#project-description)
2. [Setup Instructions](#setup-instructions)
3. [API Documentation](#api-documentation)
4. [Testing the API](#testing-the-api)
5. [Response Time Testing](#response-time-testing)
6. [Backlinks](#backlinks)


---

## **Project Description**

The goal of this project is to develop a public API that returns the following information in JSON format:
- **Email**: The registered email address used to sign up for the HNG12 Slack workspace.
- **Current Datetime**: The current datetime in ISO 8601 format (UTC).
- **GitHub URL**: The URL of the GitHub repository hosting the project's codebase.

The API is built using **Python** and **Django** and is designed to be fast, with a response time of less than **500ms**.

---

## **Setup Instructions**

Follow these steps to set up and run the project locally:

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo


2. **Create a Virtual Environment**:
        python -m venv venv
        source venv/bin/activate  # On Linux/Mac
        venv\Scripts\activate     # On Windows

3. **Install Dependencies**:
    pip install -r requirements.txt


4. **Run Migrations**:
    python manage.py migrate

5. **Start the Development Server**:
    python manage.py runserver

6. **Access the API**:
    http://127.0.0.1:8000/api/





API Documentation
Endpoint
GET https://stageonepublicapi.onrender.com/api/

Request
No request body or parameters are required.

Response Format
The API returns a JSON response with the following fields:

{
  "email": "mrtemitopejoseph@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/Tjoseph-O/public_api_hng_stage0"
}

Fields Description
email: The registered email address used to sign up for the HNG12 Slack workspace.

current_datetime: The current datetime in ISO 8601 format (UTC).

github_url: The URL of the GitHub repository hosting the project's codebase.


**Testing the API**
4. Using a Browser
Open your browser and navigate to:
    http://127.0.0.1:8000/api/




Response Time Testing
To ensure the API has a fast response time (< 500ms), you can use tools like curl, Postman, or Python's requests library.

1. Using curl
Run the following command to measure the response time:
    curl -o /dev/null -s -w "Response Time: %{time_total}s\n" http://127.0.0.1:8000/api/
    Response Time: 0.000340s

### **Example Usage**
You can test the API using `curl`:
```bash
curl https://stageonepublicapi.onrender.com/api/

{
  "email": "mrtemitopejoseph@gmail.com",
  "current_datetime": "2025-01-29T00:02:04.561520+00:00",
  "github_url": "https://github.com/Tjoseph-O/public_api_hng_stage0"
}




## **Backlinks**
- [HNG Python Developers](https://hng.tech/hire/python-developers)
- [HNG C# Developers](https://hng.tech/hire/csharp-developers)
- [HNG Golang Developers](https://hng.tech/hire/golang-developers)
- [HNG PHP Developers](https://hng.tech/hire/php-developers)
- [HNG Java Developers](https://hng.tech/hire/java-developers)
- [HNG Node.js Developers](https://hng.tech/hire/nodejs-developers)