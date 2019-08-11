<template>
  <div class="pa4 mw6">
    <div>
      <h1 class="title">{{user_name}}</h1>
      <h2 class="subtitle" @click="fetchData">{{user_age}}</h2>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user_age: "",
      user_name: "",
      interval: null
    };
  },
  methods: {
    fetchData: function() {
      this.$axios.$get("http://localhost:5000/api").then(res => {
        console.log(res.user);
        this.user_age = res.user.age;
        this.user_name = res.user.name;
      });
    }
  },
  mounted() {
    this.fetchData();
    this.interval = setInterval(
      function() {
        this.fetchData();
      }.bind(this),
      10000
    );
  },
  destroyed() {
    clearInterval(this.interval);
  }
};
</script>

