# Python RPA Bot

To create a `docker-compose.yml` file and include your OpenAI API key, run the following command:

## For simple RPA bot

```bash
cat <<EOL > docker-compose.yml
services:
  app:
    build: .
    container_name: rpa-bot-python-01
    command: streamlit run streamlit_bot.py --server.port=8515 --server.address=0.0.0.0
    environment:
      - OPENAI_API_KEY=sk-proj-xxx
    ports:
      - 8515:8515
    image:  rpa--bot-python-image-01:latest
volumes:
  img_db:
EOL
```

## Run Docker Compose

```bash
docker compose build 
docker compose up
```

### rebuild docker

```bash
docker compose down
docker compose build
docker compose up
```

## Configure venv

```bash
python -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
```

## create .env file

```bash
echo OPENAI_API_KEY="sk-xxx" >> .env
```

## Run streamlit druid bot

```bash
streamlit run modular01.py --server.headless true --server.port 8585
```
