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
  props: ['updatedData'],
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
        /*
        {
          name: 'Reduzierte_Gesamt',
          type: 'number',
        },
        */
      ],
      jsonData: [],
    }
  },
  computed: {
    formattedData() {
      if (this.updatedData.length === 0) {
        return this.jsonData.map((entry) => {
          return {
            ...entry,
            index: entry.index.substring(0, 10),
          }
        })
      } else {
        return this.updatedData.map((entry) => {
          return {
            ...entry,
            index: entry.index.substring(0, 10),
          }
        })
      }
    },
  },
  async mounted() {
    try {
      this.jsonData = await this.$axios.$get('/test')
    } catch (err) {
      // NOOP
    }
    const FusionCharts = require('fusioncharts')

    const fusionTable = new FusionCharts.DataStore().createDataTable(
      this.formattedData,
      this.schema
    )
    this.dataSource.data = fusionTable
  },
}
</script>

<style scoped>
#chart-container {
  height: 70vh;
}
</style>
