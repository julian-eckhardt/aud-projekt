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
    graphData: {
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
        series: 'Type',
        chart: {
          caption: 'Covid Fallzahlen',
          subcaption: 'Gesamtfallzahlen',
          xaxisname: 'Datum',
          yaxisname: 'Fallzahlen in 1000',
          numbersuffix: 'K',
          theme: 'fusion',
          yAxis: [
            {
              plot: [
                {
                  value: 'Fallzahlen',
                  title: 'Fallzahlen',
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
          name: 'Fallzahlen',
          type: 'number',
        },
        {
          name: 'Type',
          type: 'string',
        },
      ],
    }
  },
  computed: {
    /**
     * cut timestamps from ISO format into YYYY-MM-DD
     */
    formattedData() {
      return this.graphData.map((entry) => {
        return {
          ...entry,
          index: entry.index.substring(0, 10),
        }
      })
    },
  },
  watch: {
    /**
     * trigger fusion charts refresh when formattedData is updated
     */
    formattedData(newData) {
      this.paintGraph()
    },
  },
  mounted() {
    // paint graph when component is mounted
    this.paintGraph()
  },
  methods: {
    /**
     * paint the graph
     */
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
