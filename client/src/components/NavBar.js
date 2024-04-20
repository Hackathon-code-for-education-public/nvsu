import React, { useContext } from 'react'
import { Context } from '../index'
import { NavLink, useHistory } from 'react-router-dom'
import {
	ADMIN_ROUTE,
	LOGIN_ROUTE,
	DEFAULT_ROUTE,
	PERSONAL_ROUTE,
} from '../utils/consts'
import { Container, Button, Nav, Navbar } from 'react-bootstrap'
import { observer } from 'mobx-react-lite'

import signUpIcon from '../assets/signUpIcon.png'

const NavBar = observer(() => {
	const { user } = useContext(Context)
	const history = useHistory()

	const logOut = () => {
		user.setUser({})
		user.setIsAuth(false)
		localStorage.removeItem('token')
	}

	console.log(`user: ${JSON.stringify(user.user.role, null, 2)}`)

	return (
		<Navbar className="border-bottom py-4 navbar-light bg-white sticky-top">
			<Container fluid>
				<Navbar.Brand className="d-flex align-items-center">
					<NavLink className="nav-link" to={DEFAULT_ROUTE}>
						canChooseUni
					</NavLink>
				</Navbar.Brand>
				<Navbar.Toggle aria-controls="basic-navbar-nav" />
				<Navbar.Collapse id="basic-navbar-nav" className="w-100">
					<Nav className="ml-auto" style={{ color: 'white' }}>
						{user.isAuth ? (
							<>
								{user.user.role === 'ADMIN' && (
									<Button
										variant={'outline-primary'}
										onClick={() => history.push(ADMIN_ROUTE)}
										className="mr-4 mb-1"
									>
										Управление сайтом
									</Button>
								)}
								<Button
									variant={'outline-primary'}
									onClick={() => history.push(PERSONAL_ROUTE)}
									className="mr-4 mb-1"
								>
									Личный кабинет
								</Button>
								<Button
									variant={'outline-dark'}
									onClick={() => logOut()}
									className="ml-2"
								>
									Выйти
								</Button>
							</>
						) : (
							<Button
								variant={'outline-primary'}
								onClick={() => history.push(LOGIN_ROUTE)}
							>
								<img src={signUpIcon} alt="Войти" />
								Войти
							</Button>
						)}
					</Nav>
				</Navbar.Collapse>
			</Container>
		</Navbar>
	)
})

export default NavBar
