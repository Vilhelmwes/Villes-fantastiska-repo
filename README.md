Uppgift för första veckan:
**Host Postgres Using Docker**
Docker is already installed 🍾
Create a GitHub repo in in some dir on nixos. Use ssh keys to clone the repo.
Skapa en dockerfil för postgres (docker-compose.yaml) rikta till port 5432 om inte default.
Do Docker compose
 
In the config:
gateways:
 local:
   connection:
     type: postgres
     host: localhost #or whatever credentials you choose 
     port: 5432
     user: postgres
     password: postgres
     database: mydb
default_gateway: local
Create a model ingesting data from some public api
Look at the ingested data using DBeaver or DataGrip, both are already installed!🍾
Done! 
 
