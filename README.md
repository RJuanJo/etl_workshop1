# Data Engineering Workshop #
### Overview ###
This project consists of a Jupyter Notebook that contains solutions to specific tasks, along with diagrams and Visualizations. 
The Workshop demonstrate the use of SQLAlchemy as an ORM connected to MySQL, including data loading, transformation and visualizations.

### Table of Contents ###
- [Requirements](#requirements)
- [Setup](#setup)
- [Data Loading](#data-loading)
- [Visualizations](#visualizations)
  - Hires by Technology (Pie Chart)
  -  Hires by Year (Horizontal Bar Chart)
  - Hires by Seniority (Bar Chart)
  - Hires by Country Over Years (Multiline Chart)
### Requirements <a name="requirements"></a> ###
- Python 3.x
- SQLAlchemy
- Matplotlib
- MySQL Workbench
- CSV file ("candidates.csv")
- JSON credentials file ("credentials.json") with this format:
  
  ```
  {   
  "host": "host_server",
  "database": "database_name",
  "user": "your_user",
  "password": "your_password"
  }
  ``` 
### Setup <a name="setup"></a> ###
First of all, after you have cloned this repository
must have installed the following programs:

   - **[Python](https://www.python.org)**
   - **[MySQL](https://www.mysql.com/downloads/)**
   - **[PowerBI](https://powerbi.microsoft.com/es-es/downloads/)**
   - **[VS Code](https://code.visualstudio.com/download)** or **[Jupyter](https://jupyter.org/install)**

Using the **[requirements.txt](https://github.com/RJuanJo/etl_workshop1/blob/main/config/requirements.txt)**
run the following command in **[Jupyter Notebooks](https://github.com/RJuanJo/etl_workshop1/tree/main/notebooks)**

```python
pip install -r ../config/requirements.txt
```
Previous command will install the following necessary libraries for the project

```python
-importlib
-matplotlib
-numpy
-pandas
-pip
-psycopg2-binary
-sqlalchemy
-sqlalchemy-utils
-mysqlclient
```

### Data Loading and Transformation <a name="data-loading"></a> ###
```This process was carried out in two parts, the **[First Notebook](https://github.com/RJuanJo/etl_workshop1/blob/main/notebooks/load_data.ipynb)** is responsible for reading and loading the data into the MySQL database. These are loaded and stored using a structure or model defined in the **[db_model](https://github.com/RJuanJo/etl_workshop1/tree/main/db_model)** folder.```
``` 

```

### Visualizations <a name="visualizations"></a> ###

Hires by Technology (Pie Chart): Visualización de la distribución de contrataciones por tecnología.
Hires by Year (Horizontal Bar Chart): Mostrar el número de contrataciones por año.
Hires by Seniority (Bar Chart): Representar el número de contrataciones por nivel de seniority.
Hires by Country Over Years (Multiline Chart): Tendencias de contrataciones por país a lo largo de los años.
How to Use
Instrucciones detalladas sobre cómo ejecutar el Jupyter Notebook, incluyendo cualquier paso de configuración necesario antes de la ejecución.
