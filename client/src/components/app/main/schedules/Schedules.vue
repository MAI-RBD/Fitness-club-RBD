<script>
import Button from '../../../Button.vue'
import Table from '../../../Table.vue'

export default {
    components: {
        Table
    },
    data() {
        return {
            tableHead: [
                "Название",
                "Тип",
                "Дата",
                "Время"
            ],
            tableInfo: [{
                name: "Какое-то название 1",
                type: "Какой-то тип 1",
                date: "01.12.2022",
                time: "15:30"
            }, 
            {
                name: "Какое-то название 2",
                type: "Какой-то тип 2",
                date: "02.12.2022",
                time: "16:20"
            }],
        }
    },
    methods: {
        updateTable() {
            console.log("Update button call!");
            return null;
        }
    }
}

</script>

<template>
    <Table :back-btn="false" :update-func="updateTable" :table-head="tableHead" :table-info="tableInfo"></Table>
</template>

<style>

table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #969696;
  text-align: left; 
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #3f3f3f;
}

</style>