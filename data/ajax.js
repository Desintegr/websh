$(document).ready(function(){

  // focus on prompt
  document.getElementById('input').focus();

  $(document).click(function () {
    document.getElementById('input').focus();
  });

  $(document.body).keydown(function (e) {
    switch(e.which) {
      case 13: // enter
        var value = $('#input').attr('value');
        $.getJSON('ajax/command', { input: value }, function(data) {
          $('#completion').html('');
          $('#prompt').html(data.prompt);
          $('#log').html(data.log);
          eval(data.javascript);
          $('#input').attr('value', '');
          window.scroll(0, window.screen.availHeight);
        });
        e.preventDefault();
        break;
      case 38: // arrow key up
        $.getJSON('ajax/history_up', function(data) {
          $('#input').attr('value', data.history);
        });
        e.preventDefault();
        break;
      case 40: // arrow key down
        $.getJSON('ajax/history_down', function(data) {
          $('#input').attr('value', data.history);
        });
        e.preventDefault();
        break;
      case 9: // tab key
        var value = $('#input').attr('value');
        $.getJSON('ajax/completion', { input: value }, function(data) {
          if(data.count == 1) {
            $('#completion').html('');
            $('#input').attr('value', data.completion);
          }
          else {
            $('#completion').html(data.completion);
          }
        });
        e.preventDefault();
        break;
    }
  });

});
