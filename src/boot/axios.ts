import { boot } from 'quasar/wrappers'
import axios, { AxiosInstance } from 'axios'

declare module '@vue/runtime-core' {
	interface ComponentCustomProperties {
		$axios: AxiosInstance
		$api: AxiosInstance
	}
}

const api = axios.create({
	baseURL: process.env.DEV ? 'http://localhost:8000/api/v1/' : '/api/v1/',
	withCredentials: true,
	headers: { 'Content-Type': 'application/json' },
})

export default boot(({ app }) => {
	// for use inside Vue files (Options API) through this.$axios and this.$api

	app.config.globalProperties.$axios = axios
	// ^ ^ ^ this will allow you to use this.$axios (for Vue Options API form)
	//       so you won't necessarily have to import axios in each vue file

	app.config.globalProperties.$api = api
	// ^ ^ ^ this will allow you to use this.$api (for Vue Options API form)
	//       so you can easily perform requests against your app's API
})

export { api }
