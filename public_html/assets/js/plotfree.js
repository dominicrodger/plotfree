var options = {
    xaxis: {
        mode: "time",
        minTickSize: [1, "day"],
        timezone: "browser"
    },
    legend: {
	position: "se",
	show: true,
        margin: [10, 10]
    },
    series: {
        lines: { show: true }
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


function plotDisk(series) {
    renderPlot(series, "#diskplaceholder");
}

function plot(filename, callback) {
    $.ajax({
        url: "/data/" + filename + ".json",
        type: "GET",
        dataType: "json",
        success: callback
    });
}

$(function() {
    plot("memory", plotMemory);
    plot("disk", plotDisk);
});
