<template>
  <b-container fluid class="mt-5">
    <b-row>
      <b-col class="graphCol" cols="10">
        <client-only>
          <GraphComponent />
        </client-only>
      </b-col>
      <b-col class="formCol" cols="2">
        <b-card class="bg-light">
          <h3>Parametereingabe</h3>
          <b-form class="forms mt-4">
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
            <b-button variant="primary" class="float-right"
              >Aktualisieren</b-button
            >
          </b-form>
        </b-card>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import GraphComponent from '@/components/GraphComponent.vue'

export default {
  components: {
    GraphComponent,
  },
  data() {
    return {
      timeFrameStart: null,
      timeFrameEnd: null,
      rReductionValue: null,
    }
  },
}
</script>

<style>
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
