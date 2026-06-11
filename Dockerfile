FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install Flask Flask-Bcrypt Flask-Login Flask-SQLAlchemy Flask-WTF WTForms email-validator
RUN python -c "import sys; sys.path.insert(0, '/app/todo_project'); from todo_project import app, db; app.app_context().push(); db.create_all()"
EXPOSE 5000
CMD ["python", "todo_project/run.py"]
