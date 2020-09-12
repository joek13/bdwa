var parts = window.location.pathname.split("/");
var templateId = parts[parts.length - 1];

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function vote(by) {
    var url = `${window.location.origin}/api/vote_listing/${templateId}/${by}`;
    console.log(url);
    $.ajax(url, {
        "method": "POST",
        "headers": {
            "X-CSRFToken": csrftoken
        }
    }).done((res) => {
        $("#listing-score").html(res["new_score"]);
    });
}

$(".vote-up").click((e) => {
    // vote up
    vote(1);
});

$(".vote-down").click((e) => {
    // vote up
    vote(2);
});
