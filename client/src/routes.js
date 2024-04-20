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
import RegistrationForm from './pages/RegistrationForm'

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
		Component: UnisPage,
	},
	{
		path: UNI_ROUTE + '/:id',
		Component: UniPage,
	},
	{
		path: LOGIN_ROUTE,
		Component: Auth,
	},
	{
		path: REGISTRATION_ROUTE,
		Component: RegistrationForm,
	},
]
