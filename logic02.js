// function dropDownEvent(team, callback) {
// 	Plotly.d3.json("/get-teams/$(team)", function (error, teamNames) {
// 		if (error) return console.warn(error);
// 		Plotly.d3.json('/stats', function (error, data) {
// 			if (error) return console.warn(error);
// 			callback(teamData, data)
// 		});
// 	});

// 	Plotly.d3.json('/get-teams/$(team)', function(error, teamData) {
// 		if (error) return console.warn(error);
// 		var team = document.getElementById("teams")
// 		for (var i = 0; i < teamData.length; i++) {
// 			console.log(teamData);
// 			teams = [];
// 			if (teamData[i].Team != "- - -") {
// 				var currentOption = document.createElement("option");
// 				currentOption.innerHTML = teamData[i].Team;
// 				currentOption.value = teamData[i].Team;
// 				team.appendChild(currentOption);
// 			};
// 		statBubble(currentOption);
// 		}
// 	});
// }
		// var team = document.getElementById("teams")
		// for (var i = 0; i < data.length; i++) {
		// 	teams = [];
		// 	if (data[i].Team != "- - -") {
		// 		var currentOption = document.createElement("option");
		// 		currentOption.innerHTML = data[i].Team;
		// 		currentOption.value = data[i].Team;
		// 		team.appendChild(currentOption);
		// 	}

			// console.log(data);
		// };
	// });

// dropDownEvent();

function getData(team_data) {
	Plotly.d3.json(`/get-teams/${teamName}`, function(error, team_data) {
        if (error) return console.warn(error);
    });
}

function dropDown() {
    // data route
    var url = "/get-teams";

    // var teams = document.getElementById("teamName");
    // teams.innerHTML = '';

    Plotly.d3.json(url,function (error, team_data) {
		console.log(team_data);	
		var teams = [];
	    for(i=2; i < team_data.length; i++) {
	    	document.getElementById("teamName").innerHTML;
	    	// var teamTag = document.createElement("option");
	    	teamName.text = team_data[i];
    		teamName.value = team_data[i];
    		teams.append(teams);
	    	// teams.appendChild(teamTag);
    	}

    	// getData(team_data[0]);

    });
}

// var teams = document.getElementById("teamName");
//     teams.innerHTML = '';

//     Plotly.d3.json(url,function (error, team_data) {
// 		console.log(team_data);	
// 	    for(var key in team_data) {
// 	    	var teamTag = document.createElement("a");
// 	    	teamName = document.createTextNode(`${team_data[key]}`);
// 	    	teamTag.append(teamName);

// 	    	teams.appendChild(teamTag);
//     	}

//     });
// }

//     Plotly.d3.json(url,function (error, team_data) {
//     	console.log(team_data);
//     	var teams = [];
//     	for (i=0; i < team_data.length; i++) {
//     		document.getElementById("teamName").innerHTML += teams[i] + "<BR>";
//     		teams.push(team_data[i].Team);
//     	}
//     });


// }


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
dropDown();
statBubble();

// dropDownEvent();


