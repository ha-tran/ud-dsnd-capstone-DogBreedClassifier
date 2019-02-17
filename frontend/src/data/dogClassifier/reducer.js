import {
  POST_DOG_CLASSIFIER,
  POST_DOG_CLASSIFIER_DONE,
  POST_DOG_CLASSIFIER_FAIL
} from './constants'

const initState = {
  dog: null,
  error: null
}

export default function reducer(state = initState, action) {
  switch (action.type) {
    case POST_DOG_CLASSIFIER:
      return {
        ...state
      }

    case POST_DOG_CLASSIFIER_DONE:
      return {
        ...state,
        dog: action.response
      }

    case POST_DOG_CLASSIFIER_FAIL:
      return {
        ...state,
        error: action.error
      }

    default:
      return state
  }
}