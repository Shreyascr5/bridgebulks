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

## Future Work

- React Frontend
- Payment Integration
- Email Notifications
- Deployment on AWS

## Author

Shreyas C R
