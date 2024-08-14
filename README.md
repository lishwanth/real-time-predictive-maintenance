
# Real-Time Predictive Maintenance Pipeline

## Overview

This project implements a real-time predictive maintenance pipeline using various open-source tools. The primary goal is to detect anomalies in industrial machines using LSTM networks and provide insights into machine health in real-time.

## Features

- **Real-Time Data Ingestion**: Use Apache Kafka for real-time data streaming.
- **Data Processing**: Apache Spark processes and transforms data.
- **Predictive Modeling**: LSTM networks built using PyTorch predict machine anomalies.
- **Stream Processing**: Apache Flink handles real-time stream processing.
- **Object Storage**: MinIO stores the processed data and model outputs.

## Datasets

- **NASA’s Turbofan Engine Degradation Simulation Data Set**
- **MIMII Dataset**: Machine sounds dataset for anomaly detection in industrial machines.

## Project Structure

```plaintext
real-time-predictive-maintenance/
│
├── datasets/
│   ├── turbofan/
│   ├── mimii/
├── src/
│   ├── config/
│   ├── data_pipeline/
│   ├── models/
│   ├── stream_processing/
│   └── utils/
├── notebooks/
├── tests/
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
└── LICENSE
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/real-time-predictive-maintenance.git
cd real-time-predictive-maintenance
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Set up the environment using Docker:

```bash
docker-compose up
```

## Usage

1. Start the Kafka producer:

```bash
python src/data_pipeline/kafka_producer.py
```

2. Consume and process the data:

```bash
python src/data_pipeline/kafka_consumer.py
```

3. Train the LSTM model:

```bash
python src/models/train.py
```

4. Run stream processing using Flink:

```bash
python src/stream_processing/flink_processing.py
```

## Testing

Run the unit tests:

```bash
python -m unittest discover tests
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contact

For any questions or suggestions, please open an issue or contact the project maintainer at your.email@example.com.
