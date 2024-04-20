import React, { useContext } from 'react'
import { Context } from '../index'
import { NavLink, useHistory } from 'react-router-dom'
import {
	ADMIN_ROUTE,
	LOGIN_ROUTE,
	SHOP_ROUTE,
	BASKET_ROUTE,
} from '../utils/consts'
import { Container, Button, Form, Nav, Navbar } from 'react-bootstrap'
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

	const clickSearch = (e) => {
		e.preventDefault()
	}

	console.log(`user: ${JSON.stringify(user.user.role, null, 2)}`)

	return (
		<Navbar className="border-bottom py-4">
			<Container fluid>
				<Navbar.Brand className="d-flex align-items-center">
					<NavLink className="nav-link" to={SHOP_ROUTE}>
						НВГУ
					</NavLink>
				</Navbar.Brand>
				<Navbar.Toggle aria-controls="basic-navbar-nav" />
				<Navbar.Collapse id="basic-navbar-nav" className="w-100">
					{/* <Nav className="w-100">
						<Form className="d-flex navbar-seacrh w-100 m-auto">
							<button
								className="navbar--search__button"
								title="Искать"
								type="submit"
								onClick={clickSearch}
							>
								<img src={search} alt="поиск" />
							</button>
						</Form>
					</Nav> */}
				</Navbar.Collapse>
				{user.isAuth ? (
					<Nav className="ml-3">
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
							onClick={() => history.push(BASKET_ROUTE)}
							className="mr-4 mb-1"
						>
							{/* <img src={basket} alt="Личный кабинет" /> */}
							Личный кабинет
						</Button>
						<Button
							variant={'outline-dark'}
							onClick={() => logOut()}
							className="ml-2"
						>
							Выйти
						</Button>
					</Nav>
				) : (
					<Nav className="ml-auto" style={{ color: 'white' }}>
						<Button
							variant={'outline-primary'}
							onClick={() => history.push(LOGIN_ROUTE)}
						>
							<img src={signUpIcon} alt="Войти" />
							Войти
						</Button>
					</Nav>
				)}
			</Container>
		</Navbar>
	)
})

export default NavBar
