# Data Engineering Workshop #
### Overview ###
_This project consists of a Jupyter Notebook that contains solutions to specific tasks, along with diagrams and Visualizations._ 

_The Workshop demonstrate the use of SQLAlchemy as an ORM connected to MySQL, including data loading, transformation and visualizations._

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
- **[CSV File](https://github.com/RJuanJo/etl_workshop1/blob/main/data/candidates.csv)**
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
_First of all, after you have cloned this repository
must have installed the following programs:_

   - **[Python](https://www.python.org)**
   - **[MySQL](https://www.mysql.com/downloads/)**
   - **[PowerBI](https://powerbi.microsoft.com/es-es/downloads/)**
   - **[VS Code](https://code.visualstudio.com/download)** or **[Jupyter](https://jupyter.org/install)**

_Using the **[requirements.txt](https://github.com/RJuanJo/etl_workshop1/blob/main/config/requirements.txt)**
run the following command in **[Jupyter Notebooks](https://github.com/RJuanJo/etl_workshop1/tree/main/notebooks)**_

```python
pip install -r ../config/requirements.txt
```
_Previous command will install the following necessary libraries for the project_

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
 _This process was carried out in two parts, the **[First Notebook](https://github.com/RJuanJo/etl_workshop1/blob/main/notebooks/load_data.ipynb)** is responsible for reading and loading the data into the MySQL database. These are loaded and stored using a structure or model defined in the **[Structure File](https://github.com/RJuanJo/etl_workshop1/blob/main/db_model/models_structure.py)** inside the **[db_model](https://github.com/RJuanJo/etl_workshop1/tree/main/db_model)** folder._

_The **[Second Notebook](https://github.com/RJuanJo/etl_workshop1/blob/main/notebooks/workshop_eda.ipynb)** is where we extract the data from the database and begin a process of transformation and exploratory data analysis (EDA) to finally store the data in a new table also previously structured in the **[Structure File](https://github.com/RJuanJo/etl_workshop1/blob/main/db_model/models_structure.py)**._


### Visualizations <a name="visualizations"></a> ###

- Hires by Technology (Pie Chart): _Visualization of the distribution of hires by technology which were categorized to have a better format and ease when performing the analysis._

- Hires by Year (Horizontal Bar Chart): _Shows the number of hires per year._

- Hires by Seniority (Bar Chart): _Represents the number of hires by seniority level._

- Hires by Country Over Years (Multiline Chart): _Hiring trends by the chosen countries over the years._

### These visualizations can be seen in the **[Dashboard Summary](https://github.com/RJuanJo/etl_workshop1/blob/main/data/files/Workshop_DashB.pdf)**.
### In turn, you can access the **[Virtual Dashboard](https://app.powerbi.com/view?r=eyJrIjoiNjJjYzhlMzMtMDRiYy00NWRkLTg2ZGQtN2EwNGM2NTMxYjQ5IiwidCI6IjY5M2NiZWEwLTRlZjktNDI1NC04OTc3LTc2ZTA1Y2I1ZjU1NiIsImMiOjR9&pageName=ReportSection)** for a more interactive experience and a greater display of the data.
