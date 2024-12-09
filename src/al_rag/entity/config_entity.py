class DataIngestionConfig:
    def __init__(self, url, destination_folder, file_name):
        self.url = url
        self.destination_folder = destination_folder
        self.file_name = file_name

    def __repr__(self):
        return f"DataIngestionConfig(url={self.url}, destination_folder={self.destination_folder}, file_name={self.file_name})"