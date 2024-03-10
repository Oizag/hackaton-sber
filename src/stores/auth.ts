import { defineStore } from 'pinia'



export const useAuthStore = defineStore('authStore', {
	state: () => ({
		isLoginForm: true as boolean | undefined
	}),
})