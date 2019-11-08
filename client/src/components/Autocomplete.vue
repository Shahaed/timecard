<template>
  <section>
    <!-- <p class="content"> -->
      <!-- <b>Select project:</b> -->
      <!-- {{ selected }} -->
    <!-- </p> -->
    <!-- <b-field label="Select project"> -->
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
    </b-field>
  </section>
</template>

<script>
export default {
  data() {
    return {
      data: ["Deere", "Fedex", "IDT", "SIL", "EFS"],
      name: "",
      selected: null
    };
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

