# Stage 1 
# Base imnage

FROM  python:3.10-slim AS Food

# Working Directory 
WORKDIR /Menu

COPY requirements.txt .

# Install Dependancy
RUN apt-get update
RUN pip install --no-cache-dir -r requirements.txt

# ---------- Stage 2: Final Stage -----------------

FROM python:3.10-slim

WORKDIR /Menu

RUN pip install flask
RUN pip install --upgrade pip
COPY --from=Food /Menu/  ./
COPY . .

# Expose port
EXPOSE 5000

# Set environment variable for Flask
ENV FLASK_APP=main.py


# Run the application
CMD ["flask", "run"]
