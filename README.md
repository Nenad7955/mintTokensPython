Before starting backend run following commands:

```bash
$ docker-compose up -d # detached state

$ pip3 install -r requirements

$ prisma generate
$ prisma migrate dev # for development mode

#optionally open ui to see data in db
$ prisma studio
```

After setting up project, run following command:

```bash
$ uvicorn src.main:app
```

Don't forget to 
```bash
$ docker-compose down
```
