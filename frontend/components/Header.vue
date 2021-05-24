<template>
  <div>
    <b-navbar class="fixed-top" type="light">
      <b-container fluid>
        <b-navbar-brand>
          <strong>A&amp;D-Projekt</strong> Gruppe 2
        </b-navbar-brand>
        <b-navbar-nav ml-auto>
          <b-nav-item nuxt-link to="/"> Hauptseite </b-nav-item>
        </b-navbar-nav>
      </b-container>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: 'Header',
}
</script>

<style scoped>
.navbar {
  background: #8fd19e;
}

#nav {
  color: #000000;
}

#nav a.router-link-exact-active {
  color: #21392e;
}

.navbar-brand {
  font-size: 1em;
}
</style>
