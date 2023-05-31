// script that fetches and prints how to say "Hello" depending on the language

$('document').ready(() => {
  $('INPUT#btn_translate').click(() => {
    const url = 'https://www.fourtonfish.com/hellosalut/?';
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), (data) => {
      $('DIV#hello').html(data.hello);
    });
  });
  $('INPUT#language_code').focus(() => {
    $(this).keydown((e) => {
      if (e.keyCode === 13) {
        translate()
      }
    });
  });
});

const translate = () => {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
    $('DIV#hello').html(data.hello);
  });
}
