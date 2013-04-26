$(function() {
    var the_data = [[1366963683000, 3111.203125], [1366963684000, 3110.49609375], [1366963834000, 3087.91796875], [1366964669000, 3050.40234375], [1366964670000, 3050.2265625], [1366996322000, 3178.140625], [1366996370000, 3174.7734375], [1366996790000, 3171.703125]];

    var memory_data = [
        {data: the_data,
         label: "Available memory (MB)"},
    ];

    $.plot("#memoryplaceholder", memory_data, {
	xaxis: { mode: "time" },
	legend: {
	    position: "se",
	    show: true,
            margin: [10, 10]
	}
    });
});
