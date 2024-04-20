import React, { useContext } from 'react'
import { Switch, Route, Redirect } from 'react-router-dom'
import { adminRoutes, authRoutes, publicRoutes } from '../routes'
import { Context } from '../index'
import { observer } from 'mobx-react-lite'
import { DEFAULT_ROUTE } from '../utils/consts'

const AppRouter = observer(() => {
	const { user } = useContext(Context)

	return (
		<Switch>
			{user.isAuth &&
				authRoutes.map(({ path, Component }) => (
					<Route key={path} path={path} component={Component} exact />
				))}
			{user.isAuth &&
				user.user.role === 'ADMIN' &&
				adminRoutes.map(({ path, Component }) => (
					<Route key={path} path={path} component={Component} exact />
				))}
			{publicRoutes.map(({ path, Component }) => (
				<Route key={path} path={path} component={Component} exact />
			))}
			<Redirect to={DEFAULT_ROUTE} />
		</Switch>
	)
})

export default AppRouter
