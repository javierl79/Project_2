function statBubble(Player, statCategory) {
    var url = "/api/value-batting-data/<Player>";
    var width = 960;
    var height = 700;
    var color = Plotly.d3.scale.category20();

    Plotly.d3.json(url, function(error, value_data) {
        console.log(value_data);
        // var data = value_data.all();

        // for (var i = 0; i < value_data.length; i++) {

        var labels = value_data[0]["Player"].map(function(item) {
        	return statCategory[item]
        });
            // }
        


        var bubbleLayout = {
            margin: { t: 0 },
            hovermode: 'closest',
            height: 'height',
            width: 'width',
            xaxis: { title: 'SALARY vs. WAR' }
        };

        var bubbleData = [{
            x: value_data[12]['WAR'],
            y: value_data[3]['Dollars'],
            text: 'labels',
            mode: 'markers',
            marker: {
                size: value_data[2]['Batting'],
                color: 'color',
                colorscale: 'Earth'
            }
        }];
        var BUBBLE = document.getElementById('bubble');
        Plotly.plot(BUBBLE, bubbleData, bubbleLayout);
    });
}
statBubble();