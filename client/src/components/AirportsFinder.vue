<template>
    <div class="column">
        <AirportsMap :coordinates="coordinates"></AirportsMap>
        <AirportsSearch @submit="onSearch"></AirportsSearch>
        <AirportsTable
                v-if="airports && airports.length"
                :airports="airports"
        ></AirportsTable>
    </div>
</template>

<script>
    import airportService from "../_services/airport.service"
    import AirportsTable from "./AirportsTable";
    import AirportsMap from "./AirportsMap";
    import AirportsSearch from "./AirportsSearch";

    export default {
        name: "AirportsFinder",
        components: {
            AirportsTable,
            AirportsMap,
            AirportsSearch
        },
        data() {
            return {
                airports: []
            }
        },
        async mounted() {
            this.airports = await airportService.getAirportsByStateAndRunway("US-ID", "19")
        },
        computed: {
            coordinates() {
                return this.airports.map(airport => ([
                    airport.longitude_deg,
                    airport.latitude_deg,
                ]))
            }
        },
        methods: {
            async onSearch({runway, state}) {
                this.airports = await airportService.getAirportsByStateAndRunway(state, runway)
            }
        }
    }
</script>