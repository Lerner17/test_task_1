# test_task_1

## api

**POST** `/api/v1/vision/`

**body:** `{ "image": "<image uri>" }`

return list of objects on image or error



## Example:


**Request body**
`
{
	"image": "https://d17fnq9dkz9hgj.cloudfront.net/breed-uploads/2018/09/dog-landing-hero-lg.jpg?bust=1536935129&width=1080"
}
`

**Response 200:**
`
{
    "objects": [
        "Dog"
    ]
}
`
