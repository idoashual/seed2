import 'bootstrap/dist/css/bootstrap.css';
import axios from 'axios';
import Vue from 'vue'
import App from './App.vue'
import router from './router';
import vuetify from './plugins/vuetify'

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8080/';

Vue.config.productionTip = false

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app');