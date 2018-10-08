

function sonarr_get_status(api_data) {
    console.log('sonarr_getstatus called');
    console.log(api_data);
    var url = 'http://' + api_data.url + ':' + api_data.port + '/api/system/status?apikey=' + api_data.api_key; 
    console.log(url);
    $.get(url, function(data){
        console.log(data);
        return data;
    })
}

function arrayBufferToBase64(buffer) {
    var binary = '';
    var bytes = [].slice.call(new Uint8Array(buffer));
    
    bytes.forEach((b) => binary += String.fromCharCode(b));
    
    return window.btoa(binary);
};

function sonarr_get_image(tv_config_data, sonarr_url, sonarr_id, image_type, width) {
    var url = sonarr_url + '/MediaCover/' + sonarr_id + '/' + image_type + '.jpg';

    var headers = new Headers({'X-Api-Key': tv_config_data['sonarr_api_key']});
    var options = {
        method: 'GET',
        headers: headers,
        mode: 'cors',
        cache: 'default'
    };
    var request = new Request(url);

    fetch(request, options).then((response) => {
        response.arrayBuffer().then((buffer) => {
            var base64Flag = 'data:image/jpeg;base64,';
            var imageStr = arrayBufferToBase64(buffer);

            var newSrc = base64Flag + imageStr;
            var newImage = new Image();
            //newImage.id = 'show_image' + sonarr_id;
            newImage.src = newSrc;
            if (width > 0) {
                newImage.width = width;
            }
            $('.image-loader-'+sonarr_id).html(newImage);
            $('.image-loader-'+sonarr_id).find('img').addClass('img-responsive');
        });
    });
}