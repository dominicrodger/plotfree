function onDataReceived(series) {
    $.plot(
        "#memoryplaceholder",
        [series],
        {
            xaxis: { mode: "time" },
            yaxis: { min: 0 },
            legend: {
	        position: "se",
	        show: true,
                margin: [10, 10]
            }
        }
    );
}


$(function() {
    $.ajax({
        url: "/data/memory.json",
        type: "GET",
        dataType: "json",
        success: onDataReceived
    });
});
