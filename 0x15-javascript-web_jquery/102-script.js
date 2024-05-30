// JavaScript script that fetches and prints how to say “Hello”
// depending on the language

$('document').ready(function () {
    let languageCode = $('#language_code');
    let btn = $('#btn_translate');
    let translation = $('DIV#hello');
    let url = 'https://www.fourtonfish.com/hellosalut/?';

    btn.click(function () {
        $.get(url + $.param({ lang: languageCode.val() }), function (data) {
            translation.html(data.hello);
        });
    });
});
