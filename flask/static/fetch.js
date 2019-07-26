function getUniqueMACS(){

    var drop_down = document.getElementById("devices");
    var dev = drop_down.options[drop_down.selectedIndex].value; 

    //Delete old canvas
    $("canvas#myChart").remove();

    labels = []
    values = []
    start = document.getElementById("mac_start").value
    end = document.getElementById("mac_end").value
       
    // Async call
    fetch('http://localhost:5000/num_macs/' + dev + '/' + start + '/' + end)
    .then((res) => res.json())
    .then((data) => {

        console.log(data)
        data.forEach(function(post){
            labels.unshift(post.date);
            values.unshift(post.count);
        })
        myChart = makeChart(labels, values);

    });
}

function UniqueMACSToday(){

    var drop_down = document.getElementById("devices");
    var dev = drop_down.options[drop_down.selectedIndex].value; 
    
    $("canvas#myChart2").remove();
            
    labels = []
    values = []

    fetch('http://localhost:5000/num_macs/' + dev + '/' + 'today')
    .then((res) => res.json())
    .then((data) => {
            
        let output = ''
        data.forEach(function(post){
            output += `Date: ${post.time} Count: ${post.count} <br> `;
            labels.push(post.time);
            values.push(post.count);
        })
        myChart2 = makeChart2(labels, values);
    });
}

function getNumRepeats(){

    var drop_down = document.getElementById("devices");
    var dev = drop_down.options[drop_down.selectedIndex].value; 

    $("canvas#myChart3").remove();
    
    labels = []
    values = []

    start = document.getElementById('rep_start').value;
    end = document.getElementById('rep_end').value;
    offset = document.getElementById('offset').value;


    fetch('http://localhost:5000/num_repeats/' + dev + '/' + start + '/' + end + '/' + offset)
    .then((res) => res.json())
    .then((data) => {
        console.log(data)
        let output = ''
        data.forEach(function(post){
            console.log(data)
            output += `Date: ${post.date} Count: ${post.count} <br> `;
            labels.unshift(post.date);
            values.unshift(post.count);
        })

    myChart3 = makeChart3(labels, values);

    });
}

function macLookup(){

    var drop_down = document.getElementById("devices");
    var dev = drop_down.options[drop_down.selectedIndex].value; 
            
    let MAC = document.getElementById('mac_text').value;
    labels = []
    values = []

    $("canvas#myChart4").remove();

    fetch('http://localhost:5000/mac_lookup/' + dev + '/' + MAC)
    .then((res) => res.json())
    .then((data) => {
        let output = ''
        output+=`<br>First detection: ${data['First detection']} <br>
        Last detection: ${data['Last detection']} <br>
        Duration: ${data['Duration']} seconds<br>
        Last updated: ${data['Last updated']} <br>`
        document.getElementById("mac_data").innerHTML = output;
                    
    })

    fetch('http://localhost:5000/historical_data/' + dev + '/' + MAC)
    .then((res) => res.json())
    .then((data) => {
        let output = ''
        data.forEach(function(post){
        output += `Date: ${post.date} Count: ${post.Duration} <br> `;
        labels.unshift(post.date);
        values.unshift(post.Duration);
        })

        myChart4 = makeChart4(labels, values);
    })
}