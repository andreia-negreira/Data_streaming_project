# Data Streaming Pipeline

## Table of Contents
- [Introduction](#introduction)
- [Technologies](#technologies)
- [Getting Started](#getting-started)

## Introduction

Welcome to this comprehensive guide on constructing an end-to-end data streaming pipeline. This project delves into each stage, from data ingestion through processing and ultimately to storage. The chosen technology stack includes robust tools such as Apache Airflow, Python, Apache Kafka, Apache Spark and Cassandra. To ensure seamless deployment and scalability, everything is encapsulated within Docker containers.

The project is designed with the following components:

- **Data Source**: Leveraging the `randomuser.me` API, random users data are generated to fuel the pipeline.
- **Apache Airflow**: Acts as the orchestrator, manages the flow of data and stores it efficiently in a PostgreSQL database.
- **Apache Kafka and Zookeeper**: Form the backbone for streaming data, facilitating seamless communication from PostgreSQL to the processing engine.
- **Control Center and Schema Registry**: Monitor and schema management for the Kafka streams.
- **Apache Spark**: Takes the reins for data processing, utilizing master and worker nodes to handle the heavy lifting.
- **Cassandra**: Serves as the robust repository where the processed data finds its home.

## Technologies

- Apache Airflow
- Python
- Apache Kafka
- Apache Zookeeper
- Apache Spark
- Cassandra
- PostgreSQL
- Docker

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/andreia-negreira/Data_streaming_project.git
    ```

2. Navigate to the project directory:
    ```bash
    cd data_streaming_project
    ```

3. Run Docker Compose to spin up the services:
    ```bash
    docker-compose up
    ```

## Credits

### Tutorial

- **Author**: [Yusuf Ganiyu](https://www.youtube.com/@CodeWithYu)
- **YouTube Channel**: [CodeWithYu](https://www.youtube.com/@CodeWithYu)
- **Tutorial Title**: [Realtime Data Streaming | End To End Data Engineering Project](https://www.youtube.com/watch?v=GqAcTrqKcrY)

### Reference Repository

- **Repository**: [Data_streaming_project](https://github.com/andreia-negreira/Data_streaming_project)
- **Original Author**: [airscholar](https://github.com/airscholar)
- **Link to Original Repository**: [e2e-data-engineering](https://github.com/airscholar/e2e-data-engineering/tree/main)