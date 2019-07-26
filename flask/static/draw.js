function makeChart(labels, values) {

    // Create new canvas 
    $("div.myChart").append('<canvas id="myChart"></canvas>')
    var ctx = document.getElementById("myChart").getContext('2d');
    
    myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                data: values,
                backgroundColor: ["#2da69b", "#2da69b", "#2da69b", "#2da69b", "#2da69b"],
            borderColor: [],
            borderWidth: 1
        }]
    },
        options: {
            legend: {
                display: false
            },
            responsive: true,
            maintainAspectRatio: true,
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }],
                xAxes: [{
                    barPercentage: 0.5
                }]
            }
        }
    
    });

    return myChart;

}

function makeChart2(labels, values) {

    // Create new canvas 
    $("div.myChart2").append('<canvas id="myChart2"></canvas>')
    var ctx = document.getElementById("myChart2").getContext('2d');

    myChart2 = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                //label: 'Number of unique MACS detected per hour',
                data: values,
                backgroundColor: ["#f2c335", "#f2c335", "#f2c335", "#f2c335", "#f2c335", "#f2c335",
                // 'rgba(255, 99, 132, 0.2)',
                // 'rgba(54, 162, 235, 0.2)',
                // 'rgba(255, 206, 86, 0.2)',
                // 'rgba(75, 192, 192, 0.2)',
                // 'rgba(153, 102, 255, 0.2)',
                // 'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                // 'rgba(255, 99, 132, 1)',
                // 'rgba(54, 162, 235, 1)',
                // 'rgba(255, 206, 86, 1)',
                // 'rgba(75, 192, 192, 1)',
                // 'rgba(153, 102, 255, 1)',
                // 'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            legend: {
                display: false
            },
            responsive: true,
            maintainAspectRatio: true,
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }],
                xAxes: [{
                    barPercentage: 0.5
                }]
            }
        }

    });

    return myChart2;

}

function makeChart3(labels, values) {

// Create new canvas 
$("div.myChart3").append('<canvas id="myChart3"></canvas>')
var ctx = document.getElementById("myChart3").getContext('2d');

myChart3 = new Chart(ctx, {
type: 'bar',
data: {
    labels: labels,
    datasets: [{
        //label: 'Number of repeated MACS',
        data: values,
        backgroundColor: ["#157ebf", "#157ebf", "#157ebf", "#157ebf", "#157ebf", "#157ebf"
        // 'rgba(255, 99, 132, 0.2)',
        // 'rgba(54, 162, 235, 0.2)',
        // 'rgba(255, 206, 86, 0.2)',
        // 'rgba(75, 192, 192, 0.2)',
        // 'rgba(153, 102, 255, 0.2)',
        // 'rgba(255, 159, 64, 0.2)'
    ],
    borderColor: [
        // 'rgba(255, 99, 132, 1)',
        // 'rgba(54, 162, 235, 1)',
        // 'rgba(255, 206, 86, 1)',
        // 'rgba(75, 192, 192, 1)',
        // 'rgba(153, 102, 255, 1)',
        // 'rgba(255, 159, 64, 1)'
    ],
    borderWidth: 1
}]
},
options: {
    legend: {
        display: false
    },
    responsive: true,
    maintainAspectRatio: true,
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero:true
            }
        }],
        xAxes: [{
            barPercentage: 0.5
        }]
    }
}

    });

    return myChart3;

}

function makeChart4(labels, values) {

// Create new canvas 
$("div.myChart4").append('<canvas id="myChart4"></canvas>')
var ctx = document.getElementById("myChart4").getContext('2d');

myChart4 = new Chart(ctx, {
type: 'bar',
data: {
    labels: labels,
    datasets: [{
        //label: 'Time spent per day',
        data: values,
        backgroundColor: ["#f27405", "#f27405", "#f27405", "#f27405", "#f27405", "#f27405", 
        // 'rgba(255, 99, 132, 0.2)',
        // 'rgba(54, 162, 235, 0.2)',
        // 'rgba(255, 206, 86, 0.2)',
        // 'rgba(75, 192, 192, 0.2)',
        // 'rgba(153, 102, 255, 0.2)',
        // 'rgba(255, 159, 64, 0.2)'
    ],
    borderColor: [
        // 'rgba(255, 99, 132, 1)',
        // 'rgba(54, 162, 235, 1)',
        // 'rgba(255, 206, 86, 1)',
        // 'rgba(75, 192, 192, 1)',
        // 'rgba(153, 102, 255, 1)',
        // 'rgba(255, 159, 64, 1)'
    ],
    borderWidth: 1
}]
},
options: {
    legend: {
        display: false
    },
    responsive: true,
    maintainAspectRatio: true,
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero:true
            }
        }],
        xAxes: [{
            barPercentage: 0.5
        }]
    }
}

});

return myChart4;

}