import kaggle
import os 

kaggle.api.authenticate()
data_folder = 'data'


if not os.path.exists(data_folder):
    os.makedirs(data_folder)
    print(f"Pasta '{data_folder}' criada com sucesso!")
else:
    print(f"Pasta '{data_folder}' já existe.")


kaggle.api.dataset_download_files('najir0123/walmart-10k-sales-datasets', path=data_folder, unzip=True)
print(f"Dataset baixado e descompactado na pasta '{data_folder}'!")