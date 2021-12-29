let model, canvas
async function setup(){
    canvas = createCanvas(400,400)
    background(0)
    model = await tf.loadGraphModel("modeljs/model.json")
}

function draw(){
    stroke(255)
    strokeWeight(18)

    
}

function mouseDragged(){
    line(pmouseX,pmouseY,mouseX,mouseY)
    predict()
}

function showText(message){
    const element = document.querySelector("div.prediction-text")
    element.textContent = message
}

function predict(){
    const pixels = tf.browser.fromPixels(canvas.elt)
    const input = tf.image.resizeBilinear(pixels,[28,28]).mean(2)
    .toFloat()
    .expandDims(-1).expandDims(0).div(255)
    const output = model.predict([input])
    const prediction = output.argMax(-1).arraySync()[0]
    const predictionText = `Prediction of ${prediction}`    
    showText(predictionText)
    // setTimeout(predict,500)
}