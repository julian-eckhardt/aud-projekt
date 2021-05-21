<template>
  <div id="chart-container">
    <fusioncharts
      :type="type"
      :width="width"
      :height="height"
      :data-format="dataFormat"
      :data-source="dataSource"
    >
    </fusioncharts>
  </div>
</template>

<script>
const jsonSchema = [
  {
    name: 'index',
    type: 'date',
    format: '%Y-%d-%m',
  },
  {
    name: 'Gesamt',
    type: 'number',
  },
  {
    name: 'Reduzierte_Gesamt',
    type: 'number',
  },
]

const jsonData = [
  {
    index: '2020-05-06',
    Gesamt: 5980,
    Reduzierte_Gesamt: 5120,
  },
  {
    index: '2020-05-07',
    Gesamt: 5705,
    Reduzierte_Gesamt: 5090,
  },
  {
    index: '2020-05-08',
    Gesamt: 5394,
    Reduzierte_Gesamt: 5001,
  },
  {
    index: '2020-05-09',
    Gesamt: 5703,
    Reduzierte_Gesamt: 4120,
  },
  {
    index: '2020-05-10',
    Gesamt: 5715,
    Reduzierte_Gesamt: 3120,
  },
]

const dataSource = {
  chart: {
    caption: 'Covid Fallzahlen',
    subcaption: 'Gesamtfallzahlen',
    series: 'index',
    xaxisname: 'Datum',
    yaxisname: 'Fallzahlen in 1000',
    numbersuffix: 'K',
    theme: 'fusion',
    yAxis: [
      {
        plot: [
          {
            value: 'Gesamt',
            type: 'line',
          },
          {
            value: 'Reduzierte_Gesamt',
            type: 'column',
          },
        ],
      },
    ],
  },
  data: null,
}

export default {
  data() {
    return {
      type: 'timeseries',
      renderAt: 'chart-container',
      width: '550',
      height: '550',
      dataFormat: 'json',
      dataSource,
    }
  },
  mounted() {
    const FusionCharts = require('fusioncharts')

    const data = jsonData
    const schema = jsonSchema
    const fusionTable = new FusionCharts.DataStore().createDataTable(
      data,
      schema
    )
    this.dataSource.data = fusionTable
  },
}
</script>
