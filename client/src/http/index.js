import axios from "axios"
import { SERVER_LINK } from "../utils/consts"

const $host = axios.create({
	baseURL: SERVER_LINK,
})

const $authHost = axios.create({
	baseURL: SERVER_LINK,
})

const authInterceptor = (config) => {
	config.headers.authorization = `Bearer ${localStorage.getItem("token")}`
	config.headers["Access-Control-Allow-Origin"] = "*"
	config.headers["ngrok-skip-browser-warning"] = true

	return config
}

$authHost.interceptors.request.use(authInterceptor)

export { $host, $authHost }
