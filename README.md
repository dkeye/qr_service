# qr_service
python version: 3.9

## Simple local run abstract_service: 
### install project and local env 
```shell script
cd <PATH_TO_PROJECT>
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn abstract_service.main:app --reload
```

## docs
http://127.0.0.1:8000/docs
