

function sonarr_get_status(api_data) {
    console.log('sonarr_getstatus called');
    var url = 'http://' + api_data.url + ':' + api_data.port + '/api/system/status?apikey=' + api_data.api_key; 
    console.log(url);
    $.get(url, function(data){
        console.log(data);
        return data;
    })
}