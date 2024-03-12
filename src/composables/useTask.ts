import { api } from 'boot/axios'
import { Task } from 'src/models/task'

export function useTask() {

	const getTaskList = async () => {
		return api.get<Task[]>(
			'company/task/list'
		)
	}

	return {
		getTaskList,
	}
}
