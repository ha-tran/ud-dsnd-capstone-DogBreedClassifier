import React, { Component } from 'react'
import Dropzone from 'react-dropzone'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'
import { classifyDog } from '../data/dogClassifier/actions'

import Breed from './Breed'


class ImageUpload extends Component {
  state = {
    imgSrc: null,
    imgAlt: ''
  }

  onDrop = (files, rejected) => {
    if (!files || !files.length) return

    const image = files[0]

    const reader = new FileReader()
    reader.readAsDataURL(image)
    reader.onloadend = e => {
      this.setState({
        imgSrc: [reader.result],
        imgAlt: image.name || 'User image'
      })
    }

    this.props.dispatch(classifyDog(image))
  }

  render() {
    const { imgSrc, imgAlt } = this.state
    const { dog } = this.props

    return(
      <div>
        <Dropzone
          accept="image/*"
          onDrop={this.onDrop}
        >
          Drag image file here...
        </Dropzone>

        {
          imgSrc
            ? <img src={imgSrc} alt={imgAlt} />
            : null
        }

        <Breed dog={dog.dog} />
      </div>
    )
  }
}

ImageUpload.propTypes = {
  dog: PropTypes.object,
}

const mapStateToProps = ({ dog }) => ({
  dog,
  classifyDog
})

export default connect(mapStateToProps)(ImageUpload)