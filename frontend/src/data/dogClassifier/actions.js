import {
  POST_DOG_CLASSIFIER
} from './constants'


export const classifyDog = image => {
  return {
    type: POST_DOG_CLASSIFIER,
    image
  }
}