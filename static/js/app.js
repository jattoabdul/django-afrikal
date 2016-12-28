$(document).ready(function() {
    $('#openSearch').click(function() {
        $('#searchField').toggleClass('hide');
    });
    $('#searchClose').click(function() {
        $('#searchField').addClass('hide');
    });

    $('#findServices').click(function() {
        $('#searchField').toggleClass('hide');
    });
    // $('#searchClose').click(function() {
    //     $('#searchField').addClass('hide');
    // });
});