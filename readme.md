# 📚 Student Management System – Django CRUD with SQLite3 & Tailwind CSS

A complete **CRUD (Create, Read, Update, Delete)** web application built with **Django** and **SQLite3**, styled with **Tailwind CSS**.  
This project manages student data (name and phone number) and serves as a clean starter for learning Django fundamentals.

---

## 📖 Table of Contents
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Setup & Installation](#-setup--installation)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Create and Activate Virtual Environment](#2-create-and-activate-virtual-environment)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Apply Migrations](#4-apply-migrations)
  - [5. Create a Superuser (Optional)](#5-create-a-superuser-optional)
  - [6. Run the Development Server](#6-run-the-development-server)
- [Project Structure](#-project-structure)
- [Code Explanation](#-code-explanation)
  - [Models – `students/models.py`](#models--studentsmodelspy)
  - [Forms – `students/forms.py`](#forms--studentsformspy)
  - [Views – `students/views.py`](#views--studentsviewspy)
  - [URLs – `students/urls.py`](#urls--studentsurlspy)
  - [Templates](#templates)
  - [Admin Registration – `students/admin.py`](#admin-registration--studentsadminpy)
- [How CRUD Works (Step‑by‑Step)](#-how-crud-works-stepbystep)
- [Accessing the Database](#-accessing-the-database)
  - [Django Admin Panel](#django-admin-panel)
  - [Django Shell](#django-shell)
  - [SQLite Command Line](#sqlite-command-line)
  - [DB Browser (GUI)](#db-browser-gui)
- [Future Enhancements](#-future-enhancements)
- [License](#-license)

---

## ✨ Features
- **Add** new students with name and phone number.
- **View** a list of all students in a responsive table.
- **View** detailed information of a single student.
- **Update** existing student information.
- **Delete** a student with confirmation.
- **Beautiful UI** with Tailwind CSS (no build step, CDN).
- **SQLite3** database – zero configuration, perfect for development.
- **Django Admin** integration for easy data management.

---

## 🛠 Tech Stack
- **Backend:** Django 4.x / 5.x (Python 3.8+)
- **Database:** SQLite3 (default, can be swapped)
- **Frontend:** Tailwind CSS (via CDN)
- **Templating:** Django’s built‑in template engine

---

## 🔧 Prerequisites
- Python 3.8 or higher installed ([python.org](https://python.org))
- `pip` (comes with Python)
- Basic familiarity with the command line / terminal

---

## ⚙️ Setup & Installation

Follow these steps to get the project running on your local machine.

### 1. Clone the Repository
```bash
git clone <repository-url>
cd student-management
