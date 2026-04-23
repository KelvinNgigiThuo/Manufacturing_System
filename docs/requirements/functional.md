# Functional Requirements

**Project:** Manufacturing Order & Production Management System

---

## 1. Introduction

### 1.1 Purpose

This document defines the functional requirements for a Manufacturing Order & Production Management System. The system is designed to manage customer orders, track production processes, and maintain inventory levels.

### 1.2 Scope

The system will support:

* Order management
* Production tracking
* Inventory management
* Basic invoicing

The system is intended as a lightweight, modular solution inspired by ERP systems, focusing only on core manufacturing workflows.

---

## 2. User Roles

### 2.1 Admin

* Full access to all system features
* Manage users and system configurations

### 2.2 Operations Staff

* Create and manage customer orders
* Monitor production progress
* Generate invoices

### 2.3 Production Staff

* View assigned production batches
* Update production progress

---

## 3. Customer Management

### 3.1 Features

* Create a customer
* Update customer details
* View customer information

### 3.2 Data Fields

* Name
* Contact information
* Address

---

## 4. Product Management

### 4.1 Features

* Create and manage products
* View product catalog

### 4.2 Data Fields

* Name
* SKU (unique)
* Description

---

## 5. Order Management

### 5.1 Create Order

* Select customer
* Add one or more products (Order Items)
* Define quantity per product

### 5.2 Order Status Lifecycle

* pending
* approved
* in_production
* partially_completed
* completed
* cancelled

### 5.3 Business Rules

* Orders must be approved before production starts
* Orders cannot be cancelled once production has started
* Orders cannot be marked as completed unless all items are fulfilled

---

## 6. Production Management

### 6.1 Production Batch

* Create production batches linked to order items
* Each batch represents a portion of production work

### 6.2 Batch Status

* pending
* in_progress
* completed

### 6.3 Features

* Start a batch
* Complete a batch
* Track partial production

### 6.4 Business Rules

* Total produced quantity must not exceed ordered quantity
* A batch must be in progress before it can be completed

---

## 7. Inventory Management

### 7.1 Features

* Track stock levels per product
* Update stock automatically after production

### 7.2 Rules

* Inventory increases when production is completed
* Inventory must not go negative

---

## 8. Invoice Management

### 8.1 Features

* Generate invoice from completed orders
* Track payment status

### 8.2 Invoice Status

* draft
* issued
* paid

---

## 9. System Workflows

### 9.1 Order to Production Workflow

1. Create Order → pending
2. Approve Order → approved
3. Start Production → in_production
4. Create Production Batches
5. Complete Batches → update progress
6. If partial → partially_completed
7. If fully completed → completed

---

### 9.2 Production to Inventory Workflow

1. Production batch completed
2. Inventory updated (+quantity)
3. Order item updated (produced quantity)

---

### 9.3 Order Cancellation Workflow

* Orders can only be cancelled if no production batch is in progress or completed

---

## 10. Assumptions

* Single warehouse system
* No raw material tracking (future enhancement)
* No external system integrations

---

## 11. Out of Scope

* Full ERP functionality
* Procurement and supplier management
* Payroll and HR systems
* Advanced analytics and reporting

---

## 12. Success Criteria

The system is considered successful if:

* Orders can be created and tracked through production
* Partial production is handled correctly
* Inventory updates accurately reflect production output
* Invalid operations are prevented by business rules
