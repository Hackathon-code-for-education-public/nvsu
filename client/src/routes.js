import Admin from './pages/Admin'
import {
	ADMIN_ROUTE,
	BASKET_ROUTE,
	DEVICE_ROUTE,
	LOGIN_ROUTE,
	REGISTRATION_ROUTE,
	SHOP_ROUTE,
} from './utils/consts'
import Basket from './pages/Basket'
import Shop from './pages/Shop'
import Auth from './pages/Auth'
import DevicePage from './pages/DevicePage'

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
