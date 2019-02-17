import { combineReducers } from 'redux'

import dogClassifierReducer from './data/dogClassifier/reducer'


export default combineReducers({
  dog: dogClassifierReducer,
})