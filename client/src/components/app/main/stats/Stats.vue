<script>
import Button from '../../../Button.vue'
import Table from '../../../Table.vue'
import HDivider from '../../../HDivider.vue'


export default {
    components: {
        Button,
        Table,
        HDivider
    },
    data() { 
        return {
            text: {
                buttonFit: "Работающие тренера",
                buttonFitPop: "Популярные тренера",
                buttonFitUnPop: "Непопулярные тренера",
                buttonSecPop: "Популярные занятия",
                buttonSecUnPop: "Непопулярные занятия",
                buttonMon: "Данные по зарплате",
                buttonClients: "Клиенты в зоне риска",
                buttonBack: "Назад",
            },
            showItem: {
                Fit: false,
                FitPop: false,
                FitUnPop: false,
                SecPop: false,
                SecUnPop: false,
                Mon: false,
                Clients: false,
                Back: false,
                All: true
            },
            tableHead: [
                "Имя",
                "Фамилия",
                "Отчество",
                "Дата",
                "Время"
            ],
            tableInfo: [{
                name: "Имя 1",
                surname: "Фамилия 1",
                midname: "Отчество 1",
                date: "01.12.2022",
                time: "15:30"
            }, 
            {
                name: "Имя 2",
                surname: "Фамилия 2",
                midname: "Отчество 2",
                date: "01.12.2022",
                time: "15:45"
            }],
        }
    },
    methods: {
        btnFit() {
            this.showItem.Fit = true;
            this.showItem.All = false;
        },
        btnFitPop() {
            this.showItem.FitPop = true;
            this.showItem.All = false;
        },
        btnFitUnPop() {
            this.showItem.FitUnPop = true;
            this.showItem.All = false;
        },
        btnSecPop() {
            this.showItem.SecPop = true;
            this.showItem.All = false;
        },
        btnSecUnPop() {
            this.showItem.SecUnPop = true;
            this.showItem.All = false;
        },
        btnMon() {
            this.showItem.Mon = true;
            this.showItem.All = false;
        },
        btnClients() {
            this.showItem.Clients = true;
            this.showItem.All = false;
        },
        btnBack() {
            this.showItem = {
                Fit: false,
                FitPop: false,
                FitUnPop: false,
                SecPop: false,
                SecUnPop: false,
                Mon: false,
                Clients: false,
                Back: false,
                All: true
            };
        }
    }
}
</script>

<template>
<div v-if="showItem.All" class="btn-menu">
    <Button :title="text.buttonFit" :func="btnFit"></Button>
    <Button :title="text.buttonFitPop" :func="btnFitPop"></Button>
    <Button :title="text.buttonFitUnPop" :func="btnFitUnPop"></Button>
    <Button :title="text.buttonSecPop" :func="btnSecPop"></Button>
    <Button :title="text.buttonSecUnPop" :func="btnSecUnPop"></Button>
    <Button :title="text.buttonMon" :func="btnMon"></Button>
    <Button :title="text.buttonClients" :func="btnClients"></Button>
</div>

<div v-if="showItem.Fit">
    <form id="fitStat" @submit.prevent="btnSubmitStat">
        <p>
            <label for="date">{{ text.formStatDate }}</label>
            <input id="date" v-model="stat.date" placeholder="**.**.****">
        </p>
    </form>
    <HDivider></HDivider>
    <div>
        <Button class="btn-size" :title="text.buttonBack" :func="btnBack" form=""></Button>
        <Button class="btn-size" :title="text.formStatSubmit" form="fitStat"></Button>
    </div>
    <Button :title="text.buttonBack" :func="btnBack"></Button>
</div>

<div v-if="showItem.FitPop">
    <Button :title="text.buttonBack" :func="btnBack"></Button>
</div>

<div v-if="showItem.FitUnPop">
    <Button :title="text.buttonBack" :func="btnBack"></Button>
</div>

<div v-if="showItem.SecPop">
    <Button :title="text.buttonBack" :func="btnBack"></Button>
</div>

<div v-if="showItem.SecUnPop">
    <Button :title="text.buttonBack" :func="btnBack"></Button>
</div>

<div v-if="showItem.Mon">
    <Button :title="text.buttonBack" :func="btnBack"></Button>
</div>

<div v-if="showItem.Clients">
    <Button :title="text.buttonBack" :func="btnBack"></Button>
</div>

</template>

<style>

.btn-menu {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin-top: 20%;
}

</style>