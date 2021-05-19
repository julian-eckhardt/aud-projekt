<template>
  <div id="chart-container">
    <fusioncharts
      :type="type"
      :width="width"
      :height="height"
      :dataformat="dataFormat"
      :data-source="dataSource"
    >
    </fusioncharts>
  </div>
</template>

<script>
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

const dataSource = {
  chart: {
    caption: 'Covid Fallzahlen',
    subcaption: 'Gesamtfallzahlen',
    series: 'index',
    xaxisname: 'Datum',
    yaxisname: 'Fallzahlen in 1000',
    numbersuffix: 'K',
    theme: 'fusion',
  },
  data: jsonData,
}

export default {
  data() {
    return {
      type: 'line',
      renderAt: 'chart-container',
      width: '550',
      height: '350',
      dataFormat: 'json',
      dataSource,
    }
  },
}
</script>
