import React from 'react'
import { Container } from 'semantic-ui-react'

import Footer from './layout/Footer'
import Header from './layout/Header'
import Main from './layout/Main'


const App = () => {
  return (
    <Container>
      <Header />
      <Main />
      <Footer />
    </Container>
  )
}

export default App