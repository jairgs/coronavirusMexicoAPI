This repository hosts a RESTful API for querying the Mexico data for Coronavirus (Covid-19) official figures with Sex, Age, Date, Origin and State granularity.

The API serves the data hosted in this [repository](https://github.com/jairgs/Covid19MexicoDatos).  
For details about where from and how this data is being pulled please refer to the aforementioned repository.

## API components
There are 5 basic queries in this API:
- **All Data** - To query all historic data run a get method to   
`http://corona-api-mexico.herokuapp.com/`
- **State Data** - To query all data from a specific state run a get method to  
`http://corona-api-mexico.herokuapp.com/state/{state}`  
Use URL encoding for example Nuevo Leon would be   
`http://corona-api-mexico.herokuapp.com/state/Nuevo%20León`
- **Date Data** - To query a specific state run a get method to  
`http://corona-api-mexico.herokuapp.com/date/{yyyy-mm-dd}`  
- **Aggregated state** - If you would like to aggregate the state data and get the total cases by date for a specific state only add the "agg" parameter to the url like so
`http://corona-api-mexico.herokuapp.com/state/{State}/agg`  
- **Aggregated date** - Same functionality on the date; if you would like to see only the total cases by state on a specific date add "agg" to the date query:
`http://corona-api-mexico.herokuapp.com/date/{yyyy-mm-dd}/agg`  