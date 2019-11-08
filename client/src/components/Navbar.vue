<template>
    <b-menu>
        <b-menu-list label="Month">
          <b-datepicker
                :placeholder="date"
                icon="calendar-today">
            </b-datepicker>
                  </b-menu-list>

        <b-menu-list label="Actions">
          <b-menu-item
            label="About"
            icon="link"
            tag="router-link"
            to="/about">
          </b-menu-item>
        </b-menu-list>
    </b-menu>
    
<!-- 
<template>
  <ul class="navbar" id="navbar">
    <li><router-link to="/logout">logout</router-link></li>
    <li><router-link to="/about">about</router-link></li>
  </ul>
</template> -->

</template>

<script>
    export default {
      name: "Navbar",
      data() {
            return {
                isActive: true,
                days: []
            }
        },
      computed: {
        date: function() {
          var months = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
          return new Date();
        }
      }
    }
</script>

