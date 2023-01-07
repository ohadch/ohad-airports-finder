<template>
    <div class="card">
        <div class="card-content">
            <b-table
                    :columns="columns"
                    :data="airports"
            ></b-table>
        </div>
    </div>
</template>

<script>

    export default {
        name: "AirportsTable",
        data() {
            return {
                columns: [
                    {label: 'ICAO', field: 'ident'},
                    {label: 'Latitude', field: 'latitude_deg'},
                    {label: 'Longitude', field: 'longitude_deg'}
                ],
            }
        },
        props: {
            airports: {
                type: Array,
                required: true
            }
        }
    }
</script>

<style>
    table {
        width: 50%;
        margin-left: auto;
        margin-right: auto;
    }
</style>