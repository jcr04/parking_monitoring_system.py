from infrastructure.web.api import app
from infrastructure.db import initialize_db  
from domain.services.plate_recognition_service import PlateRecognitionService 

def initialize():
    print("Inicializando o aplicativo...")
    
    # Inicializando o Banco de Dados
    print("Inicializando o banco de dados...")
    initialize_db()  # Supondo que esta função inicializa seu banco de dados.
    
    # Carregando Modelos de Machine Learning
    print("Carregando modelos de machine learning...")
    plate_recognition_service = PlateRecognitionService('/path/to/tesseract')  # Substitua pelo caminho correto do Tesseract em seu sistema.
    app.config['plate_recognition_service'] = plate_recognition_service  # Armazenando o serviço no config do app para ser acessado em outros lugares.

if __name__ == '__main__':
    initialize()  # Chama a função de inicialização antes de iniciar o aplicativo.
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
