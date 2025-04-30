FROM python:3.12-slim

WORKDIR /app

# Copy the full project including pickle model
COPY . .

# Upgrade pip
RUN pip install --upgrade pip

RUN pip install -r requirements.txt
# Install packages from local wheelhouse (if any)
# COPY packages/ ./packages/
# RUN pip install --no-index --find-links=packages -r requirements.txt

# Optional: Expose port (if using FastAPI uvicorn server)
EXPOSE 8000

# Run the app (adjust as needed)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


