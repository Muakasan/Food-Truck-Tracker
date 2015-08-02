<script type=text/javascript src="{{url_for('static', filename='ajax.js') }}"></script>

$(function() {
  $().bind('click', function() {
    $.getJSON($SCRIPT_ROOT + '/_add_numbers', {
      a: $('input[name="a"]').val(),
      b: $('input[name="b"]').val()
    }, function(data) {
      $("#result").text(data.result);
    });
    return false;
  });
});