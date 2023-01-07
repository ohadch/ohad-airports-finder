<template>
    <div id="app">
        <h1 style=" padding: 60px;font-weight: bold; font-size: 2em;">Airport Finder</h1>
        <p>
            Plot any airport in the United States that has a certain runway.
        </p>
        <AirportsFinder/>
        <div class="footer">
            &copy; Ohad Chaet 2020
        </div>
    </div>
</template>

<script>
    import AirportsFinder from './components/AirportsFinder.vue'

    export default {
        name: 'App',
        components: {
            AirportsFinder
        }
    }
</script>

<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        color: #2c3e50;

        text-align: center;
        background: #DEDEDE;
    }

</style>
