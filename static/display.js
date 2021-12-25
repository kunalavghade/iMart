var xValues = [1,2,3,4,5,6,7];
var yValues = [12,78,45,23,90,4,55];

new Chart("myChart", {
  type: "line",
  data: {
    labels: xValues,
    datasets: [{
      fill: false,
      lineTension: 0,
      backgroundColor: "blue",
      borderColor: "rgb(23, 226, 33)",
      data: yValues
    }]
  },
  options: {
    legend: {display: false},
    scales: {
      yAxes: [{ticks: {min: 0, max:100}}],
    }
  }
});