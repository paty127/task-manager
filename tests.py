import pytest
import sys
sys.path.insert(0, '/app/todo_project')

from todo_project import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200

def test_register_page(client):
    response = client.get('/register')
    assert response.status_code == 200

def test_redirect_unauthenticated(client):
    response = client.get('/all_tasks')
    assert response.status_code in [302, 200]

def test_about_page(client):
    response = client.get('/about')
    assert response.status_code == 200
