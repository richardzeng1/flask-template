FROM python:3.7

COPY . /app

WORKDIR /app

RUN pip install pipenv

RUN pipenv install --system --deploy --ignore-pipfile --verbose

RUN pip install gunicorn[gevent]

EXPOSE 5000

CMD export FN_AUTH_REDIRECT_URI=http://localhost:5000/google/auth
CMD export FN_BASE_URI=http://localhost:5000
CMD export FN_CLIENT_ID=642274135731-k8n29ruu8kkp4tcpsvni5s8c4ptl0485.apps.googleusercontent.com
CMD export FN_CLIENT_SECRET=THvGEufM0NbADU4fNN8oIiBY

CMD export FLASK_APP=app.py
CMD export FLASK_DEBUG=1
CMD export FN_FLASK_SECRET_KEY=ASDFOUHWVLKAWEORVLKNWROINSV

CMD python shell
CMD gunicorn --worker-class gevent --workers 8 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info