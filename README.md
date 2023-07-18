# readthat

Microservice that returns an MP3 file of text sent to it using Google TTS

# Usage

Send a request over HTTP:

`$ curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -H "Authorization: YOUR_TOKEN" -d "text=Hello world" http://localhost:5000/generate -o output.mp3`

The server should return an audio file labeled `output.mp3`.

# Installation with docker-compose

Run the following command:

`$ docker compose up -d`

The service is now running and reachable over HTTP port 5000.

You can and should secure it behind a reverse proxy that uses TLS encryption to ensure there is no data or token leak.

# Installation for development purposes

Configure `config.py`:

```
TTS_LANGUAGE = 'en'

DATABASE_NAME = 'db_name'
DATABASE_HOST = 'db_host'
DATABASE_USER = 'db_username'
DATABASE_PASS = 'db_password'
```

Generate a url-safe token using Python secrets:

`$ python3 -c 'import secrets; print(secrets.token_urlsafe(32));'`

Insert the token in the database:

`INSERT INTO tokens (token) VALUES ('replace-this-token');`