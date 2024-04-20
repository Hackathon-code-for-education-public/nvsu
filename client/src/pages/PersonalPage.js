import React, { useContext } from 'react'
import { Container, Card, Button } from 'react-bootstrap'
import { observer } from 'mobx-react-lite'
import { Context } from '../index'

const PersonalPage = observer(() => {
	const { user } = useContext(Context)

	return (
		<Container
			className="d-flex justify-content-center align-items-center"
			style={{ height: window.innerHeight - 95 }}
		>
			<Card style={{ width: 300 }} className="p-4">
				<div className="d-flex justify-content-center align-items-center">
					<img
						src={user.user.avatar}
						alt="avatar"
						width="100px"
						height="100px"
					/>
				</div>
				<div className="mt-3 text-center">
					<h4>{user.user.fullName}</h4>
					<h5>{user.user.university}</h5>
					<h6>{user.user.role}</h6>
				</div>
				<Button variant="primary" className="mt-3">
					Edit Profile
				</Button>
			</Card>
		</Container>
	)
})

export default PersonalPage
