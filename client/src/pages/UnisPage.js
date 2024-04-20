import React from 'react'
import { Container, Row, Col, Card } from 'react-bootstrap'

const universities = [
	{ id: 1, name: 'University 1', image: 'image1.jpg' },
	{ id: 2, name: 'University 2', image: 'image2.jpg' },
	//... add more universities here
]

const UniversityCard = ({ university }) => (
	<Col md={4}>
		<Card>
			<Card.Img variant="top" src={university.image} />
			<Card.Body>
				<Card.Title>{university.name}</Card.Title>
			</Card.Body>
		</Card>
	</Col>
)

const UnisPage = () => {
	return (
		<Container>
			<Row>
				{universities.map((university) => (
					<UniversityCard key={university.id} university={university} />
				))}
			</Row>
		</Container>
	)
}

export default UnisPage
