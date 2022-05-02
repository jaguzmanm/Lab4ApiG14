# ApiPipelineG14
 
## Pasos para correr el api:
#### Instalar vitualenv
    pip install virtualenv
    
#### Crear un entorno virual
    virtualenv env
    
#### Activar el entorno virtual
    env\Scripts\activate.bat
    
#### Instalar las dependencias desde requirements.txt
    pip install -r requirements.txt
    
#### Correr el api
    uvicorn main:app --reload
## Links para pruebas:
- Para probar predicciones: http://127.0.0.1:8000/predict 
- Para calcular el R2: http://127.0.0.1:8000/calculate_r2
