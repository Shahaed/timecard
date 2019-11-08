
<template>
  <div>
    <Topbar/>
    <div class="columns left">
      <div class="column is-one-fifth">
        <Navbar/>
      </div>
      <div class="column is-four-fifths">
        <SubmitTime/>
        <br>
        <h1>{{info}}</h1>
      </div>
    </div>
  </div>
</template>

<script>
import SubmitTime from '../views/SubmitTime';
import Navbar from '../components/Navbar'
import Topbar from '../components/Topbar'
import axios from 'axios'

export default {
  name: 'home',
  components: {
    SubmitTime,
    Navbar,
    Topbar
  },
  data() {
    return {
      info: "Waiting..."
    }
  },
  mounted () {
    axios
      .get('https://368876ac.ngrok.io/')
      .then(response => (this.info = response.data[0]))
  }

};
</script>

<style>
.left {
  margin-top: .5%;
  margin-left: 5%;
  margin-right: 5%;
}
</style>