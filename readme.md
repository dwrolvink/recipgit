# Flasklet
This project is nothing more than a very simple template for a quick and dirty flask application for home use.

# Prerequisites
- Make sure you've installed `docker` and `docker-compose`
- If you use vs code, I can really recommend the docker extension (not needed for installation though).

# Build image
```
docker build -t dwrolvink/recipgit .
```

# Run container
```
docker-compose up --detach
```

# Develop
Now a container will have spun up and you can go to http://localhost:8080 to view the website.

`/app` will be mounted as a volume, so you can develop and see the changes immediately.

in firefox: use shift+f5 when you edit css to reload all the cached files
