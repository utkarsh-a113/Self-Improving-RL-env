# 1. Use Python as the base image
FROM python:3.13.5

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy requirements file
COPY requirements.txt .

# 4. Install Python dependencies
RUN pip install -r requirements.txt

# 5. Copy the project files
COPY . .

EXPOSE 8000
# 6. Start FastAPI server
CMD ["uvicorn", "test_llm:app", "--host", "0.0.0.0", "--port", "8000"]