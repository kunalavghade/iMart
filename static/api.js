
// Defining async function
const url ="https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=MPFQ6IDGVK5LB9JQ"
let current_time  = new Date()
console.log(current_time.getMinutes())
async function getapi(url) {
	
	// Storing response
	const response = await fetch(url);
	
	// Storing data in form of JSON
	var data = await response.json();
	let data_time = (data["Time Series (5min)"]);
    console.log(data_time[0])
}

getapi(url)