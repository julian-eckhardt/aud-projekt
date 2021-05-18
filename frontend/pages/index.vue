<template>
  <div class="container">
    <b-row>
      <b-col class="graphCol">
        <GraphComponent />
      </b-col>
      <b-col class="formCol">
        <b-form class="forms">
          <b-form-group
            id="rReductionValue"
            label="R-Zahl-Reduktion:"
            label-for="rReductionInput"
          >
            <b-form-input
              id="rInput"
              v-model="rReductionValue"
              class="rReductionInput"
              placeholder="Z.B. 1.2"
              required
              type="text"
            />
          </b-form-group>

          <b-form-group
            id="timeFrameStart"
            label="Startzeitpunkt:"
            label-for="timeFrameStartInput"
          >
            <b-form-input
              id="timeFrameStartInput"
              v-model="timeFrameStart"
              placeholder="Datum eingeben"
              type="date"
            />
          </b-form-group>
          <b-form-group
            id="timeFrameEnd"
            label="Endzeitpunkt:"
            label-for="timeFrameEndInput"
          >
            <b-form-input
              id="timeFrameEndInput"
              v-model="timeFrameEnd"
              placeholder="Datum eingeben"
              type="date"
            />
          </b-form-group>
          <b-button variant="primary"> Senden </b-button>
        </b-form>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import GraphComponent from '@/components/GraphComponent.vue'

export default {
  components: {
    GraphComponent,
  },
}
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
