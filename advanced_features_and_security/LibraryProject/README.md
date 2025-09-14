# Permissions and Groups Setup Guide

## Overview
This Django application implements a comprehensive permission system using Django's built-in authentication system with custom permissions and groups.

## Custom Permissions
The Book model has been extended with four custom permissions:
- `can_view` - View books
- `can_create` - Create new books
- `can_edit` - Edit existing books
- `can_delete` - Delete books

## Groups Configuration
Three groups have been created with the following permissions:

### 1. Viewers Group
- Permissions: `can_view`
- Description: Users can only view books but cannot modify them.

### 2. Editors Group
- Permissions: `can_view`, `can_create`, `can_edit`
- Description: Users can view, create, and edit books but cannot delete them.

### 3. Admins Group
- Permissions: `can_view`, `can_create`, `can_edit`, `can_delete`
- Description: Users have full access to all book operations.

## Setup Instructions

1. **Create Groups and Assign Permissions:**
   - Go to Django Admin → Groups
   - Create the three groups: Viewers, Editors, Admins
   - Assign the appropriate permissions to each group

2. **Assign Users to Groups:**
   - Go to Django Admin → Users
   - Select a user and assign them to the appropriate group

3. **Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate