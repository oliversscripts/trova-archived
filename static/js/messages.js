function infoMessage(messageText) {
    bootoast.toast({
        message: messageText,
        type: 'info',
        position: 'top',
        icon: null,
        timeout: 2,
        animationDuration: 300,
        dismissible: true
    });
}

function successMessage(messageText) {
    bootoast.toast({
        message: messageText,
        type: 'success',
        position: 'top',
        icon: null,
        timeout: 2,
        animationDuration: 300,
        dismissible: true
    });
}

function warningMessage(messageText) {
    bootoast.toast({
        message: messageText,
        type: 'warning',
        position: 'top',
        icon: null,
        timeout: 2,
        animationDuration: 300,
        dismissible: true
    });
}

function errorMessage(messageText) {
    bootoast.toast({
        message: messageText,
        type: 'danger',
        position: 'top',
        icon: null,
        timeout: 2,
        animationDuration: 300,
        dismissible: true
    });
}