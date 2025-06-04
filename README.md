
---

##  Data Versioning with Apache Airflow (via Astronomer)

This setup uses **Astronomer's Astro CLI** to run **Apache Airflow** in a containerized environment with Docker. It simplifies development and eliminates dependency issues.

---

###  Steps to Set Up

#### 1. **Install Docker Desktop**

Download and install Docker Desktop from:
 [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

> Docker is required to run the containerized Airflow environment.

---

#### 2. **Install Astro CLI**

Install the [Astro CLI](https://docs.astronomer.io/astro/cli/install-cli) (command-line tool for managing Airflow projects):

```bash
curl -sSL https://install.astronomer.io | sudo bash
```

Verify installation:

```bash
astro --version
```

---

#### 3. **Initialize the Astro Project**

Navigate to your project folder and run:

```bash
astro dev init
```

This will create the following structure:

```
.
├── dags/
├── include/
├── plugins/
├── tests/
├── Dockerfile
└── airflow_settings.yaml
```

---

#### 4. **Create Your DAG**

---

#### 5. **Run the Project**

To start your local Airflow environment:

```bash
astro dev start
```

* Access Airflow UI at: [http://localhost:8080](http://localhost:8080)
* Default credentials: `admin / admin`

The DAG will now run as scheduled, extracting data from the source, transforming it, and loading it into your database.

---




##  Successfully Deployed ETL Pipeline

![Airflow UI Screenshot](https://raw.githubusercontent.com/Gangasagarhl/MLOPS_HEART_DISEASE/main/airflow_succes.png)

---

##  Uploaded Data Successfully to MongoDB Atlas

![MongoDB Upload Screenshot](https://raw.githubusercontent.com/Gangasagarhl/MLOPS_HEART_DISEASE/main/database.png)


---



### Projects For Phising Data

Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = ap-south-1

AWS_ECR_LOGIN_URI = 
ECR_REPOSITORY_NAME = 


Docker Setup In EC2 commands to be Executed
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker# MLOPS_HEART_DISEASE
