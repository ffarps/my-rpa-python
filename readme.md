# Simple RPA Chatbot - Proof of Concept

This is a Python project exploring Robotic Process Automation (RPA) through a chatbot interface. It demonstrates how conversational AI can trigger and manage automated processes.

## What This Project Does

The project combines a simple chatbot with web automation capabilities:

- **Chatbot Interface**: Built with Streamlit, handles greetings and a basic check-in process that collects user information and generates a reservation code
- **Web Automation**: Uses the RPA library for browser automation, with an example script that searches DuckDuckGo
- **Modular Architecture**: Designed to easily add new automation flows

The goal is to show how chatbots can make RPA more accessible by providing a natural language interface for triggering automated tasks.

## Quick Start

### Local Setup

1. Create a virtual environment:

   ```bash
   python -m venv myvenv
   source myvenv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the chatbot:

   ```bash
   streamlit run streamlit_bot.py
   ```

### Docker Setup

1. Create docker-compose.yml:

   ```bash
   cat <<EOL > docker-compose.yml
   services:
     app:
       build: .
       container_name: rpa-bot-python-01
       command: streamlit run streamlit_bot.py --server.port=8515 --server.address=0.0.0.0
       ports:
         - 8515:8515
       image: rpa-bot-python-image-01:latest
   volumes:
     img_db:
   EOL
   ```

2. Build and run:

   ```bash
   docker compose build
   docker compose up
   ```

## Project Structure

- `streamlit_bot.py` - Main chatbot application
- `Check_in_flow.py` - Check-in workflow logic
- `define_type_of_flow.py` - Flow routing
- `modular01.py` - State management
- `duckduckgo_rpa.py` - Example RPA automation script
- `requirements.txt` - Python dependencies

## Releasing as a Proof of Concept

To prepare this for sharing as a PoC:

### Code Quality

- Remove unused dependencies and files
- Add proper error handling and logging
- Ensure code is well-documented
- Test all functionality

### Documentation

- Add screenshots of the interface
- Include usage examples
- Document the RPA capabilities

### Deployment

- Create a Dockerfile for containerization
- Set up environment configuration
- Consider cloud deployment options

### Distribution

- Publish on GitHub with clear setup instructions
- Add relevant tags and topics
- Consider a demo deployment

### Future Development

- Implement additional RPA workflows
- Add API integrations
- Include user authentication
- Enhance conversation capabilities

## Purpose

RPA tools are powerful but often require technical expertise. This project explores how conversational interfaces can make automation more approachable for non-technical users, potentially serving as a foundation for enterprise automation solutions.
