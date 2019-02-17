import { all } from 'redux-saga/effects'
import { watchPostDogClassifier } from './data/dogClassifier/saga'


export default function* rootSaga() {
  yield all([
    watchPostDogClassifier(),
  ])
}