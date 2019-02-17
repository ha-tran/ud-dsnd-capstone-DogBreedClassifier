import { takeLatest } from 'redux-saga/effects'
import {
  call,
  put
} from 'redux-saga/effects'
import {
  postDogClassifier
} from './api'
import {
  POST_DOG_CLASSIFIER,
  POST_DOG_CLASSIFIER_DONE,
  POST_DOG_CLASSIFIER_FAIL
} from './constants'


function *requestDogClassifier(image) {
  try {
    let response = yield call(postDogClassifier, image)

    yield put({ type: POST_DOG_CLASSIFIER_DONE, response })
  } catch (error) {
    yield put({ type: POST_DOG_CLASSIFIER_FAIL, error})
  }
}

export function* watchPostDogClassifier() {
  yield takeLatest(POST_DOG_CLASSIFIER, requestDogClassifier)
}