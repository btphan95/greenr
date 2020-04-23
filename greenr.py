#deep learning libraries
from fastai.vision import *
import torch
defaults.device = torch.device('cpu')

#web frameworks
from starlette.applications import Starlette
from starlette.responses import JSONResponse, HTMLResponse, RedirectResponse
import uvicorn
import aiohttp
import asyncio

import sys

async def get_bytes(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()

app = Starlette()

path = Path('data/greenr')

img = open_image(path/'grass'/'00000025.jpg')
learner = load_learner(path)

pred_class,pred_idx,outputs = learner.predict(img)
print(pred_class)


@app.route("/upload", methods = ["POST"])
async def upload(request):
    data = await request.form()
    bytes = await (data["file"].read())
    return predict_image_from_bytes(bytes)

@app.route("/classify-url", methods = ["GET"])
async def classify_url(request):
    bytes = await get_bytes(request.query_params["url"])
    return predict_image_from_bytes(bytes)

def predict_image_from_bytes(bytes):
    img_file = open("img.jpg", "wb")
    img_file = io.BytesIO(bytes)
    img = open_image(img_file)
    pred_class, pred_idx, outputs = learner.predict(img)
    formatted_outputs = ["{:.1f}%".format(value) for value in [x * 100 for x in torch.nn.functional.softmax(outputs, dim = 0)]]
    pred_probs = sorted(zip(learner.data.classes, map(str, formatted_outputs)),
                        key = lambda p: p[1],
                        reverse = True
                       )
    return HTMLResponse(
        """
        <html>
            <body>
                <p> Prediction: <b> %s </b> </p>
                <Confidence: %s </p>
            </body>
        <figure class = "figure">
            <img src = %s class = "figure-img">
        </figure>
        </html>
        """ %(pred_class, pred_probs, "img.jpg"))
        
@app.route("/")
def form(request):
        return HTMLResponse(
            """
            <h1> Greenr </h1>
            <p> Is your picture of a dandelion or grass? </p>
            <form action="/upload" method = "post" enctype = "multipart/form-data">
                <u> Select picture to upload: </u> <br> <p>
                1. <input type="file" name="file"><br><p>
                2. <input type="submit" value="Upload">
            </form>
            <br>
            <br>
            <u> Submit picture URL </u>
            <form action = "/classify-url" method="get">
                1. <input type="url" name="url" size="60"><br><p>
                2. <input type="submit" value="Upload">
            </form>
            """)
        
@app.route("/form")
def redirect_to_homepage(request):
        return RedirectResponse("/")
        
if __name__ == "__main__":
        if "serve" in sys.argv:
            uvicorn.run(app, host = "0.0.0.0", port = 8008)