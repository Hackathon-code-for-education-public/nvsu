import React, { createContext } from 'react'
import ReactDOM from 'react-dom'
import App from './App'
import UserStore from './store/UserStore'
import './index.css'

export const Context = createContext(null)

console.log(process.env)

ReactDOM.render(
	<Context.Provider
		value={{
			user: new UserStore(),
		}}
	>
		<App />
	</Context.Provider>,
	document.getElementById('root')
)
