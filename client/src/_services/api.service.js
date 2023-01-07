export default {
    request
}

const API_HOST = "http://localhost:8000"

/**
 *
 * @param { string } method
 * @param { string } endpoint
 * @param { object|undefined } params
 * @param { object|undefined } body
 * @returns {Promise<Response>}
 */
async function request(method, endpoint, { params, body } = {}) {
    const requestOptions = {
        method: method.toUpperCase(),
        headers: {"Content-Type": "application/json"}
    };

    if (["POST", "PUT", "DELETE"].includes(method.toUpperCase())) {
        requestOptions.body = JSON.stringify(body);
    }

    let url = buildUrl(endpoint, params)
    return await fetch(url, requestOptions).then(handleResponse);
}


/**
 * Returns the url with the query string
 * @param { string } endpoint
 * @param { object } params
 */
function buildUrl(endpoint, params) {
    if (!params) return endpoint;

    const fullUrl = `${API_HOST}${endpoint}`
    let url = new URL(fullUrl)
    Object.keys(params).forEach(key => url.searchParams.append(key, params[key]))
    return url.toString();
}


function handleResponse(response) {
    return response.text().then(text => {
        const data = text && JSON.parse(`${text}`);
        if (!response.ok) {
            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
        }

        return data;
    });
}
