import apiService from "./api.service";

export default {
    getAirportsByStateAndRunway
}


async function getAirportsByStateAndRunway(usState, runway) {
    const { airports } = await apiService.request("GET", "/api/airports", {
        params: {
            us_state: usState,
            runway
        }
    })

    return airports.map(airport => ({
        ...airport,
        latitude_deg: +airport.latitude_deg,
        longitude_deg: +airport.longitude_deg,
    }));
}