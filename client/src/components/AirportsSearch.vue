<template>
    <form @submit.prevent="onSubmit" style="margin-top: 15px;">
        <nav class="level">
            <div class="level-item has-text-centered">
                <b-field label="US State">
                <b-input v-model="state" value="US-ID" maxlength="5"></b-input>
            </b-field>

            <b-field label="Runway">
                <b-input v-model="runway" value="19" maxlength="3"></b-input>
            </b-field>
            <b-button type="is-primary" native-type="submit">Search</b-button>
            </div>
        </nav>
    </form>
</template>

<script>
    export default {
        name: "AirportsSearch",
        data() {
            return {
                state: "US-ID",
                runway: "19"
            }
        },
        methods: {
            onSubmit() {
                const {state, runway} = this;
                this.$emit("submit", {
                    state,
                    runway
                })
            }
        }
    }
</script>

<style scoped>

</style>