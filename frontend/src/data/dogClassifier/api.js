/**
 * Action for classifying image and identifying dog breed
 * @param {params} params
 */
export const postDogClassifier = (params) => {
  const image = params.image
  if (!image) return;

  const url = 'http://localhost:5000/api/classifier/'

  let form = new FormData()
  form.append('image', image)

  return fetch(url, {
    method: 'POST',
    body: form
  })
    .then(res => res.json())
    .then(res => res)
}