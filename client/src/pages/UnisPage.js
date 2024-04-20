import React, { useEffect, useState } from 'react'
import { Container, Row, Col, Card } from 'react-bootstrap'
import { getAllUniversities } from '../http/uniApi'
import { UNI_ROUTE } from '../utils/consts'
import { NavLink } from 'react-router-dom'

const UniversityCard = ({ university }) => (
	<Col md={4}>
		<Card>
			<Card.Img variant="top" src={university.image} />
			<Card.Body>
				<Card.Title>{university.name}</Card.Title>
				<Card.Text>{university.description}</Card.Text>
				<NavLink to={`${UNI_ROUTE}/${university.id}`}>Ссылка</NavLink>
			</Card.Body>
		</Card>
	</Col>
)

const UnisPage = () => {
	const [universities, setUniversities] = useState([])

	useEffect(() => {
		const formData = async () => {
			const unis = await getAllUniversities()
			setUniversities(unis.universities)
		}

		formData()
	}, [])

	return (
		<Container>
			<Row
				className="position-relative d-flex justify-content-center align-items-center"
				style={{ height: '100vh' }}
			>
				{universities.length > 0 ? (
					universities.map((university) => (
						<UniversityCard key={university.id} university={university} />
					))
				) : (
					<p className="position-absolute text-center fs-3">
						Видимо, у вас проблемы с интернетом или у нас легла спать база
						данных. Уже разбираемся {':D'}
					</p>
				)}
			</Row>
		</Container>
	)
}

export default UnisPage
