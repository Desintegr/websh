$(document).ready(function(){

  // focus on prompt
  document.getElementById('input_prompt').focus();

  $(document).click(function () {
    document.getElementById('input_prompt').focus();
  });

  $(document.body).keydown(function (e) {
    switch(e.which) {
      case 38: // arrow key up
        $.get('ajax/history_up', function(data) {
          $('#input_prompt').attr('value', data);
        });
        break;
      case 40: // arrow key down
        $.get('ajax/history_down', function(data) {
          $('#input_prompt').attr('value', data);
        });
        break;
    }
  });

});
