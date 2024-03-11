import { defineStore } from 'pinia'

export const useDataStore = defineStore('dataStore', {
	state: () => ([{
		count: 0,
		name: 'Разработка котиков',
		amountOfPeople: 200,
		price: 1200,
		progress: 50.5,
		lastChange: 'Игорь Николаевич',
		dueDate: '23.05.2023',
		condition: 'Не перспективный',
		developmentStage: 'Аналитика',
	},
	{
		count: 0,
		name: 'Разработка котиковdasd',
		amountOfPeople: 200,
		price: 1200,
		progress: 50.5,
		lastChange: 'Игорь Николаевич',
		dueDate: '23.05.2023',
		condition: 'Не перспективный',
		developmentStage: 'Аналитика',
	}
	])
})