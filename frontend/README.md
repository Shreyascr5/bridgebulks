# BridgeBulks

## Intelligent Vendor Selection & Bulk Procurement Optimization System

---

## Overview

BridgeBulks is a full-stack web application that optimizes bulk purchasing by automatically selecting the best vendor based on price, vendor rating, delivery time, and stock availability. The system helps customers reduce procurement costs and improve vendor selection using an intelligent scoring algorithm.

This project demonstrates supply chain optimization using a Multi-Criteria Decision Making (MCDM) algorithm.

---

## Tech Stack

| Layer            | Technology               |
| ---------------- | ------------------------ |
| Frontend         | React (Vite) + Bootstrap |
| Backend          | FastAPI (Python)         |
| Database         | PostgreSQL               |
| Cache            | Redis                    |
| Authentication   | JWT                      |
| Charts           | Chart.js                 |
| Containerization | Docker                   |

---

## System Architecture Diagram

            +------------------+
            |   React Frontend |
            |  (Vite + Bootstrap)
            +---------+--------+
                      |
                      |
                      v
            +------------------+
            |    FastAPI       |
            |     Backend      |
            +----+----+--------+
                 |    |
                 |    |
      +----------+    +-----------+
      |                           |
      v                           v

+------------------+ +------------------+
| PostgreSQL | | Redis |
| Database | | Cache |
+------------------+ +------------------+
|
v
+----------------------+
| Vendor Selection |
| Algorithm (MCDM) |
+----------------------+
|
v
+----------------------+
| Vendor Selection |
| Algorithm (MCDM) |
+----------------------+

---

## Vendor Selection Algorithm

The system selects the best vendor using a weighted scoring formula:
Score = (1 / Price) \* 0.5

- (Rating / 5) \* 0.3
- (1 / Delivery Days) \* 0.2

### Weight Distribution

| Factor        | Weight |
| ------------- | ------ |
| Price         | 50%    |
| Rating        | 30%    |
| Delivery Time | 20%    |

The vendor with the highest score is selected automatically.

Backend

The backend is built using FastAPI and provides:

JWT Authentication (Login & Register)
Vendor Management
Product Management
Vendor Inventory Management
Bulk Order Processing
Intelligent Vendor Selection Algorithm
Order Status Tracking
Vendor Rating System
Savings Calculation
Analytics Dashboard
Redis Caching

Backend URL:
http://127.0.0.1:8000

Swagger API Docs:
http://127.0.0.1:8000/docs

Frontend

The frontend is built using React (Vite) and provides:

Login & Registration
Dashboard with analytics charts
Bulk order creation
Order history tracking
Vendor inventory view
Vendor comparison page
Order status tracking
Vendor performance visualization

Frontend URL:
http://localhost:5173

Test Flow
Register a new user
Login
Add Vendors
Add Products
Vendors add Inventory (price, stock, delivery days)
Create Bulk Order
System selects best vendor automatically
View Comparison Page
View Savings
Track Order Status
View Analytics Dashboard

bridgebulks/
│
├── app/
│ ├── api/routes/
│ ├── models.py
│ ├── schemas.py
│ ├── db.py
│ └── main.py
│
├── frontend/
│ ├── src/pages/
│ ├── src/components/
│ └── src/App.jsx
│
├── docker-compose.yml
├── Dockerfile
└── README.md
