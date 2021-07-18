<template>
  <div>
    <b-container fluid>
      <b-row>
        <!-- GRAPH COL -->
        <b-col cols="9">
          <client-only>
            <GraphComponent :graph-data="graphData" />
          </client-only>
        </b-col>

        <!-- PARAMETER FORM COL -->
        <b-col class="formCol" cols="3">
          <b-card header="Parametereingabe">
            <b-card-text>
              <b-form class="forms" @submit.prevent="updateData()">
                <b-form-group
                  id="state"
                  label="Bundesland:"
                  label-for="state-input"
                >
                  <b-form-select
                    v-model="state"
                    :options="statesOptions"
                  ></b-form-select>
                </b-form-group>
                <b-form-group
                  id="rReductionValue"
                  label="Reduktion:"
                  label-for="rReductionInput"
                >
                  <b-form-input
                    id="rInput"
                    v-model="rReductionValue"
                    type="range"
                    min="0"
                    max="250"
                    class="rReductionInput"
                    placeholder="z.B. 0.8"
                    required
                  />
                  <b-form-info> {{ rReductionPercent }}% </b-form-info>
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
                <b-button
                  variant="primary"
                  class="float-right"
                  @click="updateData()"
                  >Aktualisieren</b-button
                >
              </b-form>
            </b-card-text>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import GraphComponent from '@/components/GraphComponent.vue'

export default {
  components: {
    GraphComponent,
  },
  async asyncData({ $axios }) {
    // get states from server
    let states = await $axios.$get(`/bundeslaender`)

    // move "Gesamt" to states list head
    states = states.filter((land) => land !== 'Gesamt')
    states.unshift('Gesamt')

    // what is returned here gets moved into data
    return {
      states,
      state: states[0],
      timeFrameStart: null,
      timeFrameEnd: null,
      rReductionValue: 0,
      graphData: [],
    }
  },
  computed: {
    /**
     * Provide states, as needed by the selection dropdown
     */
    statesOptions() {
      return this.states.map((land) => {
        return {
          value: land,
          text: land,
        }
      })
    },
    /**
     * Reduction value, converted to decimal
     */
    rReductionDecimal() {
      return this.rReductionValue / 1000
    },
    /**
     * Reduction value, converted to percent
     */
    rReductionPercent() {
      return this.rReductionValue / 10
    },
  },
  async mounted() {
    await this.updateData()
  },
  methods: {
    /**
     * Updates the graph
     */
    async updateData() {
      const params = {
        bundesland: this.state !== 'Gesamt' ? this.state : null,
        timeFrameStart: this.timeFrameStart,
        timeFrameEnd: this.timeFrameEnd,
        rReductionValue: this.rReductionDecimal ? this.rReductionDecimal : null,
      }
      try {
        // build query string: drop
        const queryString = Object.keys(params)
          .filter((key) => params[key] != null)
          .map((key) => {
            return `${encodeURIComponent(key)}=${encodeURIComponent(
              params[key]
            )}`
          })
          .join('&')
        this.graphData = await this.$axios
          .get(`/data?${queryString}`)
          .then((response) => response.data)
      } catch (e) {
        alert(e.toString())
      }
    },
  },
}
</script>
