# House Tasks API

A REST API for shared households, built with Django REST Framework. People join a house, share task lists, mark tasks done, attach files, and the house earns points for finished work.

## Features

- **Houses:** create a house with a name, description and image; members can join and leave, and members can be removed
- **Points:** a house gets 10 points when a task is completed and loses them if the task is reopened
- **Task lists and tasks:** each house has task lists, each list has tasks with a status (not completed or completed), who created it and who completed it
- **Update a task's status** with a dedicated action; a task list is marked complete when all its tasks are done
- **Attachments:** upload files to a task
- **Users and profiles:** a profile with a picture is created automatically for each new user
- OAuth2 authentication with `django-oauth-toolkit` and `django-rest-framework-social-oauth2`
- Filtering with `django-filter`
- UUID primary keys for houses and attachments, and generated upload paths for images and files

## API

All routes are under `/api/`.

| Endpoint | Description |
| --- | --- |
| `/api/auth/` | OAuth2 token endpoints (get, refresh, revoke) |
| `/api/accounts/users/`, `/api/accounts/profiles/` | Users and profiles |
| `/api/house/houses/` | Houses |
| `/api/house/houses/<id>/join/` | Join a house (POST) |
| `/api/house/houses/<id>/leave/` | Leave a house (POST) |
| `/api/house/houses/<id>/remove_member/` | Remove a member (POST, `user_id`) |
| `/api/tasklists/tasklists/` | Task lists |
| `/api/tasklists/tasks/` | Tasks |
| `/api/tasklists/tasks/<id>/update_task_status/` | Change a task's status |
| `/api/tasklists/attachments/` | Task attachments |

## Built with

- Python 3, Django 5.0, Django REST Framework 3.15
- django-oauth-toolkit, django-rest-framework-social-oauth2, social-auth-app-django
- django-filter
- SQLite

## Run it locally

```bash
git clone https://github.com/hamzakhalem/django-repo.git
cd django-repo
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
export DJANGO_SECRET_KEY="any-long-random-string"   # PowerShell: $env:DJANGO_SECRET_KEY="..."
cd main
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

To get OAuth2 tokens, create an application in the Django admin under **Django OAuth Toolkit → Applications**, then call `/api/auth/token` with its client id and secret.

## Project structure

```
main/
  main/    Settings and root URLs
  users/   Users, profiles, signals that create a profile for each user
  house/   Houses, join/leave/remove member actions, permissions
  task/    Task lists, tasks, attachments, signals for points and list status
```
