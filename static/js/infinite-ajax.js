$(document).ready(function () {
    $('#like_btn').click(function () {
        var gameIdVar;
        gameIdVar = $(this).attr('data-gameid');
        $.get('/infinite/like_game/',
            { 'game_id': gameIdVar },
            function (data) {
                $('#like_count').html(data);
                $('#like_btn').hide();
            })
    });
});
