<template>
  <div>
    <b-container class="footerCont" fluid>
      <b-row>
        <b-col />
        <b-col>
          <h5>Pages</h5>
          <b-nav type="light" vertical>
            <b-nav-item nuxt-link to="/about"> Über </b-nav-item>
            <b-nav-item nuxt-link to="/help"> Hilfe </b-nav-item>
          </b-nav>
        </b-col>
        <b-col />
        <b-col />
        <b-col>
          <h5>Terms</h5>
          <b-nav type="light" vertical>
            <b-nav-item nuxt-link to="/terms"> AGB </b-nav-item>
            <b-nav-item nuxt-link to="/privacy">
              Datenschutzerklärung
            </b-nav-item>
          </b-nav>
        </b-col>
        <b-col />
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'Footer',
}
</script>

<style scoped>
.footerCont {
  background-color: #8fd19e;
  padding: 5vh;
}
</style>
