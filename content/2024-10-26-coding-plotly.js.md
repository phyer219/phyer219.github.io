---
title: 在博客中嵌入 JavaScript 之 Plotly.js
date: 2024/10/26
categories: 软件使用
tags: [javascript, plotly]
---

<script src="https://unpkg.com/mathjs@13.2.0/lib/browser/math.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/plotly.js/2.35.0/plotly.min.js"></script>


<form id="form", class="img-like">
  <label for="eq">Enter an equation: f(x)=</label>
  <input type="text" id="eq" value="sin(x)" />
  <input type="submit" value="Draw" />
</form>

<div id="plot" class="img-like"></div>

<script>

        window.MathJax.loader = { load: ['output/svg'] };
        window.MathJax.startup = {
            ready() {
                MathJax.startup.defaultReady();
                draw("plot");
            }
        }

async function draw(idToPlot) {
    try {
        // compile the expression once
        const expression = document.getElementById('eq').value;
        const expr = math.compile(expression);

        // evaluate the expression repeatedly for different values of x
        const xValues = math.range(-10, 10, 0.1).toArray();
        const yValues = xValues.map(function (x) {
            return expr.evaluate({ x: x })
        });

        // render the plot using plotly
        const trace1 = {
            x: xValues,
            y: yValues,
            type: 'scatter'
        };
        const layout = {
            title: 'Plot Example',
            xaxis: {title: {text: '$x$'},
			        showgrid: false,
					// linecolor: 'blue',
					// zerolinecolor: 'red'
					},
            yaxis: {title: {text: '$f(x)$'}, showgrid: false},
			paper_bgcolor: "rgba(255, 200, 200, 0)",
			plot_bgcolor: "rgba(200, 200, 255, 0)",
			gridcolor:"rgba(0, 0, 255, 1)",
			autosize: true
        };
        const config = {
            responsive: false,
        };

		await Plotly.newPlot(idToPlot, [trace1], layout, config);
        MathJax.typesetPromise();
    }
    catch (err) {
        console.error(err)
        alert(err)
    }
};

document.getElementById('form').onsubmit = function (event) {
    event.preventDefault()
    draw("plot")
};
</script>


## JavaScript Code

```javascript

        window.MathJax.loader = { load: ['output/svg'] };
        window.MathJax.startup = {
            ready() {
                MathJax.startup.defaultReady();
                draw("plot");
            }
        }

async function draw(idToPlot) {
    try {
        // compile the expression once
        const expression = document.getElementById('eq').value;
        const expr = math.compile(expression);

        // evaluate the expression repeatedly for different values of x
        const xValues = math.range(-10, 10, 0.1).toArray();
        const yValues = xValues.map(function (x) {
            return expr.evaluate({ x: x })
        });

        // render the plot using plotly
        const trace1 = {
            x: xValues,
            y: yValues,
            type: 'scatter'
        };
        const layout = {
            title: 'Plot Example',
            xaxis: {title: {text: '$x$'},
			        showgrid: false,
					// linecolor: 'blue',
					// zerolinecolor: 'red'
					},
            yaxis: {title: {text: '$f(x)$'}, showgrid: false},
			paper_bgcolor: "rgba(255, 200, 200, 0)",
			plot_bgcolor: "rgba(200, 200, 255, 0)",
			gridcolor:"rgba(0, 0, 255, 1)",
			autosize: true
        };
        const config = {
            responsive: false,
        };

		await Plotly.newPlot(idToPlot, [trace1], layout, config);
        MathJax.typesetPromise();
    }
    catch (err) {
        console.error(err)
        alert(err)
    }
};

document.getElementById('form').onsubmit = function (event) {
    event.preventDefault()
    draw("plot")
};
```

## Reference

- [https://mathjs.org/examples/browser/plot.html.html](https://mathjs.org/examples/browser/plot.html.html)
- [https://github.com/plotly/plotly.js/pull/6073](https://github.com/plotly/plotly.js/pull/6073)
- ChatGPT 4o