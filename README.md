# Google OAuth Authentication API

## Overview
This project provides an authentication system using Google OAuth to allow users to log in securely with their Google accounts. It integrates FastAPI, Pydantic, and MongoDB to handle user authentication, user data storage, and API endpoints.

## Features
- Google OAuth 2.0 authentication
- Secure access token exchange
- User information retrieval and storage in MongoDB
- Organazing the project organization

## Technologies Used
- **FastAPI**: Web framework for building APIs
- **Pydantic**: Data validation and settings management
- **MongoDB**: Database for user data storage

## API Endpoints
### 1. Generate Google Login URL
**Endpoint:** `GET /auth/google`
- Returns the Google OAuth login URL.

### 2. Handle Google OAuth Callback
**Endpoint:** `GET /auth/google/callback`
- Exchanges the authorization code for an access token.
- Retrieves user information and stores it in MongoDB.

## Project Structure
```
📂 google-auth-api
 ├── 📂 configs
 │   ├── db_conn.py
 ├── 📂 models
 │   ├── user_model.py
 ├── 📂 services
 │   ├── auth_service.py
 ├── 📂 storages
 │   ├── user_storage.py
 ├── 📂 routers
 │   ├── auth_router.py
 ├── .env
 ├── main.py
 ├── requirements.txt
 ├── README.md
```