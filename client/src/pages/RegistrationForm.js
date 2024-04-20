import React, { useState } from 'react'
import { Container, Form, Button, Alert } from 'react-bootstrap'

const RegistrationForm = () => {
	const [role, setRole] = useState('')
	const [errors, setErrors] = useState({})

	const validateForm = () => {
		const newErrors = {}
		// здесь добавьте валидацию полей формы
		// и добавьте сообщения об ошибках в объект newErrors
		setErrors(newErrors)
		return Object.keys(newErrors).length === 0
	}

	const handleSubmit = (event) => {
		event.preventDefault()
		if (!validateForm()) {
			return
		}
		// здесь обработайте отправку формы
	}

	return (
		<Container
			className="d-flex justify-content-center align-items-center py-5"
			style={{ height: window.innerHeight - 95 }}
		>
			<Form onSubmit={handleSubmit}>
				<Form.Group>
					<Form.Label>Фамилия</Form.Label>
					<Form.Control type="text" />
					{errors.surname && <Alert variant="danger">{errors.surname}</Alert>}
				</Form.Group>

				<Form.Group>
					<Form.Label>Имя</Form.Label>
					<Form.Control type="text" />
					{errors.name && <Alert variant="danger">{errors.name}</Alert>}
				</Form.Group>

				<Form.Group>
					<Form.Label>Отчество</Form.Label>
					<Form.Control type="text" />
					{errors.patronymic && (
						<Alert variant="danger">{errors.patronymic}</Alert>
					)}
				</Form.Group>

				<Form.Group>
					<Form.Label>Роль</Form.Label>
					<Form.Control as="select" onChange={(e) => setRole(e.target.value)}>
						<option>Абитуриент</option>
						<option>Студент</option>
						<option>Представитель университета</option>
					</Form.Control>
				</Form.Group>

				<Form.Group>
					<Form.Label>Фото паспорта</Form.Label>
					<Form.Control type="file" accept=".jpg, .jpeg, .png, .pdf" />
					{errors.passport && <Alert variant="danger">{errors.passport}</Alert>}
				</Form.Group>

				{role === 'Студент' && (
					<Form.Group>
						<Form.Label>Фото студенческого билета</Form.Label>
						<Form.Control type="file" accept=".jpg, .jpeg, .png, .pdf" />
						{errors.studentCard && (
							<Alert variant="danger">{errors.studentCard}</Alert>
						)}
					</Form.Group>
				)}

				{role === 'Представитель университета' && (
					<Form.Group>
						<Form.Label>Документ, подтверждающий статус</Form.Label>
						<Form.Control type="file" accept=".jpg, .jpeg, .png, .pdf" />
						{errors.document && (
							<Alert variant="danger">{errors.document}</Alert>
						)}
					</Form.Group>
				)}

				<Button className="" type="submit">
					Зарегистрироваться
				</Button>
			</Form>
		</Container>
	)
}

export default RegistrationForm
