import React from 'react'


const Breed = ({ dog }) => {
  if (!dog) return (
    <div>
      <p>Upload image to classify dog images</p>
    </div>
  )

  if (!dog.is_dog) return (
    <div>
      <p>Model failed. Couldn't determine if picture contains a dog</p>
    </div>
  )

  let text

  if (dog.is_dog.toLowerCase() === 'true') {
    text = `The dog in the image is a ${dog.breed}`
  } else {
    text = `There are no dogs in the image. Anyway, the classified breed is ${dog.breed}`
  }

  return (
    <div>
      <p>{text}</p>
    </div>
  )
}

export default Breed