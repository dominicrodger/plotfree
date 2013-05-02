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

function plotProcesses(series) {
    $.plot(
        "#processesplaceholder",
        series,
        {
            series: {
                pie: {
                    innerRadius: 0.4,
                    show: true,
                    combine: {
                        color: '#999',
                        threshold: 0.02
                    }
                }
            },
            legend:{
                show: false
            }
        }
    );
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
    plot("processes", plotProcesses);
});
