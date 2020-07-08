# About
This Web Server provides an endpoint that receives a list of images and using Microsoft cognitive service to
analyze faces on these images the result will be the biggest face in the list

#Usage
1. Create an account on microsoft Azure get cognition endpoint address and secret key
2. create .env file

```.env
FLASK_APP=vocaface/app.py
DYNACONF_COGNITION_ENDPOINT="https://<endpoint>.cognitiveservices.azure.com"
DYNACONF_COGNITION_KEY="topsecretkeygoeshere"
```

then run
```bash
docker-compose up
```

That's it, the server is up now you can make an API call like this

```bash
curl --location --request POST 'http://0.0.0.0:5000/api/face' \
--header 'Content-Type: application/json' \
--data-raw '[
            {
                "url": "https://res.cloudinary.com/demo/image/upload/butterfly.jpg"
            },
            {
                "url": "https://res.cloudinary.com/demo/image/upload/docs/plain_face.jpg"
            },
            {
                "url": "https://i2-prod.mirror.co.uk/incoming/article14334083.ece/ALTERNATES/s615/3_Beautiful-girl-with-a-gentle-smile.jpg"
            }

        ]'
```




