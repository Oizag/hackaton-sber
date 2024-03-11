import { api } from 'boot/axios'
import { Project } from 'src/models/project'

export function useProject() {

	const getProjectList = async () => {
		return api.get<Project[]>(
			'company/project/list'
		)
	}

	return {
		getProjectList,
	}
}
