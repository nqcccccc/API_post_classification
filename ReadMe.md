current python 3.9.13

## CREATE VENV 

```bash
python -m venv myenv
. myenv/bin/active
```

## INSTALL REQUIREMENTS

```bash
pip install -r requirements.txt
```

## START SERVER

```bash
uvicorn wsgi:app --reload
```

## RUN DOCKER 

```bash
docker run -p 8080:8080 nqcccccc/api-nude-detect 
```