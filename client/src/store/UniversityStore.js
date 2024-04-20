import create from 'zustand'

export const useUniversityStore = create((set, get) => ({
	universities: [],
	setUniversities: (universities) => set({ universities }),
	clearUniversities: () => set({ universities: [] }),
	getUniversity: (id) => {
		const store = get()
		return store.universities.find((university) => university.id === id)
	},
}))
