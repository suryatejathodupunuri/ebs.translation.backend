# EBS Translation Backend

This project provides a Flask-based API for translating text. It is designed to facilitate easy access to translation services for various Indian languages.
## Frontend

A frontend for this API is available at [EBS Translation Frontend](https://github.com/suryatejathodupunuri/ebs.translation.frontend). This frontend provides a user-friendly interface for interacting with the translation API, allowing users to easily input text and view results.

## Installation  
Follow these steps to set up the EBS Translation Backend on your local machine.

1. **Download Python and check the version:**
   - Ensure Python is installed and check the version:
     ```bash
     python --version
     ```

2. **Download Python, check the version and install mysql-connector-python:**
   - Ensure Python is installed,check the version and install mysql-connector-python:
     ```bash
     python --version
     pip install mysql-connector-python
     ```

3. **Clone the GitHub repository containing the backend code:**
   - Clone the repository:
     ```bash
     git clone https://github.com/suryatejathodupunuri/ebs.translation.backend
     ```

5. **Change to the cloned directory:**
   - Navigate into the cloned project directory:
     ```bash
     cd ebs.translation.backend
     ```
6. **Set up the database**
   - Modify the host,username and password in the code as per the deployed system
   - Create Database translation
     ```bash
     create database translation_db;
     ```
   - use translation database
     ```bash
     use translation_db;
     ```
    - create table translation
     ```bash
     CREATE TABLE translation (id INT AUTO_INCREMENT PRIMARY KEY, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, user VARCHAR(255) NOT NULL DEFAULT 'guest', src CHAR(3), tar CHAR(3), inp LONGTEXT, output LONGTEXT,ipaddress VARCHAR(255));
     ```

7. **Run the backend code:**
   - Start the backend server:
     ```bash
     python3 translation.py
     ```
## API Endpoints

### Transliterate Text

**Endpoint:** `/api/translation`

**Method:** `POST`

**Request Body:**

```json
{
  "src": "en",
  "tar": "te",
  "inp": "My dear countrymen, today I want to tell you all that together we will make our country strong. All your help is very much appreciated. We have to move on the path of progress together. Thank you"
}
```
**Response:**

```json
[
  {
    "output": "నా ప్రియమైన దేశవాసులారా, ఈ రోజు నేను మీ అందరికీ చెప్పాలనుకుంటున్నాను, కలిసి మన దేశాన్ని బలోపేతం చేస్తాం. మీరు చేసిన సాయానికి చాలా కృతజ్ఞతలు. మనం కలిసి పురోగతి మార్గంలో పయనించాలి. ధన్యవాదాలు."
  },
  {
    "status": "SUCCESS"
  }
]
```

### Test Endpoint

**Endpoint:** `/api/test`

**Method:** `GET`

**Description:** Checks if the backend server is running successfully.

**Response:** Backend Running Succesfully.

