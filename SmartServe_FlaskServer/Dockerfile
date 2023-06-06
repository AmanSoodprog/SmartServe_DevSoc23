FROM python:3.10.9
WORKDIR /aFlaskServer
COPY Pipfile Pipfile.lock ./
RUN pip install --no-cache-dir pipenv && \
    pipenv install --system --deploy --ignore-pipfile
COPY . .
EXPOSE 5000
CMD ["python", "FlaskRoutes.py"]