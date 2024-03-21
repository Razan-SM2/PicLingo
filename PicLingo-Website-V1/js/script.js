const token = "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"
const inputTxt = document.getElementById("text")
const image = document.getElementById("image")
const button = document.getElementById("btn")

async function query() {
	//image.src ="\loading.gif"
	const response = await fetch(
		"https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5",
		{
			headers: { Authorization: "Bearer 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" },
			method: "POST",
			body: JSON.stringify({"inputs": inputTxt.value}),
		}
	);
	const result = await response.blob();
	return result;
}

button.addEventListener('click', async function(){
    query().then((response) => {
        const objectURL = URL.createObjectURL(response)
        image.src = objectURL
    });

})