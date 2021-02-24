var HttpClient = function() {
    this.get = function(aUrl, aCallback) {
        var anHttpRequest = new XMLHttpRequest();
        anHttpRequest.onreadystatechange = function() { 
            if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200)
                aCallback(anHttpRequest.responseText);
        }

        anHttpRequest.open( "GET", aUrl, true );            
        anHttpRequest.send( null );
    }
}

var counter = document.getElementById("deaths");

setInterval(function(){
    var client = new HttpClient();
    client.get('counter.txt?x='+Math.random()*10, function(response) {
        counter.innerText = response;
    });
}, 500);