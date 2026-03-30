# BridgeBulks – Bulk Ordering Optimization System

## Overview

BridgeBulks is a bulk ordering optimization platform that helps local stores combine their orders and automatically select the best vendor based on price, rating, delivery time, and historical performance.

## Features

- Customer Authentication (JWT)
- Bulk Order Management
- Smart Vendor Selection Algorithm
- Vendor Rating & Performance Tracking
- Redis Caching for Performance Optimization
- Order Status Tracking
- Analytics Dashboard APIs
- Dockerized Deployment
- PostgreSQL Database

## Tech Stack

- FastAPI
- PostgreSQL
- Redis
- Docker
- SQLAlchemy
- JWT Authentication

## System Architecture

Client → FastAPI → Redis → PostgreSQL

## Smart Vendor Selection Algorithm

The system selects vendors using:

- Price (50%)
- Vendor Rating (30%)
- Delivery Time (20%)
- Historical Performance

## API Endpoints

| Endpoint            | Description       |
| ------------------- | ----------------- |
| /login              | Customer login    |
| /vendors            | Manage vendors    |
| /products           | Manage products   |
| /vendor-products    | Vendor pricing    |
| /bulk-orders        | Create bulk order |
| /order-status       | Track order       |
| /vendor-rating      | Rate vendor       |
| /vendor-performance | Vendor analytics  |
| /analytics          | System analytics  |

This project demonstrates supply chain optimization using a Multi-Criteria Decision Making (MCDM) algorithm.

Tech Stack
Layer Technology
Frontend React (Vite) + Bootstrap
Backend FastAPI (Python)
Database PostgreSQL
Cache Redis
Authentication JWT
Charts Chart.js
Containerization Docker
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

Backend runs on:
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

Frontend runs on:
http://localhost:5173

Vendor Selection Algorithm

The system selects the best vendor using a weighted scoring formula:

Score = (1 / Price) _ 0.5 + (Rating / 5) _ 0.3 + (1 / Delivery Days) \* 0.2
Weight Distribution
Factor Weight
Price 50%
Rating 30%
Delivery Time 20%

The vendor with the highest score is selected automatically.

Main Modules
Authentication
Vendors
Products
Inventory
Bulk Orders
Vendor Selection
Comparison & Savings
Order Status Tracking
Vendor Rating
Analytics Dashboard
How to Run the Project
Using Docker
docker compose up --build

Backend:

http://127.0.0.1:8000

Frontend:

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
Project Structure
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
Project Title

## Future Work
- Deployment on AWS

## Author

Shreyas C R
