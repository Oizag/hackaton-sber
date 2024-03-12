import { defineStore } from 'pinia'

export const useProjectStore = defineStore('projectStore', {
	state: () => ({
		projectObject: {} as object | undefined

	}),
})