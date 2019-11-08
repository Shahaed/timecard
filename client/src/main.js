import 'buefy/dist/buefy.css';
import Vue from 'vue';

import App from './App';
import router from './router';
import store from './store';
import Buefy from 'buefy';

Vue.config.productionTip = false;
Vue.use(Buefy);

export default new Vue({
  router,
  store,
  el: '#app',
  template: '<App/>',
  components: { App },
});
