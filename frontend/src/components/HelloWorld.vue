<template>
  <v-data-table
    dark
    :headers="headers"
    :items="items"
    class="elevation-1"
    :items-per-page="9"
    :search="search"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>Network Seed</v-toolbar-title>
        <v-divider
          class="mx-3"
          inset
          vertical
        ></v-divider>
        <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
        <v-spacer></v-spacer>
        <v-dialog
          v-model="dialog"
          max-width="400px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="rgb(150, 150, 150)"
              dark
              class="mb-2"
              v-bind="attrs"
              v-on="on"
            >
              New Device
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col
                    cols="12"
                    sm="6"
                    md="5"
                  >
                    <v-text-field
                      v-model="editedItem.name"
                      label="name"
                    ></v-text-field>
                  </v-col>
                  <v-divider inset></v-divider>
                  <v-col
                    cols="12"
                    sm="6"
                    md="5"
                  >
                    <v-text-field 
                      v-model="editedItem.ip"
                      label="ip"
                    ></v-text-field>
                  </v-col>
             
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="blue darken-1"
                text
                @click="close"
              >
                Cancel
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="save"
              >
                Save
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
              <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
        <template v-slot:[`item.connections`]="{ item }">
               <v-btn
               color="rgb(150, 150, 150)"
              dark
              class="mb-1;mt-1"
              @click="deleteItem(item)"
            >
              Ping
            </v-btn>
            <v-btn
            color="rgb(150, 150, 150)"
              dark
              class="mb-1;mt-1"
              style = "margin-left: 5%"
              @click="deleteItem(item)"
            >
              SNMP
            </v-btn>
            <v-btn
            color="rgb(150, 150, 150)"
              dark
              class="mb-1;mt-1"
              style = "margin-left: 5%"
              @click="deleteItem(item)"
              v-if="item.status== 'Unmanaged'"
            >
              Manage
            </v-btn>
            <v-btn
            color="rgb(150, 150, 150)"
              dark
              class="mb-1;mt-1"
              style = "margin-left: 5%"
              @click="deleteItem(item)"
              v-if="item.status== 'Managed'"
            >
              Unmanage
            </v-btn>
    </template>
    <template v-slot:[`item.actions`]="{ item }">
      <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
        v-if="item.status== 'New'"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        small
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
      
    </template>

    <template v-slot:no-data>
      <v-btn
        color="primary"
        @click="deleteItem(item)"
      >
        Reset
      </v-btn>
    </template>
  </v-data-table>
</template>
<script>


import Vue from 'vue'
import axios from 'axios';
import VueAxios from 'vue-axios'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
Vue.use(VueAxios,axios)


// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'


// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

  export default {
    data: () => ({
      search: '',
      dialog: false,
      dialogDelete: false,
      headers: [
        { text: 'Name', value: 'name', align: 'start'},
        { text: 'IP', value: 'ip' },
        { text: 'Status', value: 'status' },
        { text: 'Actions', value: 'connections', sortable: false },
        { text: '', value: 'actions', sortable: false }
       
      ],
      items: undefined,
      editedIndex: -1,
      editedItem: {
        // name: '',
        // calories: 0,
        // fat: 0,
        // carbs: 0,
        // protein: 0,
      },
      defaultItem: {
        // name: '',
        // calories: 0,
        // fat: 0,
        // carbs: 0,
        // protein: 0,
      },
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New Device' : 'Edit Device'
      },
    },

    watch: {
      dialog (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
    },

    created () {
      this.fetchSeed();
      
    },
       mounted()
  {
     this.fetchSeed();
     this.timer = setInterval(this.fetchSeed, 10000);
  },

    methods: {
                  fetchSeed () {
      Vue.axios.get('/getDevices')
    .then((res)=>{
    this.items=res.data;
    console.warn(res.data)
    })
        },
      editItem (item) {
        this.editedIndex = this.items.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        this.editedIndex = this.items.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
      },

      deleteItemConfirm () {
        this.items.splice(this.editedIndex, 1)
        Vue.axios.put('/deleteDevice'+'?name='+this.editedItem.name+'&ip='+this.editedItem.ip)
          .then((res)=>{
          // this.items=res.data;
          console.warn(res.data)
          this.close()
         })
        this.closeDelete()
      },

      close () {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      closeDelete () {
        this.dialogDelete = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      save () {
        if (this.editedIndex > -1) {
          Vue.axios.post('/editDevice'+'?origin='+this.items[this.editedIndex].ip+'&name='+this.editedItem.name+'&ip='+this.editedItem.ip)
          .then((res)=>{
          // this.items=res.data;
          console.warn(res.data)
          this.close()
         })
          Object.assign(this.items[this.editedIndex], this.editedItem)
        } else {
          Vue.axios.put('/addDevice'+'?name='+this.editedItem.name+'&ip='+this.editedItem.ip)
          .then((res)=>{
          // this.items=res.data;
          console.warn(res.data)
          this.close()
         })
          this.items.push(this.editedItem)
        }
        this.close()
      },
    },
  }
</script>

