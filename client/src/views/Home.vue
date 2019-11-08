
<template>
  <div>
    <hr />
    <form action="#" method="POST"></form>
    <div class="container">
      <div class="rows">
        <div class="row is-full"></div>
        <div class="row is-full">
          <div class="columns">
            <div class="column is-5">
              <b-autocomplete
                rounded
                v-model="name"
                :data="filteredDataArray"
                placeholder="e.g. Deere"
                icon="magnify"
                @select="option => selected = option"
              >
                <template slot="empty">No results found</template>
              </b-autocomplete>
            </div>
            <div class="column is-3">
              <b-clockpicker
                rounded
                placeholder="Click to select..."
                icon="clock"
                v-model="start_time"
              ></b-clockpicker>
            </div>
            <div class="column is-3">
              <b-clockpicker
                rounded
                placeholder="Click to select..."
                icon="clock"
                v-model="time_end"
              ></b-clockpicker>
            </div>
            <div class="column is-3">
              <b-button @click="clickMe()">Submit</b-button>
            </div>
          </div>
        </div>
        <div class="row is-full"></div>
      </div>
    </div>
  </div>
</template>

<script>
import Autocomplete from "../components/Autocomplete";
export default {
  name: "home",
  components: {
    Autocomplete
  },

  data() {
    return {
      tasks: [],
      data: ["Deere", "Fedex", "IDT", "SIL", "EFS"],
      name: "",
      start_time: "",
      time_end: "",
      selected: null
    };
  },
  methods: {
    clickMe() {
      this.tasks.push({
        deliverable: this.name,
        st: this.start_time,
        et: this.time_end
      });
      console.log(this.tasks);
    }
  },
  computed: {
    filteredDataArray() {
      return this.data.filter(option => {
        return (
          option
            .toString()
            .toLowerCase()
            .indexOf(this.name.toLowerCase()) >= 0
        );
      });
    }
  }
};
</script>
