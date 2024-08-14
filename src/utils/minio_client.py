from minio import Minio
from config.minio_config import MinIOConfig

class MinioClient:
    def __init__(self):
        self.client = Minio(
            MinIOConfig.ENDPOINT,
            access_key=MinIOConfig.ACCESS_KEY,
            secret_key=MinIOConfig.SECRET_KEY,
            secure=False
        )

    def upload_file(self, file_path, object_name):
        self.client.fput_object(MinIOConfig.BUCKET_NAME, object_name, file_path)

# Example Usage
if __name__ == "__main__":
    minio_client = MinioClient()
    minio_client.upload_file("datasets/turbofan/train_FD001.txt", "train_FD001.txt")
