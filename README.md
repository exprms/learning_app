# learning_app
simple app for learing pairs

### setup with conda:
```
conda env create -f conda-env.yml
```

in case of an update:
```
conda env update --file conda_env.yml --prune
```

## start app:
### start server:
```
uvicorn server.main:app --port 8000
```

### start app
```
streamlit run client.py
```

## references

- https://medium.com/@iambkpl/setup-fastapi-and-sqlalchemy-mysql-986419dbffeb
- https://medium.com/towards-data-engineering/fastapi-with-sql-1c7852ccbf21

