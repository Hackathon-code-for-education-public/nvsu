import { $authHost, $host } from './index'

export const getAllUniversities = async () => {
	const { data } = await $host.get('universities/all')
	return data
}

export const getUniversityById = async (id) => {
	const { data } = await $host.get(`universities/${id}`)
	return data
}

export const createUniversity = async (universityData) => {
	const { data } = await $authHost.post('university/create', universityData)
	return data
}
