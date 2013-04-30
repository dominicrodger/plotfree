var options = {
    xaxis: {
        mode: "time",
        timezone: "browser"
    },
    yaxis: {
        min: 0
    },
    legend: {
	position: "se",
	show: true,
        margin: [10, 10]
    },
    series: {
        lines: { show: true },
        points: { show: true }
    }
}

function renderPlot(series, selector) {
    $.plot(
        selector,
        [series],
        options
    );
}

function plotMemory(series) {
    renderPlot(series, "#memoryplaceholder");
}


$(function() {
    $.ajax({
        url: "/data/memory.json",
        type: "GET",
        dataType: "json",
        success: plotMemory
    });
});
