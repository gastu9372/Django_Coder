/*!
* Start Bootstrap - One Page Wonder v6.0.6 (https://startbootstrap.com/theme/one-page-wonder)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-one-page-wonder/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
// Hecho con ayuda de gpt
document.addEventListener("DOMContentLoaded", function () {
    let toastElList = [].slice.call(document.querySelectorAll('.toast'));
    toastElList.map(function (toastEl) {
        let toast = new bootstrap.Toast(toastEl);
        toast.show();  // Muestra el toast
        setTimeout(function() {
            toast.hide();  // Se cierra después de 3 segundos
        }, 3000);  // 3000 milisegundos = 3 segundos
    });
});

