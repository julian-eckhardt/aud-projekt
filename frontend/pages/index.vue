<template>
  <div>
    <b-container fluid>
      <b-row>
        <!-- GRAPH COL -->
        <b-col cols="9">
          <client-only>
            <GraphComponent />
          </client-only>
        </b-col>

        <!-- PARAMETER FORM COL -->
        <b-col class="formCol" cols="3">
          <b-card header="Parametereingabe">
            <b-card-text>
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
                    placeholder="z.B. 1.2"
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
  data() {
    return {
      timeFrameStart: null,
      timeFrameEnd: null,
      rReductionValue: null,
    }
  },
}
</script>

<style></style>
