$(function() {
    function submit() {
        $.getJSON($SCRIPT_ROOT + '/addition', {
                a: $('input[name="a"]').val(),
                b: $('input[name="b"]').val()
            },
            function(data) {
                $("#result").html(data.result);
            });
    };
   $("#txt").click(function() {
        var txt;
        $.ajax({
            url: "/test",

            async: false,
            success:function(data){
              txt=data;
              $("#mesg").html(data.result[0]+data.result[1]);
            }
            });

    });

   $("#about").click(function() {
        window.location.href="about"
    });


$('#calculate').bind('click', submit);

});