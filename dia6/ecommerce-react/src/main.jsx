import React from 'react'
import ReactDOM from 'react-dom/client'
import router from './router/Router'
import { RouterProvider } from 'react-router-dom'

import './assets/css/bootstrap.css'
import './assets/css/chosen.css'
import './assets/css/elements-media.css'
import './assets/css/elements.css'
import './assets/css/font-awesome.min.css'
import './assets/css/media.css'
import './assets/css/style.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <RouterProvider router={router} />
)
