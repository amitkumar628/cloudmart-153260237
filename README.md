CloudMart Backend – FastAPI + Cosmos DB + ACI + ACR

Author: Amit Kumar (153260237)
Course: CSP451 – Cloud Infrastructure
Project: CloudMart Backend Deployment (Docker + ACR + ACI + CosmosDB)

📌 Project Overview

CloudMart Backend is a FastAPI-based microservice that provides APIs for product catalogs, cart operations, and store management.
The application is containerized using Docker, pushed to Azure Container Registry (ACR), and deployed to Azure Container Instances (ACI).
Cosmos DB is used as the NoSQL database.

🚀 Architecture
FastAPI App → Docker Image → Azure Container Registry (ACR) → Azure Container Instances (ACI)
                                       ↓
                                Azure Cosmos DB

📁 Project Structure
backend/
│── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── templates/
│   ├── static/
│   └── services/
│
│── Dockerfile
│── requirements.txt
│── startup.txt
│── README.md

🧪 Local Testing (Before Docker Build)
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run FastAPI locally
uvicorn app.main:app --reload

3️⃣ Open browser

http://localhost:8000

http://localhost:8000/products

http://localhost:8000/cart

🐳 Docker Build + Test
Build Docker image
docker build -t cloudmart-backend:latest .

Run container locally
docker run -p 8000:80 cloudmart-backend:latest

🔐 Push to Azure Container Registry (ACR)
Build & Push from Azure Cloud Shell
az acr build --registry cloudmartacr153260237 --image cloudmart-backend:latest .


ACR Image Path:

cloudmartacr153260237.azurecr.io/cloudmart-backend:latest

☁ Deploy to Azure Container Instances (ACI)
Create ACI from ACR Image
az container create \
  --resource-group Student-RG-1887890 \
  --name cloudmart-backend-aci \
  --image cloudmartacr153260237.azurecr.io/cloudmart-backend:latest \
  --registry-login-server cloudmartacr153260237.azurecr.io \
  --registry-username  
  --registry-password <YOUR-ACR-PASSWORD> \
  --ports 80 \
  --os-type Linux \
  --cpu 1 --memory 1.5 \
  --environment-variables \
      COSMOS_ENDPOINT="<your-cosmos-uri>" \
      COSMOS_KEY="<your-cosmos-key>"

🗄 Configure Cosmos DB
Required environment variables
COSMOS_ENDPOINT=https://cloudmartdb153260237.documents.azure.com:443/



These values must be added during ACI deployment.

🌐 Access the Running API

Once ACI is deployed:

http://<PUBLIC-IP-OF-ACI>/
http://<PUBLIC-IP-OF-ACI>/health
http://<PUBLIC-IP-OF-ACI>/products

🔎 Useful Azure Commands
Check ACI container status
az container show \
  --resource-group Student-RG-1887890 \
  --name cloudmart-backend-aci \
  -o table

View logs
az container logs \
  --resource-group Student-RG-1887890 \
  --name cloudmart-backend-aci

📝 Submission Requirements (For Seneca CSP451)

Dockerfile ✔

requirements.txt ✔

FastAPI source code ✔

ACR build screenshot ✔

ACI deployment screenshot ✔

Cosmos DB configuration screenshot ✔

Health endpoint working screenshot ✔

Products endpoint working screenshot ✔

README.md (this file) ✔
