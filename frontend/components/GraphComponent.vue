<template>
  <div id="d3-graph"></div>
</template>

<script>
import * as d3 from 'd3'

export default {
  mounted() {
    this.drawGraph()
  },
  methods: {
    drawGraph() {
      const width = 500
      const height = 500
      const margin = { top: 40, right: 40, bottom: 40, left: 40 }

      const jsonData = [
        {
          index: '2020-05-06T00:00:00.000Z',
          'Baden-Württemberg': 908,
          Bayern: 1318,
          Berlin: 276,
          Brandenburg: 125,
          Bremen: 119,
          Hamburg: 95,
          Hessen: 447,
          'Mecklenburg-Vorpommern': 23,
          Niedersachsen: 361,
          'Nordrhein-Westfalen': 1465,
          'Rheinland-Pfalz': 208,
          Saarland: 94,
          Sachsen: 149,
          'Sachsen-Anhalt': 54,
          'Schleswig-Holstein': 140,
          Thüringen: 198,
          Gesamt: 5980,
        },
        {
          index: '2020-05-07T00:00:00.000Z',
          'Baden-Württemberg': 779,
          Bayern: 1246,
          Berlin: 265,
          Brandenburg: 116,
          Bremen: 126,
          Hamburg: 85,
          Hessen: 420,
          'Mecklenburg-Vorpommern': 23,
          Niedersachsen: 350,
          'Nordrhein-Westfalen': 1498,
          'Rheinland-Pfalz': 176,
          Saarland: 87,
          Sachsen: 162,
          'Sachsen-Anhalt': 50,
          'Schleswig-Holstein': 142,
          Thüringen: 180,
          Gesamt: 5705,
        },
        {
          index: '2020-05-08T00:00:00.000Z',
          'Baden-Württemberg': 665,
          Bayern: 1182,
          Berlin: 272,
          Brandenburg: 117,
          Bremen: 140,
          Hamburg: 86,
          Hessen: 424,
          'Mecklenburg-Vorpommern': 22,
          Niedersachsen: 351,
          'Nordrhein-Westfalen': 1379,
          'Rheinland-Pfalz': 157,
          Saarland: 64,
          Sachsen: 155,
          'Sachsen-Anhalt': 52,
          'Schleswig-Holstein': 149,
          Thüringen: 179,
          Gesamt: 5394,
        },
        {
          index: '2020-05-09T00:00:00.000Z',
          'Baden-Württemberg': 706,
          Bayern: 1223,
          Berlin: 280,
          Brandenburg: 131,
          Bremen: 155,
          Hamburg: 89,
          Hessen: 415,
          'Mecklenburg-Vorpommern': 22,
          Niedersachsen: 430,
          'Nordrhein-Westfalen': 1448,
          'Rheinland-Pfalz': 159,
          Saarland: 55,
          Sachsen: 170,
          'Sachsen-Anhalt': 60,
          'Schleswig-Holstein': 174,
          Thüringen: 186,
          Gesamt: 5703,
        },
        {
          index: '2020-05-10T00:00:00.000Z',
          'Baden-Württemberg': 772,
          Bayern: 1148,
          Berlin: 269,
          Brandenburg: 118,
          Bremen: 170,
          Hamburg: 80,
          Hessen: 456,
          'Mecklenburg-Vorpommern': 24,
          Niedersachsen: 417,
          'Nordrhein-Westfalen': 1449,
          'Rheinland-Pfalz': 149,
          Saarland: 52,
          Sachsen: 163,
          'Sachsen-Anhalt': 58,
          'Schleswig-Holstein': 202,
          Thüringen: 188,
          Gesamt: 5715,
        },
      ]

      const x = d3
        .scaleTime()
        .domain([
          new Date(jsonData[0].index),
          d3.timeDay.offset(new Date(jsonData[jsonData.length - 1].index), 1),
        ])
        .rangeRound([0, width - margin.left - margin.right])

      const y = d3
        .scaleLinear()
        .domain([
          0,
          d3.max(jsonData, function (d) {
            return d.Gesamt
          }),
        ])
        .range([height - margin.top - margin.bottom, 0])

      const xAxis = d3
        .axisBottom(x)
        .tickFormat(d3.timeFormat('%-m/%-d/%Y'))
        .tickPadding(8)

      const yAxis = d3.axisLeft(y).tickPadding(8)

      const svg = d3
        .selectAll('#d3-graph')
        .data(jsonData)
        .append('svg')
        .attr('width', width)
        .attr('height', height)
        .append('g')
        .attr('transform', 'translate(' + margin.left + ', ' + margin.top + ')')

      const line = d3
        .line()
        .x((d) => x(d.index))
        .y((d) => y(d.Gesamt))

      svg
        .select('#d3-graph')
        .attr('x', function (d) {
          return x(new Date(d.index))
        })
        .attr('y', function (d) {
          return (
            height -
            margin.top -
            margin.bottom -
            (height - margin.top - margin.bottom - y(d.Gesamt))
          )
        })
        .attr('width', 10)
        .attr('height', function (d) {
          return height - margin.top - margin.bottom - y(d.Gesamt)
        })

      svg
        .append('g')
        .attr('class', 'x axis')
        .attr(
          'transform',
          'translate(0, ' + (height - margin.top - margin.bottom) + ')'
        )
        .call(xAxis)

      svg.append('g').attr('class', 'y axis').call(yAxis)

      svg
        .selectAll('#d3-graph')
        .data(jsonData)
        .enter()
        .append('path')
        .attr('d', function (d) {
          return line(d.Gesamt)
        })
        .attr('stroke', 'steelblue')
        .attr('stroke-width', 1.5)
        .attr('stroke-linejoin', 'round')
        .attr('stroke-linecap', 'round')
    },
  },
}
</script>
