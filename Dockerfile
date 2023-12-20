FROM public.ecr.aws/lambda/python:3.8
RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/blob/main/tflite/tflite_runtime-2.5.2-cp38-cp38-linux_x86_64.whl?raw=true
RUN pip install Pillow
RUN pip install numpy
RUN pip install requests
COPY color-classifier-model.tflite .
COPY lambda_function.py .

CMD ["lambda_function.lambda_handler"]