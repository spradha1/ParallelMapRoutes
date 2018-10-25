const container = document.querySelector('panel');
let directionsService;
let directionsDisplay;
let output = "";
let c = 0;

function initMap() {
    directionsService = new google.maps.DirectionsService();
    directionsDisplay = new google.maps.DirectionsRenderer();
    var mapOptions = {
        center: {lat: 30, lng: -90},
        zoom: 6
    }
    var map = new google.maps.Map(document.getElementById('map'), mapOptions);
    directionsDisplay.setMap(map);
    var request = {
        origin: from_to[0][0],
        destination: from_to[0][1],
        travelMode: 'TRANSIT',
        provideRouteAlternatives: false,
        // drivingOptions: {
        //     departureTime: new Date('October 3, 2018 09:00:00'),
        //     trafficModel: 'pessimistic'
        // },
        transitOptions: {
            departureTime: new Date('November 7, 2018 05:30:00'),
            modes: ['BUS'],
            routingPreference: 'FEWER_TRANSFERS'
        },
        unitSystem: google.maps.UnitSystem.IMPERIAL
    };
    nextLocation(request);
}

function nextLocation(request) {
    return new Promise((resolve, reject) => {
        directionsService.route(request, (result, status) => {
            if (status == 'OVER_QUERY_LIMIT') {
                console.log('over');
            }
            if (status == 'INVALID_REQUEST'){
                console.log('other status')
            }
            if (status == 'OK') {
                var data = result["routes"][0].legs[0];
                output += data["distance"].text + " " + data["duration"].text + "\n";
                directionsDisplay.setDirections(result);
                console.log(result);
            }
        
            if (c == from_to.length) {
                reject();
            }

            setTimeout(function() {
                resolve(request);
            }, 455);
        })
    }).then(function (request) {
        request["origin"] = from_to[c][0];
        request["destination"] = from_to[c][1];
        c++;
        return nextLocation(request);
    })
    .catch(function() {
        download("data.txt", output, 'text/plain');
        console.log(output);
    });
}

function download(name, text, type) {
    const file = new Blob([text], {type: type});
    const atag = '<a href="' + URL.createObjectURL(file) + '" download="' + name + '">Download</a>';
    container.insertAdjacentHTML('afterbegin', atag);
}