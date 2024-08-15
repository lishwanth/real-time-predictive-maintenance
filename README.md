
# Real-Time Predictive Maintenance Pipeline

## Overview

This project implements a real-time predictive maintenance pipeline, leveraging a suite of open-source tools. The objective is to detect anomalies in industrial machinery by ingesting, processing, and analyzing data streams in real-time using machine learning models, specifically LSTM networks.

## Tools & Technologies Used

### 1. **Apache Kafka**
   - **Purpose**: Kafka is used for building the real-time data ingestion pipeline. It allows the system to handle large volumes of data in real-time by streaming sensor data from industrial machines.
   - **Role in Project**: Kafka produces and consumes the data streams that feed into the predictive maintenance pipeline.

### 2. **Apache Spark**
   - **Purpose**: Spark is utilized for processing and analyzing the streaming data. Its in-memory processing capabilities make it ideal for handling large-scale data efficiently.
   - **Role in Project**: Spark transforms the raw data into features that can be fed into the LSTM model for prediction.

### 3. **PyTorch (LSTM Networks)**
   - **Purpose**: PyTorch is used to build and train the LSTM model that predicts potential machine failures.
   - **Role in Project**: The LSTM model processes the time-series data from machines and predicts when a machine is likely to fail, enabling proactive maintenance.

### 4. **Apache Flink**
   - **Purpose**: Flink is an alternative stream processing engine that provides low-latency data processing.
   - **Role in Project**: Flink processes the Kafka data streams in real-time and applies business logic to detect anomalies.

### 5. **MinIO**
   - **Purpose**: MinIO serves as an object storage solution, similar to AWS S3, where processed data and models can be stored securely.
   - **Role in Project**: MinIO stores the results from the Spark processing and the trained LSTM models for further use.

### 6. **Pandas**
   - **Purpose**: Pandas is used for data manipulation and analysis in Python.
   - **Role in Project**: It is particularly useful in the exploratory data analysis phase and for preparing data for the LSTM model.

### 7. **Seaborn & Matplotlib**
   - **Purpose**: These libraries are used for data visualization.
   - **Role in Project**: Seaborn and Matplotlib are used to generate plots and visualizations that help understand data distributions and model performance.

### 8. **Docker & Docker Compose**
   - **Purpose**: Docker is used to containerize the entire application, making it easier to deploy and manage dependencies.
   - **Role in Project**: Docker Compose orchestrates the various services (Kafka, Spark, Flink, MinIO) in containers to ensure smooth integration and scalability.

## Project Structure

```plaintext
real-time-predictive-maintenance/
│
├── datasets/
│   ├── turbofan/
│   │   └── [NASA's Turbofan Dataset Files]
│   ├── mimii/
│       └── [MIMII Dataset Files]
│
├── src/
│   ├── config/
│   │   ├── __init__.py
│   │   ├── kafka_config.py
│   │   ├── spark_config.py
│   │   ├── minio_config.py
│   ├── data_pipeline/
│   │   ├── __init__.py
│   │   ├── kafka_producer.py
│   │   ├── kafka_consumer.py
│   │   ├── data_processor.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── lstm_model.py
│   │   └── train.py
│   ├── stream_processing/
│   │   ├── __init__.py
│   │   ├── flink_processing.py
│   └── utils/
│       ├── __init__.py
│       ├── logger.py
│       ├── data_loader.py
│       ├── minio_client.py
│
├── notebooks/
│   └── eda.ipynb
│
├── tests/
│   ├── __init__.py
│   ├── test_data_pipeline.py
│   ├── test_models.py
│   ├── test_stream_processing.py
│   └── test_utils.py
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
└── LICENSE
```

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/real-time-predictive-maintenance.git
cd real-time-predictive-maintenance
```

2. **Install the required Python packages**:

```bash
pip install -r requirements.txt
```

3. **Set up the environment using Docker**:

```bash
docker-compose up
```

## Usage

1. **Start the Kafka producer**:

```bash
python src/data_pipeline/kafka_producer.py
```

2. **Consume and process the data**:

```bash
python src/data_pipeline/kafka_consumer.py
```

3. **Train the LSTM model**:

```bash
python src/models/train.py
```

4. **Run stream processing using Flink**:

```bash
python src/stream_processing/flink_processing.py
```

## Testing

Run the unit tests:

```bash
python -m unittest discover tests
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please open an issue or contact the project maintainer at lishwanthkumar@gmail.com.
