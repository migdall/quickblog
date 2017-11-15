
$(document).ready(function() {
    // Code goes here
    $("#new-post-div").click(function(event) {
        $("#new-post-form").show();
    });

    $(".post-delete-link").click(function(event) {
        var result = confirm("Do you want to delete this post?");
        if (!result) {
            event.preventDefault();
        }
    });
});

