from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    url: str
    destination_folder: str
    file_name: str

@dataclass
class DocumentLoaderConfig:
    file_path: str