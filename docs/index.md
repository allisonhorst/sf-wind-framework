# San Francisco wind 

This example accesses near real-time wind data using R and Python data loaders, and uses GitHub actions to automatically rebuild and deploy to GitHub pages every 2 hours.

**Data:** NOAA Tides and Currents, [CO-OPS API](https://api.tidesandcurrents.noaa.gov/api/prod/)

## Using R data loader 
```js echo
const windR = await FileAttachment("./data/windR.csv").csv({typed: true});
```

```js
// Direction abbreviations in meaninful order
const directions = d3.groupSort(windR, g => d3.median(g, d => d.windDirAngle), d => d.windDirAbb).reverse();
```


```js
display(Inputs.table(windR));
```

```js
const windyRChart = Plot.plot({
  color: {range: ["skyblue", "navy"], 
  interpolate: "hcl"},
  x: {grid: true, label: "Date"},
  y: {grid: true, label: "Wind speed (knots)"},
  marks: [
    Plot.areaY(windR, {x: "Date Time", y: "Speed", fill: "skyblue", opacity: 0.3}),
    Plot.line(windR, {x: "Date Time", y: "Speed", stroke: "skyblue", strokeWidth: 1}),
    Plot.dot(windR, {x: "Date Time", y: "Speed", fill: "Speed", opacity: 0.8}),
    Plot.vector(windR, {x: "Date Time", y: "Speed", length: "Speed", rotate: d => 180 + d.windDirAngle, stroke: "Speed", anchor: "start"})
  ]
});

display(windyRChart);
```

## Using Python data loader

```js echo
const windPy = await FileAttachment("./data/windPy.csv").csv({typed: true});
```

```js
display(Inputs.table(windPy));
```

```js
const windyPyChart = Plot.plot({
  x: {domain: directions, label: "Wind direction"},
  marks: [
    Plot.barY(windPy, Plot.groupX({y: "count"}, {x: "windDirAbb", fill: "navy"})),
    Plot.ruleY([0])
  ]
});

display(windyPyChart);
```
