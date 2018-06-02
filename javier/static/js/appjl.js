/* data route */
var url = "/data";

function buildPlot() {
    Plotly.d3.json(url, function(error, response) {

        console.log(response);
        var trace1 = {
            type: "scatter",
            mode: "lines",
            name: "Baseball Heatmap",
            x: response.map(data => data.birthYear),
            y: response.map(data => data.salary),
            line: {
                color: "#17BECF"
            }
        };

        var data = [trace1];

        var layout = {
            title: "Salary Per State Per Year",
            xaxis: {
                type: "date"
            },
            yaxis: {
                autorange: true,
                type: "linear"
            }
        };

        Plotly.newPlot("plot", data, layout);
    });
}

buildPlot();
