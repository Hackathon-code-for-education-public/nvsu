import React from 'react'
import { Container, Row, Col, Card, Button } from 'react-bootstrap'
import { useUniversityStore } from '../store/UniversityStore'
import { useParams } from 'react-router-dom'

const UniPage = () => {
	const { getUniversity } = useUniversityStore()
	const { id } = useParams()
	const university = {
		name: 'Нижневартовский ГУ',
		videoUrl: 'Ссылочка',
		image: 'Ссылочка на картинку',
		description: 'Классный ВУЗ, ничего не скажешь',
		analytics: {
			budgetPlaces: 10,
			faculties: 5,
			specialities: 30,
			graduates: 4,
		},
	}
	// getUniversity(id)

	return (
		<Container>
			<Row className="mt-4">
				<Col>
					<h2>{university.name}</h2>
					<iframe
						width="560"
						height="315"
						src={university.videoUrl}
						frameBorder="0"
						allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
						allowFullScreen
					></iframe>
				</Col>
			</Row>
			<Row className="mt-4">
				<Col md={6}>
					<Card>
						<Card.Img variant="top" src={university.image} />
						<Card.Body>
							<Card.Title>{university.name}</Card.Title>
							<Card.Text>{university.description}</Card.Text>
							<Button
								variant="primary"
								href={university.website}
								target="_blank"
							>
								Visit Website
							</Button>
						</Card.Body>
					</Card>
				</Col>
				<Col md={6}>
					<h3>Analytics</h3>
					<p>Budget Places: {university.analytics.budgetPlaces}</p>
					<p>Faculties: {university.analytics.faculties}</p>
					<p>Specialities: {university.analytics.specialities}</p>
					<p>Graduates: {university.analytics.graduates}</p>
				</Col>
			</Row>
			<Row className="mt-4">
				<Col>
					<h3>Reviews</h3>
					{/* Add reviews here */}
				</Col>
			</Row>
		</Container>
	)
}

export default UniPage
