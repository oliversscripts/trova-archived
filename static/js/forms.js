function fieldset_toggler(controlling_field, fieldset_list) {

    if (controlling_field) {
        
        if (!$('#' + controlling_field).is(":checked")) {
            fieldset_list.forEach(function(element){
                $('#' + element).prop('disabled', true);
                console.log($('#' + element).prop('disabled'));
            });
            
        }  
        
        $('#' + controlling_field).change(function() {
            if (!$('#' + controlling_field).is(":checked")) {
                fieldset_list.forEach(function(element){
                    $('#' + element).prop('disabled', true);
                });
            } else {
                fieldset_list.forEach(function(element){
                    $('#' + element).prop('disabled', false);
                });
            }
        });
        
    }
    
}