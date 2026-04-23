# Manufacturing Order & Production Management System

## Overview

This project is a backend-focused manufacturing system designed to manage the lifecycle of customer orders through production and inventory updates.

The system is inspired by ERP concepts but intentionally scoped to focus on core manufacturing workflows:

* Order management
* Production tracking
* Inventory synchronization

The goal of this project is to demonstrate strong backend engineering practices, including data modeling, state management, and business rule enforcement.

---

## Problem Statement

Small and medium-sized manufacturing businesses often require systems to:

* Track customer orders
* Manage production progress
* Maintain accurate inventory levels

Many existing ERP solutions are complex, expensive, and difficult to customize. This project explores a simplified, modular alternative focused on essential operations.

---

## Features

### Order Management

* Create and manage customer orders
* Track order status through defined lifecycle stages
* Support partial order fulfillment

### Production Management

* Create and manage production batches
* Track production progress at batch level
* Handle partial production scenarios

### Inventory Management

* Automatically update stock levels based on production output
* Maintain accurate product quantities

### Business Rule Enforcement

* Prevent invalid state transitions
* Ensure production does not exceed ordered quantities
* Maintain data consistency across modules

---

## System Architecture

This project follows a modular architecture:

* **Orders Module** → Handles customer orders and lifecycle
* **Production Module** → Manages production batches and execution
* **Inventory Module** → Tracks product stock levels

Detailed architecture documentation:

* `docs/architecture/` 

---

## Project Structure

```bash
manufacturing-system/
│
├── docs/                  # Project documentation
│   └── requirements/
│
├── backend/               # Django backend
│
├── frontend/              # Frontend 
│
├── tests/                 # Test suites
│
└── README.md
```

---

## Tech Stack

* **Backend:** Django, Django REST Framework
* **Database:** PostgreSQL
* **Testing:** Pytest / Django Test Framework
* **Version Control:** Git + GitHub

---

## Getting Started

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd manufacturing-system
```

### 2. Setup Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Environment Variables

Create a `.env` file based on:

```bash
.env.example
```

---

### 4. Run Migrations

```bash
python manage.py migrate
```

---

### 5. Start Development Server

```bash
python manage.py runserver
```

---

## API Documentation

API endpoints and usage will be documented in:

```
docs/api/
```

---

## Testing

Run backend tests:

```bash
pytest
```

Test strategy and cases will be documented in:

```
docs/testing/
```

---

## Current Status

🚧 In active development

* Requirements defined
* Backend architecture in progress

---

## Future Improvements

* Role-based access control enhancements
* Delivery and dispatch tracking
* Multi-warehouse support
* Offline-first capabilities
* Frontend dashboard

---

## Learning Objectives

This project is focused on:

* Designing scalable backend systems
* Implementing real-world business workflows
* Enforcing data integrity and constraints
* Writing testable and maintainable code

---

