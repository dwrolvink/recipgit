// Do a GET request to a url
// json.parse the text that the url returns
// call the callback function (with arguments when provided)
// : no error handling!
function httpGetJsonAsync(url, callback_success)
{
    var callback_success_func = callback_success[0]
    var callback_success_args = callback_success.slice(1)

    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200){
            callback_success_func(JSON.parse(xmlHttp.responseText), ...callback_success_args);
        }
    }
    xmlHttp.open("GET", url, true); // true for asynchronous 
    xmlHttp.send(null);
}