<template>
  <div>
    <b-container class="headerCont" fluid>
      <div id="nav">
        <b-navbar class="navBar fixed-top" type="light">
          <b-navbar-nav>
            <b-nav-item nuxt-link to="/"> Hauptseite </b-nav-item>
            <b-nav-item nuxt-link to="/about"> Über </b-nav-item>
            <b-nav-item nuxt-link to="/help"> Hilfe </b-nav-item>
          </b-navbar-nav>
        </b-navbar>
      </div>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'Header',
}
</script>

<style scoped>
.navBar {
  background: #8fd19e;
}

#nav {
  color: #000000;
}

#nav a.router-link-exact-active {
  color: #21392e;
}

.headerCont {
  margin-bottom: 5vh;
}
</style>
