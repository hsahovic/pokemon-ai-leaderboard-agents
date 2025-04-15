FROM python:3.10-slim

# Install dependencies
RUN pip install --no-cache-dir poke-env

# Create app directory
WORKDIR /app

# Copy script
COPY agents/poke-env-RandomPlayer/start_agent.py .

# Default command
ENTRYPOINT ["python", "start_agent.py"]
