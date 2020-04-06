[English Version](Readme_eng.md)

---
Este repositorio alberga una API RESTful para consultar los datos oficiales de México del Coronavirus (Covid-19) incluyuendo granularidad a nivel Sexo, Edad, Fecha de Contagio, Origen de Contagio y Estado.

La API sirve los datos albergados en este [repositorio](https://github.com/jairgs/Covid19MexicoDatos).  
Para más detalles de dónde y cómo se extraen los datos favor de referirse al repositorio ya mencionado.


## Componentes de la API
La API se compone de 5 funciones básicas:

- **Todos los datos** - Para solicitar todo el conjunto de datos correr un método get a  
`http://corona-api-mexico.herokuapp.com/`
- **Datos a Nivel Estado** - Para requerir todos los datos de un Estado específico correr un método get a  
`http://corona-api-mexico.herokuapp.com/state/{Estado}`  
Use codificación de URL; por ejemplo, Nuevo León quedaría     
`http://corona-api-mexico.herokuapp.com/state/Nuevo%20León`
- **Datos por Fecha** - Para solicitar los datos para una fecha específica corra un método get a  
`http://corona-api-mexico.herokuapp.com/date/{aaaa-mm-dd}`  
- **Datos de Estado Agregados** - Si requiere la serie de tiempo de casos confirmados para un estado específico, basta con agregar el parámetro "agg" al url de la siguiente manera:
`http://corona-api-mexico.herokuapp.com/state/{Estado}/agg`  
- **Datos de Fecha Agregados** - La misma funcionalidad se aplica a los datos por fecha por lo que si se requieren los datos de casos confirmados por Estado para una fecha específica se usa la siguiente URL:  
`http://corona-api-mexico.herokuapp.com/date/{aaaa-mm-dd}/agg`  