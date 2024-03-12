import { api } from 'boot/axios'
import { Employee } from 'src/models/employee'

export function useEmployee() {

	const getEmployeeList = async () => {
		return api.get<Employee[]>(
			'employees/employee/list'
		)
	}

	return {
		getEmployeeList,
	}
}
