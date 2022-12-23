import { createStore } from 'vuex'

// Create a new store instance.
const store = createStore({
  state: {
      opt: "Все",
      listOpt: ["Все", "Клиент", "Менеджер", "Отдел продаж", "Тренер", "Ресепшн"]
  },
  getters: {
    option(state) {
      return state.opt;
    },
    listOpt(state) {
      return state.listOpt;
    }
  },
  mutations: {
    changeState (state, payload) {
      state.opt = payload.opt;
    }
  }
})

export default store