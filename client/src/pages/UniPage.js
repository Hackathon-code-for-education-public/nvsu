import React, { useEffect, useState } from 'react'
import { Container, Row, Col, Card, Button } from 'react-bootstrap'
import { useUniversityStore } from '../store/UniversityStore'
import { useParams } from 'react-router-dom'
import './uni.css'
import Panorama from '../components/Pannorama'
import { getUniversityById } from '../http/uniApi'

const UniPage = () => {
	const { id } = useParams()
	const [university, setUniversity] = useState({})

	// const { getUniversity } = useUniversityStore()

	useEffect(() => {
		getUniversityById(id).then((data) => {
			setUniversity(data)
		})
	}, [])

	// const university = {
	// 	name: 'Нижневартовский Государственный университет',
	// 	videoUrl: '/testVideo.mp4',
	// 	website: 'https://nvsu.ru/',
	// 	image: 'https://nvsu.ru/img/corpus.png',
	// 	description: 'Классный ВУЗ, ничего не скажешь',
	// 	analytics: {
	// 		budgetPlaces: 10,
	// 		faculties: 5,
	// 		specialities: 30,
	// 		graduates: 4,
	// 	},
	// }
	// getUniversity(id)

	return (
		<Container>
			{/* Main */}
			<Row className="mt-4">
				<Col>
					<h2 className="d-flex justify-content-center">{university.name}</h2>
				</Col>
			</Row>
			{/* Video */}
			{university.videoUrl && (
				<Row className="mt-4">
					<Col>
						<video className="w-100" controls>
							{/* <source src="/video-example.webm" type="video/webm" /> */}
							<source src={university.videoUrl} type="video/mp4" />
							Sorry, your browser doesn't support videos.
						</video>
					</Col>
				</Row>
			)}

			<Row className="mt-5">
				<Container fluid>
					<Card>
						<Card.Img
							className="card__image_uni"
							variant="top"
							src={university.image}
						/>
						<Card.Body>
							<Card.Title>{university.name}</Card.Title>
							<Card.Text>{university.description}</Card.Text>
							<Button
								className="btn"
								variant="primary"
								href={university.site_url}
								target="_blank"
							>
								Visit Website
							</Button>
						</Card.Body>
					</Card>
				</Container>
			</Row>
			<Row className="mt-4">
				<Panorama university={university} />
			</Row>
			<Row className="mt-4">
				<Col md={6}>
					<h3>Analytics</h3>
					<p>Budget Places: {university?.analytics?.budgetPlaces}</p>
					<p>Faculties: {university?.analytics?.faculties}</p>
					<p>Specialities: {university?.analytics?.specialities}</p>
					<p>Graduates: {university?.analytics?.graduates}</p>
					<Card.Text>Email: {university.email}</Card.Text>
					<Card.Text>Phone: {university.phone}</Card.Text>
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
