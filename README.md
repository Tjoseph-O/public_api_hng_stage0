

# HNG Stage 0 Backend Task

This is a Django-based API developed as part of the HNG Stage 0 Backend Task. The API returns basic information in JSON format, including the registered email address, the current datetime in ISO 8601 format (UTC), and the GitHub URL of the project's codebase.

---

## **Table of Contents**
1. [Project Description](#project-description)
2. [Setup Instructions](#setup-instructions)
3. [API Documentation](#api-documentation)
4. [Testing the API](#testing-the-api)
5. [Response Time Testing](#response-time-testing)


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
GET https://stageonepublicapi.onrender.com/

Request
No request body or parameters are required.

Response Format
The API returns a JSON response with the following fields:

{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}

Fields Description
email: The registered email address used to sign up for the HNG12 Slack workspace.

current_datetime: The current datetime in ISO 8601 format (UTC).

github_url: The URL of the GitHub repository hosting the project's codebase.


**Testing the API**
4. Using a Browser
Open your browser and navigate to:
    http://127.0.0.1:8000/




Response Time Testing
To ensure the API has a fast response time (< 500ms), you can use tools like curl, Postman, or Python's requests library.

1. Using curl
Run the following command to measure the response time:
    curl -o /dev/null -s -w "Response Time: %{time_total}s\n" http://127.0.0.1:8000/
    Response Time: 0.000340s




Backlinks
HNG Python Developers

HNG C# Developers

HNG Golang Developers

HNG PHP Developers

HNG Java Developers

HNG Node.js Developers