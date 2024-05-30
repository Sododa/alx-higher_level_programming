// JavaScript script that fetches from https://hellosalut.stefanbohacek.dev
// and displays the value of hello from that fetch in the HTML tag DIV#hello

$(function () {
    
    var Hello = $('DIV#character');

    $.ajax({
        type: 'GET',
        url: 'https://fourtonfish.com/hellosalut/?lang=fr',
        success: function(data) {
            $(data.hello).appendTo(Hello);
        }
    })
})
