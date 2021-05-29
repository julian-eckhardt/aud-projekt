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
export default {
  props: {
    updatedData: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      type: 'timeseries',
      renderAt: 'chart-container',
      width: '100%',
      height: '100%',
      dataFormat: 'json',
      dataSource: {
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
      },
      schema: [
        {
          name: 'index',
          type: 'date',
          format: '%Y-%m-%d',
        },
        {
          name: 'Gesamt',
          type: 'number',
        },
        {
          name: 'Reduzierte_Gesamt',
          type: 'number',
        },
      ],
    }
  },
  computed: {
    formattedData() {
      return this.updatedData.map((entry) => {
        return {
          ...entry,
          index: entry.index.substring(0, 10),
        }
      })
    },
  },
  watch: {
    formattedData(newData) {
      this.paintGraph()
    },
  },
  mounted() {
    this.paintGraph()
  },
  methods: {
    paintGraph() {
      const FusionCharts = require('fusioncharts')
      this.dataSource.data = new FusionCharts.DataStore().createDataTable(
        this.formattedData,
        this.schema
      )
    },
  },
}
</script>

<style scoped>
#chart-container {
  height: 70vh;
}
</style>
