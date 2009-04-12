$(document).ready(function(){

  // focus on prompt
  document.getElementById('input_prompt').focus();

  $(document).click(function () {
    document.getElementById('input_prompt').focus();
  });

  $(document.body).keydown(function (e) {
    switch(e.which) {
      case 38: // arrow key up
        $.getJSON('ajax/history_up', function(data) {
          $('#input_prompt').attr('value', data.history);
        });
        break;
      case 40: // arrow key down
        $.getJSON('ajax/history_down', function(data) {
          $('#input_prompt').attr('value', data.history);
        });
        break;
      case 9: // tab key
        var value = $('#input_prompt').attr('value');
        $.getJSON('ajax/completion', { complete: value }, function(data) {
          if(data.count == 1) {
            $('#input_prompt').attr('value', data.completion);
            $('#completion').html('');
          }
          else {
            $('#completion').html(data.completion);
          }
          document.getElementById('input_prompt').focus();
        });
        break;
    }
  });

});
