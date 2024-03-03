# Data Engineering Workshop #
### Overview ###
This project consists of a Jupyter Notebook that contains solutions to specific tasks, along with diagrams and Visualizations. 
The Workshop demonstrate the use of SQLAlchemy as an ORM connected to MySQL, including data loading, transformation and visualizations.

### Table of Contents ###
[Requirements](#requirements)
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

Using the **[requirements.txt](https://github.com/RJuanJo/etl_workshop1/edit/main/README.md#requirements)**
run the following command in **[Jupyter Notebooks](

```python
pip install -r ../config/requirements.txt
```
In this case the project is in a upyter notebook, an installation of jupyter is needed:

```python
pip install jupyterlab
```
Then, you have to run the lab with the command:

```python
jupyter lab
```
After this steps, you have to clon this repository and run the jupyter notebook workshop.ipynb.
Data Loading and Transformation <a name="data-loading-and-transformation"></a>
Detalles sobre cómo se carga la data desde diversas fuentes hacia la base de datos, incluyendo pasos para la limpieza y transformación de datos.

Visualizations <a name="visualizations"></a>
Descripciones y objetivos de cada visualización creada, con enlaces directos a las celdas específicas del Jupyter Notebook que contienen el código para generar estas visualizaciones.

Hires by Technology (Pie Chart): Visualización de la distribución de contrataciones por tecnología.
Hires by Year (Horizontal Bar Chart): Mostrar el número de contrataciones por año.
Hires by Seniority (Bar Chart): Representar el número de contrataciones por nivel de seniority.
Hires by Country Over Years (Multiline Chart): Tendencias de contrataciones por país a lo largo de los años.
How to Use
Instrucciones detalladas sobre cómo ejecutar el Jupyter Notebook, incluyendo cualquier paso de configuración necesario antes de la ejecución.
