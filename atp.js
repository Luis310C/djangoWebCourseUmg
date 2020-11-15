var settings = {
    "async": true,
    "crossDomain": true,
    "url": "https://community-open-weather-map.p.rapidapi.com/weather?q=san%20francisco%2Cus",
    "method": "GET",
    "headers": {
      "x-rapidapi-host": "community-open-weather-map.p.rapidapi.com",
      "x-rapidapi-key": "96f9da3898mshce7f0de8f0fdb28p1b5788jsn10da6df9d383"
    }
  }
  
  $.ajax(settings).done(function (response) {
    console.log(response);
  });