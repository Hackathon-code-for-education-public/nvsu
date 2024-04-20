import {
	DEFAULT_ROUTE,
	ADMIN_ROUTE,
	LOGIN_ROUTE,
	REGISTRATION_ROUTE,
	PERSONAL_ROUTE,
	UNI_ROUTE,
} from './utils/consts'

import AdminPage from './pages/AdminPage'
import PersonalPage from './pages/PersonalPage'
import Auth from './pages/Auth'
import UnisPage from './pages/UnisPage'
import UniPage from './pages/UniPage'

export const adminRoutes = [
	{
		path: ADMIN_ROUTE,
		Component: AdminPage,
	},
]

export const authRoutes = [
	{
		path: PERSONAL_ROUTE,
		Component: PersonalPage,
	},
]

export const publicRoutes = [
	{
		path: DEFAULT_ROUTE,
		Component: UniPage,
	},
	{
		path: UNI_ROUTE,
		Component: UnisPage,
	},
	{
		path: LOGIN_ROUTE,
		Component: Auth,
	},
	{
		path: REGISTRATION_ROUTE,
		Component: Auth,
	},
]
