# Docker python
FROM python:3

# Create folders
RUN mkdir -p /usr/bin/simple_api/

# Set application workdir
WORKDIR /usr/bin/simple_api/

# Copy application
COPY . .

# Install packages
RUN pip install flask connexion

# Set timezone
ENV TZ=America/Sao_Paulo

# Expose PORTS
EXPOSE 5000

# Init server
CMD [ "python", "./server.py" ]
