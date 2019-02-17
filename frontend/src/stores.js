import { createStore, applyMiddleware } from 'redux'
import createSagaMiddleware from 'redux-saga'

import reducers from './reducers'
import rootSaga from './sagas'

/**
 * Create Redux store
 */
export default function configureStore() {
  const sagaMiddleware = createSagaMiddleware()

  return {
    ...createStore(reducers,
      applyMiddleware(sagaMiddleware)
    ),
    runSaga: sagaMiddleware.run(rootSaga)
  }
}