import React, { useState, useContext, useEffect } from 'react'
import { Button, Container, Row, Col, Form, Dropdown } from 'react-bootstrap'
import { Context } from '../index'
// import { fetchBrands, fetchTypes } from '../http/deviceAPI'
import { observer } from 'mobx-react-lite'

const Admin = observer((props) => {
	// const { device } = useContext(Context)
	// const [brandVisible, setBrandVisible] = useState(false)
	// const [typeVisible, setTypeVisible] = useState(false)
	// const [deviceVisible, setDeviceVisible] = useState(false)

	useEffect(() => {
		// fetchTypes().then((data) => device.setTypes(data))
		// fetchBrands().then((data) => device.setBrands(data))
	}, [])

	const clickDropDownTypes = () => {
		// fetchTypes().then((data) => device.setTypes(data))
	}

	const clickDropDownBrands = () => {
		// fetchBrands().then((data) => device.setBrands(data))
	}

	// console.log(`device.brand`, JSON.stringify(device.brands, null, 2))
	// console.log(`device.types`, JSON.stringify(device.types, null, 2))
	return (
		<Container className="d-flex flex-column">
			<Row>
				{/* Первая сущность */}
				<Col md="4" className="mt-3 d-flex flex-column align-items-center">
					<Form.Label className="d-block mb-3">Корпуса</Form.Label>
					<Button
						variant={'outline-primary'}
						className="p-2 d-block"
						// onClick={() => setDeviceVisible(true)}
					>
						Добавить
					</Button>
					<Button variant="outline-danger" className="mt-2 p-2 d-block">
						Обновить (в разработке)
					</Button>
					<Button variant="outline-danger" className="mt-2 p-2 d-block">
						Удалить (в разработке)
					</Button>
				</Col>

				{/* Вторая сущность */}
				<Col md="4" className="mt-3 d-flex flex-column align-items-center">
					<Form.Label className="d-block mb-3">Этажи</Form.Label>
					<Button
						variant={'outline-primary'}
						className="p-2 d-block"
						// onClick={() => setTypeVisible(true)}
					>
						Добавить этаж
					</Button>
					<Button
						variant={'outline-primary'}
						className="p-2 d-block"
						// onClick={() => setTypeVisible(true)}
					>
						Обновить этаж
					</Button>
					<Button
						variant={'outline-primary'}
						className="p-2 d-block"
						// onClick={() => setTypeVisible(true)}
					>
						Удалить этаж
					</Button>
					<Dropdown className="mt-2" onClick={clickDropDownTypes}>
						<Dropdown.Toggle variant="info">{'Все категории'}</Dropdown.Toggle>
						<Dropdown.Menu>
							{/* {device.types.map((type) => (
								<Dropdown.Item key={type.id}>{type.name}</Dropdown.Item>
							))} */}
						</Dropdown.Menu>
					</Dropdown>
				</Col>

				{/* Третья сущность */}

				<Col md="4" className="mt-3 d-flex flex-column align-items-center">
					<Form.Label className="d-block mb-3">Аудитории</Form.Label>
					<Button
						variant={'outline-primary'}
						className="p-2 d-block"
						// onClick={() => setBrandVisible(true)}
					>
						Добавить аудиторию
					</Button>
					<Button variant="outline-danger" className="mt-2 p-2 d-block">
						Удалить аудиторию
					</Button>
					<Dropdown className="mt-2" onClick={clickDropDownBrands}>
						<Dropdown.Toggle variant="info">{'Все аудитории'}</Dropdown.Toggle>
						<Dropdown.Menu>
							{/* {device.brands.map((brand) => (
								<Dropdown.Item key={brand.id}>{brand.name}</Dropdown.Item>
							))} */}
						</Dropdown.Menu>
					</Dropdown>
				</Col>

				{/* {brandVisible && (
					<CreateBrand
						show={brandVisible}
						onHide={() => setBrandVisible(false)}
					/>
				)}
				{deviceVisible && (
					<CreateDevice
						show={deviceVisible}
						onHide={() => setDeviceVisible(false)}
					/>
				)}
				{typeVisible && (
					<CreateType show={typeVisible} onHide={() => setTypeVisible(false)} />
				)} */}
			</Row>
		</Container>
	)
})

export default Admin
