function dropDownEvent(data) {
	Plotly.d3.json("/api/standard-batting-data", function (error, data) {
		if (error) return console.warn(error);
		var team = document.getElementById("teams")
		for (var i = 0; i < data.length; i++) {
			teams = [];
			if (data[i].Team != "- - -") {
				var currentOption = document.createElement("option");
				currentOption.innerHTML = data[i].Team.unique();
				currentOption.value = data[i].Team;
				team.appendChild(currentOption);
			}

			console.log(data);
		};
	});
}


function statBubble(data) {
    var url = "/api/value-batting-data/<Player>";
    

    var width = 960;
    var height = 700;

    Plotly.d3.json(url, function(error, data) {
        // console.log(data);

        var x = [];
        var y = [];

        var label_data = [];
        var marker_size = [];

        for (i=0; i < data.length; i++) {

	        if (data[i].Dollars != "") {
	        	x.push(data[i].WAR);
	        	y.push(data[i].Dollars);
	        	marker_size.push((data[i].Batting)/10);
	        	label_data.push("Player: " + data[i].Player + 
	        		'</br>' + "WAR: " + data[i].WAR + 
	        		'</br>' + "Earnings: " +  data[i].Dollars);
        	} 
      	};

        var bubbleLayout = {
        	title: 'SALARY vs. WAR',
            margin: { t: 0 },
            hovermode: 'closest',
            height: 'height',
            width: 'width',
            xaxis: { title: 'SALARY vs. WAR' }
        };

        var bubble_data = [{
            x: x,
            y: y,
            hovertext: label_data,
            mode: 'markers',
            marker: {
                size: marker_size,
                sizeref: 0.20,
                sizemode: 'area',
                color: x,
                showscale: "True",
                opacity: 0.7,

                colorscale: 'Bluered',
                colorbar: {
                	title: "WAR",
                	titelside: "top",
                },
                zauto:false,
                cmin: 0,
                cmax : 175
            }
        }];
        var BUBBLE = document.getElementById('bubble');
        Plotly.plot(BUBBLE, bubble_data, bubbleLayout);
        
    });
}
statBubble();
dropDownEvent();

// function() {
//         var svg = d3.select('svg');

//         // Baseball field home plate
//         // location
//         var home = {
//             x: 300,
//             y: 500
//         };

//         // The x, y coord are given to us on a 250 x 250 scale
//         // so we need to translate it to appropriate coords
//         // given the scale of the our baseball svg where feet
//         // are measured in pixels.
//         var xscale = d3.scaleLinear()
//             .domain([0, 250])
//             .range([0, 600]);
//         var yscale = d3.scaleLinear()
//             .domain([0, 250])
//             .range([0, 600]);

//         function drawfield() {
//             var toMound = 60.0;
//             var betweenBases = 90.0;
//             var moundToBase = 127.28 / 2;
//             var distToCenter = 405.36;
//             var cornerToCenter = 573 / 2;
//             var moundToOutfield = 95.0;

//             // The corners of the field
//             var leftCorner = {
//                 x: home.x - cornerToCenter,
//                 y: home.y - cornerToCenter
//             };

//             var rightCorner = {
//                 x: home.x + cornerToCenter,
//                 y: home.y - cornerToCenter
//             };

//             var outfield = [leftCorner, home, rightCorner];
//             var center = [home, {
//                 x: home.x,
//                 y: home.y - distToCenter
//             }];
//             var bases = [{
//                 x: home.x - moundToBase,
//                 y: home.y - toMound
//             }, {
//                 x: home.x,
//                 y: home.y - moundToBase * 2
//             }, {
//                 x: home.x + moundToBase,
//                 y: home.y - toMound
//             }];


//             // line function
//             var line = d3.svg.line()
//                 .x(function(d) {
//                     return d.x;
//                 })
//                 .y(function(d) {
//                     return d.y;
//                 })
//                 .interpolate('linear');

//             var arc = d3.svg.arc()
//                 .innerRadius(function(d) {
//                     return d.radius;
//                 })
//                 .outerRadius(function(d) {
//                     return d.radius;
//                 })
//                 .startAngle(0)
//                 .endAngle(function(d) {
//                     return d.perimeter;
//                 })

//             svg.append('svg:path')
//                 .attr('d', line(outfield));

//             svg.append('svg:path')
//                 .attr('d', line(bases));


//             svg.append('svg:path')
//                 .attr('d', arc({
//                     radius: toMound + moundToOutfield,
//                     perimeter: Math.PI * 1 / 2
//                 }))
//                 .attr('transform', 'translate(' + home.x + ',' + home.y +
//                     ')rotate(-45)');

//             svg.append('svg:path')
//                 .attr('d', arc({
//                     radius: distToCenter,
//                     perimeter: Math.PI * 1 / 2
//                 }))
//                 .attr('transform', 'translate(' + home.x + ',' + home.y +
//                     ')rotate(-45)');

//             // third base length
//             svg.append('svg:text')
//                 .attr('transform', 'translate(' + (home.x - moundToBase - 15) + ',' + (home.y +
//                     -toMound - 4) + ')rotate(45)')
//                 .attr('font-size', '14')
//                 .attr('dy', '0.35em')
//                 .text(function(d) { return '90 feet' });

//             // center field
//             svg.append('svg:text')
//                 .attr('transform', 'translate(' + (home.x - 15) + ',' + (home.y +
//                     -distToCenter - 15) + ')rotate(0)')
//                 .attr('font-size', '14')
//                 .attr('dy', '0.35em')
//                 .text(function(d) { return Math.round(distToCenter) + ' feet' });
//         }
            


// }

// drawfield();
