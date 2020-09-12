let results = null;

$(".albumAutoComplete").autoComplete({
    resolver: "ajax",
    resolverSettings: {
        url: window.location.origin + "/albums/",
        requestThrottling: 700,
    },
    events: {
        searchPost: function (resultFromServer) {
            var i = 0;
            return resultFromServer.results.map(x => { return { 
                "value": JSON.stringify({"album": x["album"], "artist": x["artist"], "url": x["url"]}),
                "text": `${x["album"]} — ${x["artist"]}` 
            }; });
        }
    }
});