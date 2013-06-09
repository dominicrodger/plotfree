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
    var options = {
        series: {
            pie: {
                innerRadius: 0.4,
                show: true,
                combine: {
                    threshold: 0.02
                }
            }
        },
        legend:{
            show: false
        }
    };

    options.colors = $.map(series, function(o, i) {
        return jQuery.Color({ hue: (i*200/series.length), saturation: 0.95, lightness: 0.35, alpha: 1 }).toHexString();
    });

    $.plot(
        "#processesplaceholder",
        series,
        options
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
