import Admin from './pages/Admin'
import { ADMIN_ROUTE, LOGIN_ROUTE, REGISTRATION_ROUTE } from './utils/consts'
import Auth from './pages/Auth'

export const adminRoutes = [
	{
		path: ADMIN_ROUTE,
		Component: Admin,
	},
]

export const authRoutes = [{}]

export const publicRoutes = [
	{
		path: LOGIN_ROUTE,
		Component: Auth,
	},
	{
		path: REGISTRATION_ROUTE,
		Component: Auth,
	},
]
